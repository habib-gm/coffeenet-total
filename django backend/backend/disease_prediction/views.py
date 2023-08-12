from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import tensorflow as tf
from .models import *
from .predictionSerializers import *
import cv2 as cv
import numpy as np
from django.core.files.base import ContentFile

# Create your views here.

interpreter = tf.lite.Interpreter(
    model_path="models/coffee_leaf_binary_network_efficientnetv2_b0_adam0_0003_batch128.tflite"
)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
segmentationModel = tf.keras.models.load_model(
    "models/segmentation_model.h5", compile=False
)

classificationModel = tf.keras.models.load_model("models/class_new_5.h5", compile=False)

leafSegmentationModel = tf.keras.models.load_model(
    "models/leaf_segmentation.h5", compile=False
)

DISEASE_NAMES = ["free_feeder", "leaf_rust", "leaf_skeletonizer"]

COLORS = [(0, 0, 255), (255, 0, 0), (100, 100, 0)]


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def predict(request):
    data = request.data
    requestImage = data["image"]
    image = grab_image(stream=request.FILES["image"])
    imageSize = image.shape[:2]
    user = request.user
    imageName = data["imageName"]
    scanned = True if data.get("scanned").lower() == "true" else False

    verificationImage = cv.resize(image, (224, 224))
    verificationImage = np.reshape(verificationImage, (1, 224, 224, 3))
    input_data = np.array(verificationImage, dtype=np.float32)
    interpreter.set_tensor(input_details[0]["index"], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]["index"])[0][0]
    if output_data > 0.2:
        return Response("invalid image", status=400)

    rotated = False
    if image.shape[0] > image.shape[1]:
        image = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
        rotated = True

    image = cv.resize(image, (512, 256))
    predictedImage, predictedDiseases, severity = segmentImage(image=image)
    prediction = Prediction(
        imageName=imageName,
        user=user,
        image=requestImage,
        scanned=scanned,
        severity=severity,
    )

    if rotated:
        predictedImage = cv.rotate(predictedImage, cv.ROTATE_90_CLOCKWISE)

    predictedImage = cv.resize(predictedImage, imageSize[::-1])
    ret, buf = cv.imencode(".jpg", predictedImage)
    content = ContentFile(buf.tobytes())
    prediction.predictedImage.save(imageName, content)

    diseaseObjects = []

    for diseaseName in predictedDiseases:
        disease = Disease.objects.get_or_create(name=diseaseName)
        diseaseObjects.append(disease)

    for disease, exist in diseaseObjects:
        prediction.diseases.add(disease)

    serializer = PredictionSerializer(prediction)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllData(request):
    user = request.user
    predictions = Prediction.objects.filter(user=user)
    serializer = PredictionSerializer(predictions, many=True)
    return Response(serializer.data)


def segmentImage(image):
    segmentation = segmentationModel.predict(np.array([image]))
    segmentation = segmentation[0]
    segmentation = np.amax(segmentation, axis=-1)
    segmentation[segmentation >= 0.5] = 1
    segmentation[segmentation < 0.5] = 0
    segmentation = segmentation * 255
    currDiseases = set()
    segmentation = np.array(segmentation, np.uint8)
    contours, hierarchy = cv.findContours(
        segmentation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )

    if contours:
        leafMask = leafSegmentationModel.predict(np.array([image]))[0]
        leafMask = leafMask >= 0.5
        leafArea = np.sum(leafMask)
        maskArea = segmentation == 255
        diseasedArea = np.sum(maskArea)
        severity = diseasedArea / (leafArea - diseasedArea)
    else:
        severity = 0

    originalImage = image.copy()

    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        croppedImage = image[y : y + h, x : x + w]

        if w < 7 or h < 7:
            continue

        croppedImage = cv.resize(croppedImage, (150, 150))
        output = classificationModel.predict(np.array([croppedImage]))[0]
        diseaseIndex = max(list(range(len(output))), key=lambda x: output[x])
        currDisease = DISEASE_NAMES[diseaseIndex]
        thickness = 5
        cv.drawContours(image, [cnt], 0, COLORS[diseaseIndex], -thickness)
        cv.fillConvexPoly(image, cnt, COLORS[diseaseIndex])
        currDiseases.add(currDisease)

    predictedImage = cv.addWeighted(originalImage, 0.6, image, 0.4, 0)

    return predictedImage, list(currDiseases), severity


def grab_image(stream):
    data = stream.read()
    image = np.asarray(bytearray(data), dtype="uint8")
    image = cv.imdecode(image, cv.IMREAD_COLOR)

    return image

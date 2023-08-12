# Coffeenet — Detecting Coffee Leaf Diseases with AI 🌿☕

![Coffeenet Banner](https://github.com/habib-gm/coffeenet-total/blob/master/Assets/coffeenet.png)

Welcome to Coffeenet, your smart partner in ensuring the health of your coffee plants! Powered by cutting-edge artificial intelligence and deep learning, Coffeenet is your reliable assistant for identifying and combatting coffee leaf diseases. Let's dive into the world of Coffeenet and see how it can revolutionize your coffee plantation.

## Detecting Coffee Diseases with Precision

Coffeenet boasts an impressive capability to identify not just one, but three major coffee leaf diseases:

1. **Free Feeder**
2. **Leaf Rust**
3. **Leaf Skeletonizer**

With Coffeenet, you'll be equipped to tackle these threats head-on and take proactive measures to safeguard your precious coffee plants.

## The Power of Deep Learning Models

Our robust deep learning models drive Coffeenet's accurate disease detection process:

1. **coffee_leaf_binary_network_efficientnetv2_b0_adam0_0003_batch128**: Before delving into disease detection, this model classifies whether an object is a coffee leaf or not.
   - [Model Details](machine_learning_models/coffee_leaf_binary_network_efficientnetv2_b0_adam0_0003_batch128.tflite)

2. **leaf_segmentation and segmentation_model**: These heroes handle leaf segmentation, isolating the leaf from the background, and skillfully detecting and segmenting the disease-affected areas.
   - [Leaf Segmentation Model](machine_learning_models/leaf_segmentation.h5)
   - [Segmentation Model](machine_learning_models/segmentation_model.h5)

3. **class_new_5**: Once the disease-affected area is isolated, this model identifies the specific coffee leaf disease with remarkable accuracy.

## Intuitive Mobile App and Robust Backend

Experience Coffeenet's power through our user-friendly mobile app, crafted with Flutter's cross-platform magic. The app follows best practices, featuring Domain-Driven Design (DDD) and BLoC for efficient state management. Its sleek design and intuitive navigation provide a seamless experience for both iOS and Android users.

But that's not all — the backend, developed using Django and Django Rest Framework, adds an extra layer of reliability. With user authentication, data synchronization, and specialized image storage, your coffee plant data stays safe and organized.

![Coffeenet splash screen](https://github.com/habib-gm/coffeenet-total/blob/master/Assets/splash%20screen.jpg)
![Coffeenet App login screen](https://github.com/habib-gm/coffeenet-total/blob/master/Assets/login%20screen.jpg)
![Coffeenet App detail page](https://github.com/habib-gm/coffeenet-total/blob/master/Assets/detail%20page.PNG)
![Coffeenet App Upload screen](https://github.com/habib-gm/coffeenet-total/blob/master/Assets/uploading.PNG)

## Exploring the Project Origins

Coffeenet is the brainchild of a dedicated intern team at the Ethiopian Artificial Intelligence Center. Our gratitude goes to FREX for contributing invaluable leaf disease data that fuels the Coffeenet engine.

## Getting Started with Coffeenet

Ready to join the revolution? Here's how:

1. Set the stage by installing Python, Django, and Flutter.
2. Clone this repository or grab the code. Focus on the `django_backend` and `flutter_mobile_application` folders — they're your launchpad to Coffeenet's world.
3. Launch the Django backend by navigating to the `django_backend` folder.
4. For the cherry on top, fire up the Flutter mobile app by heading to the `flutter_mobile_application` folder.

Get ready to embark on a journey towards healthier coffee plants and increased yields. Coffeenet has your back, every step of the way!

For a more comprehensive guide, dive into the documentation within the respective folders.

Visit the [Ethiopian Artificial Intelligence Center](http://www.aii.et/) to explore more groundbreaking projects.

Start brewing success with Coffeenet today! ☕🌱

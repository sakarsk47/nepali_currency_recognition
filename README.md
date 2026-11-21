
NEPALI CURRENCY DENOMINATION RECOGNITION USING DEEP LEARNING

Project Overview

This project was undertaken as part of my MSc Data Analytics dissertation. It focuses on the application of deep learning and computer vision techniques for the automatic detection and classification of Nepali currency denominations.

The system uses a trained convolutional neural network to classify images of Nepali banknotes into seven denomination categories. In addition to model development and evaluation, a Flask-based web application was implemented to demonstrate the practical use of the trained model.

The application supports both image-based and webcam-based recognition. It also incorporates audio announcements to communicate the predicted denomination, with the aim of improving accessibility for visually impaired users.

Recognized Denominations

The model identifies the following seven Nepali currency denominations:

- NPR 5
- NPR 10
- NPR 20
- NPR 50
- NPR 100
- NPR 500
- NPR 1000

Application Features

- Classification of seven Nepali banknote denominations.
- Image upload and denomination prediction.
- Webcam-based currency recognition.
- Image preprocessing before model prediction.
- Audio announcements of recognized denominations.
- Flask-based web interface for interacting with the model.

Methodology

The project explores deep learning-based image classification using convolutional neural networks. MobileNetV2 was investigated as a transfer learning architecture, alongside a baseline CNN, to examine their performance in recognizing Nepali currency denominations.

The development process involved dataset preparation, image preprocessing, model training, performance evaluation and implementation of the trained model in a web-based application.

Research Results

Dataset

The experiments were conducted using a dataset of 16,249 Nepali currency images representing seven denominations: NPR 5, NPR 10, NPR 20, NPR 50, NPR 100, NPR 500 and NPR 1,000.

The dataset was divided into three subsets:

| Dataset | Number of Images |
|:--------|-----------------:|
| Training | 10,500 |
| Validation | 3,500 |
| Testing | 2,249 |
| **Total** | **16,249** |

Model Performance Comparison

Three model configurations were evaluated: a baseline Convolutional Neural Network (CNN), MobileNetV2 using transfer learning, and MobileNetV2 with hyperparameter tuning.

| Model | Validation Accuracy | Test Accuracy | Precision | Recall | F1-score |
|:------|--------------------:|--------------:|----------:|-------:|---------:|
| Baseline CNN | 87% | 85% | 0.83 | 0.81 | 0.82 |
| MobileNetV2 (Transfer Learning) | 91% | 89% | 0.89 | 0.87 | 0.88 |
| MobileNetV2 (Hyperparameter Tuning) | 95% | 84% | 0.93 | 0.91 | 0.92 |

Key Findings

- MobileNetV2 with transfer learning achieved the highest independent test accuracy of 89%, outperforming the baseline CNN, which achieved    85%.
- Hyperparameter-tuned MobileNetV2 achieved the highest validation accuracy of 95%, along with the strongest reported precision, recall and   F1-score.
- Despite its higher validation accuracy, the tuned model achieved 84% test accuracy, indicating that its validation performance did not    translate into the highest performance on the independent test dataset.
- Classification errors were more frequent between visually similar denominations, particularly NPR 50 and NPR 100.
- Image quality, including lighting conditions, blur and banknote wear, remains an important consideration for reliable recognition.

These results demonstrate the potential of transfer learning and CNN-based approaches for Nepali currency denomination classification, while highlighting the importance of independent testing and further evaluation under diverse real-world conditions.


Technologies and Tools

- Python
- TensorFlow and Keras
- Convolutional Neural Networks
- MobileNetV2
- OpenCV
- NumPy
- Pillow
- Flask

Application Implementation

The developed Flask application provides two methods of currency recognition.

Image Upload

Users can upload an image of a Nepali banknote through the web interface. The application preprocesses the image and passes it to the trained model for denomination classification. The predicted denomination is displayed and communicated through an audio announcement.

Webcam Recognition

The application also supports webcam-based recognition. It captures video frames, processes the images and uses the trained model to identify the denomination. Once a banknote is recognised with sufficient confidence, the application displays and announces the prediction.

Research Background

This work was completed as part of my MSc Data Analytics dissertation at Islington College, in collaboration with London Metropolitan University.

Dissertation Title

Deep Learning Based Detection and Classification of Nepali Currency Denominations Using Optimized Convolutional Neural Networks.

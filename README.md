# Nepali Currency Denomination Recognition Using Deep Learning

## 1. Project Overview

This project was undertaken as part of my **MSc Data Analytics dissertation**. It focuses on the application of deep learning and computer vision techniques for the automatic detection and classification of Nepali currency denominations.

The system uses a trained **Convolutional Neural Network (CNN)** to classify images of Nepali banknotes into seven denomination categories. In addition to model development and evaluation, a **Flask-based web application** was implemented to demonstrate the practical application of the trained model.

The application supports both image-based and webcam-based recognition. It also incorporates audio announcements to communicate the predicted denomination, with the aim of improving accessibility for visually impaired users.

## 2. Recognised Currency Denominations

The model identifies the following seven Nepali currency denominations:

- NPR 5
- NPR 10
- NPR 20
- NPR 50
- NPR 100
- NPR 500
- NPR 1,000

## 3. Application Features

- Classification of seven Nepali banknote denominations.
- Image upload and denomination prediction.
- Real-time webcam-based currency recognition.
- Image preprocessing before model prediction.
- Audio announcements of recognised denominations.
- Flask-based web interface for interacting with the trained model.

## 4. Methodology

The project explores deep learning-based image classification using convolutional neural networks. **MobileNetV2** was investigated as a transfer learning architecture alongside a baseline CNN to examine their performance in recognising Nepali currency denominations.

The overall development process involved:

1. Dataset preparation and organisation.
2. Image preprocessing and augmentation.
3. CNN model development and training.
4. Transfer learning using MobileNetV2.
5. Hyperparameter tuning and model optimisation.
6. Performance evaluation using an independent test dataset.
7. Integration of the trained model into a Flask-based web application.

## 5. Model Development and Training

Three deep learning model configurations were developed and evaluated to investigate their effectiveness in classifying seven Nepali currency denominations.

### 5.1 Image Preprocessing and Augmentation

Before training, the currency images were prepared to ensure consistency across the dataset.

The preprocessing and augmentation procedures included:

- **Image resizing:** Images were resized to 128 × 128 pixels.
- **Normalisation:** Pixel values were scaled between 0 and 1.
- **Rotation:** Random rotations of up to ±15 degrees were applied.
- **Flipping:** Horizontal and vertical flipping introduced variations in image orientation.
- **Brightness adjustment:** Brightness variations simulated different lighting conditions.
- **Zooming and scaling:** These transformations introduced variations in image appearance and scale.

These techniques were used to improve the models' ability to recognise banknotes under varying image conditions and reduce overfitting.

### 5.2 Baseline Convolutional Neural Network (CNN)

A custom CNN architecture was developed from scratch to establish a baseline for comparison.

The architecture consisted of:

- **Convolutional layers:** Extract spatial features from input images.
- **Max-pooling layers:** Reduce feature dimensions while retaining important information.
- **Fully connected layers:** Learn patterns and relationships for classification.
- **Softmax output layer:** Predict one of the seven currency denominations.

The model was trained using the Adam optimiser and categorical cross-entropy loss.

### 5.3 MobileNetV2 with Transfer Learning

MobileNetV2 was implemented using pre-trained ImageNet weights to leverage previously learned image features.

The transfer learning approach involved:

1. Loading the pre-trained MobileNetV2 architecture.
2. Initially freezing the convolutional base to retain its pre-trained feature representations.
3. Adding a new fully connected classification layer for the seven Nepali currency denominations.
4. Training the classification layers on the currency dataset.
5. Unfreezing selected upper layers for further fine-tuning on the target dataset.

This approach leveraged the feature extraction capabilities of MobileNetV2 while adapting the model to Nepali currency classification.

### 5.4 MobileNetV2 with Hyperparameter Tuning

A further MobileNetV2 configuration was developed using hyperparameter optimisation to investigate improvements in classification performance.

Random search using **Keras Tuner** was employed to explore different hyperparameter combinations.

The parameters investigated included:

- **Learning rate:** Values ranging from 0.001 to 0.00001.
- **Batch size:** 16, 32 and 64.
- **Dropout rate:** Values between 0.2 and 0.5.
- **Dense layer units:** 128 to 512 neurons.
- **Activation functions:** Different activation configurations.

The optimal configuration was selected based on validation performance.

### 5.5 Model Training and Evaluation

The models were developed and trained using **TensorFlow and Keras**.

The documented training setup included:

- **Optimiser:** Adam.
- **Loss function:** Categorical cross-entropy.
- **Batch size:** 32 for the training setup.
- **Maximum training duration:** 20 epochs.
- **Learning rate adjustment:** ReduceLROnPlateau.
- **Early stopping:** Applied when validation loss stopped improving.

For MobileNetV2, the training process initially focused on the newly added classification layers, followed by fine-tuning selected layers of the pre-trained network.

Model performance was assessed using accuracy, precision, recall and F1-score. Additional evaluation included confusion matrix analysis, precision-recall curves and ROC-AUC analysis.

## 6. Research Results

### 6.1 Dataset

The experiments were conducted using a dataset of **16,249 Nepali currency images** representing seven denominations: NPR 5, NPR 10, NPR 20, NPR 50, NPR 100, NPR 500 and NPR 1,000.

The dataset was divided into three subsets:

| Dataset | Number of Images |
|:--|--:|
| Training | 10,500 |
| Validation | 3,500 |
| Testing | 2,249 |
| **Total** | **16,249** |

### 6.2 Model Performance Comparison

Three model configurations were evaluated: a baseline Convolutional Neural Network (CNN), MobileNetV2 using transfer learning, and MobileNetV2 with hyperparameter tuning.

| Model | Validation Accuracy | Test Accuracy | Precision | Recall | F1-score |
|:--|--:|--:|--:|--:|--:|
| Baseline CNN | 87% | 85% | 0.83 | 0.81 | 0.82 |
| MobileNetV2 (Transfer Learning) | 91% | 89% | 0.89 | 0.87 | 0.88 |
| MobileNetV2 (Hyperparameter Tuning) | 95% | 84% | 0.93 | 0.91 | 0.92 |

### 6.3 Key Findings

- **Best independent test accuracy:** MobileNetV2 with transfer learning achieved 89%, outperforming the baseline CNN, which achieved 85%.
- **Best validation accuracy:** Hyperparameter-tuned MobileNetV2 achieved 95%, along with the strongest reported precision, recall and F1-score.
- **Generalisation:** Despite its higher validation accuracy, the tuned model achieved 84% test accuracy, indicating that its validation performance did not translate into the highest performance on the independent test dataset.
- **Classification errors:** Errors were more frequent between visually similar denominations, particularly NPR 50 and NPR 100.
- **Image quality:** Lighting conditions, blur and banknote wear remain important considerations for reliable recognition.

These results demonstrate the potential of transfer learning and CNN-based approaches for Nepali currency denomination classification, while highlighting the importance of independent testing and further evaluation under diverse real-world conditions.

## 7. Technologies and Tools

The project was developed using the following technologies and tools:

- **Programming Language:** Python
- **Deep Learning Frameworks:** TensorFlow and Keras
- **Model Architectures:** Convolutional Neural Networks (CNNs), MobileNetV2
- **Computer Vision:** OpenCV
- **Image Processing:** Pillow
- **Numerical Computing:** NumPy
- **Web Application Framework:** Flask

## 8. Application Implementation

The developed Flask application provides two methods of currency recognition.

### 8.1 Image Upload and Recognition

Users can upload an image of a Nepali banknote through the web interface. The application preprocesses the image and passes it to the trained model for denomination classification. The predicted denomination is displayed and communicated through an audio announcement.

### 8.2 Webcam-Based Recognition

The application also supports real-time webcam-based recognition. It captures video frames, processes the images and uses the trained model to identify the denomination. Once a banknote is recognised with sufficient confidence, the application displays and announces the prediction.

### 8.3 Trained Model Integration

The deep learning model was trained and evaluated using **TensorFlow and Keras** as part of this research. Following model development and evaluation, the trained model was saved in HDF5 format as `cashRec.h5`.

The Flask application loads this saved model during startup and uses it to perform inference on uploaded banknote images and webcam input. This allows the application to classify Nepali currency denominations without requiring the model to be retrained each time the application is launched.

## 9. Research Background

This work was completed as part of my **MSc Data Analytics dissertation** at Islington College, in collaboration with London Metropolitan University.

**Dissertation Title:**

*Deep Learning Based Detection and Classification of Nepali Currency Denominations Using Optimized Convolutional Neural Networks.*

## 10. Application Demonstration

The following demonstrations showcase the practical implementation of the trained deep learning model within the Flask web application, including real-time currency recognition, image-based classification and audio feedback.

### 10.1 Application Setup and Web Interface

The application is developed using Flask and provides a web-based interface for interacting with the trained currency recognition model.

After executing `app.py` in VS Code, the Flask development server starts locally and displays the application URL (`http://127.0.0.1:5000`) in the terminal. Opening this URL in a web browser provides access to the Nepali Currency Recognition web application.

**Application Running in VS Code**

![Application running in VS Code](images/code.jpg)

**Main Web Application Interface**

![Web application interface](images/WebApplication.jpg)

### 10.2 Real-Time Currency Recognition

The application supports real-time currency recognition through a webcam. After selecting the live video option, the webcam is activated, allowing users to position a banknote within the designated detection area. The system predicts the denomination and displays the corresponding confidence score.

The demonstration shows successful recognition of NPR 50, NPR 10 and NPR 20 banknotes.

**Watch the Real-Time Currency Recognition Demonstration:**

[View Real-Time Recognition Video](https://youtube.com/shorts/ZuMjuFYxfMU)

### 10.3 Recognition of Seven Nepali Currency Denominations

The system is designed to recognise seven Nepali currency denominations: NPR 5, NPR 10, NPR 20, NPR 50, NPR 100, NPR 500 and NPR 1,000.

The following demonstration presents sample images of all seven denominations.

**Watch the Seven Denominations Demonstration:**

[View Seven Denominations Video](https://youtu.be/eAiTSauuFDU)

### 10.4 Image Upload and Audio-Based Recognition

In addition to webcam-based recognition, the application allows users to upload banknote images for denomination classification. Following image processing and prediction, the application provides an audio announcement of the recognised denomination in Nepali.

This feature demonstrates the potential of the system as an assistive application for visually impaired users by providing auditory feedback alongside visual predictions.

The demonstration includes two examples:

- NPR 5 banknote with a Nepali audio announcement.
- NPR 100 banknote with a Nepali audio announcement.

**Watch the Image Upload and Audio Recognition Demonstration:**

[View Image Upload and Audio Recognition Video](https://youtu.be/IxATT7Z5PPY)
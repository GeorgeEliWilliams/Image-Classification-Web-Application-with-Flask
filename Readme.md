# Image Classification Web Application With Flask

## Overview

This project is a web application built using Flask that allows users to upload images and receive predictions on the image's content. The application leverages a pre-trained ResNet50 model from Keras, which has been trained on the ImageNet dataset, to classify the uploaded images into various categories.

## Features

* User-friendly web interface for uploading images.
* Utilizes ResNet50, a state-of-the-art convolutional neural network model, for image classification.
* Provides the top prediction with a confidence percentage.
* Simple and clean code structure for easy understanding and maintenance.

## Technologies Used

* Flask: A lightweight WSGI web application framework in Python.
* Keras: A deep learning API written in Python, running on top of TensorFlow.
* ResNet50: A 50-layer deep convolutional network that has been pre-trained on the ImageNet dataset.

## Setup and Installation
### Prerequisites
Ensure you have the following installed on your local development environment:

* Python 3.7 or higher
* Pip (Python package installer)

## Installation Steps

1. Create and Activate a virtual environment
``` bash
python -m venv venv
source venv\Scripts\activate

```

2. Install the required packages
``` bash
pip install -r requirements.txt
```

3. Create the necessary directory for storing uploaded images:
``` bash
mkdir images
```

4. Run the Flask application:
``` bash
python app.py
```
6. Open your web browser and navigate to http://127.0.0.1:3000 to access the application.

## Project Structure

* app.py: The main application file containing the Flask routes and image processing logic.
* templates/index.html: The HTML template for the web interface.
* requirements.txt: A file listing the dependencies needed to run the application.
* images/: A directory where uploaded images are saved.

## Usage

* Open the web application in your browser.
* Upload an image using the provided file upload form.
* Click the submit button to receive the classification result.
* The application will display the predicted class and the confidence percentage.

## Code Explanation

### app.py
* Imports: Necessary modules from Flask and Keras.
* Model Initialization: Loads the pre-trained ResNet50 model.
* Routes:
GET /: Renders the homepage (index.html).
POST /: Handles the image upload, processes the image, and returns the prediction.
* Image Processing: Resizes, converts, reshapes, and preprocesses the image for the model.
* Prediction: Uses the model to predict the image class and decodes the prediction.

### index.html

A simple HTML template with a form for uploading images and displaying the prediction result.
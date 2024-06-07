# Import necessary modules from Flask and Keras libraries
from flask import Flask, render_template, request
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.applications.resnet50 import ResNet50

# Initialize a Flask application
app = Flask(__name__)

# Load the ResNet50 model pre-trained on ImageNet dataset
model = ResNet50()

# Define the route for the homepage, accepting GET requests
@app.route('/', methods=['GET'])
def hello_world():
    # Render and return the index.html template when accessing the homepage
    return render_template("index.html")

# Define the route for handling image upload and prediction, accepting POST requests
@app.route('/', methods=['POST'])
def predict():
    # Get the uploaded image file from the request
    imagefile = request.files['imagefile']
    
    # Define the path where the image will be saved
    image_path = "./images/" + imagefile.filename
    
    # Save the uploaded image to the specified path
    imagefile.save(image_path)

    # Load the image and resize it to the target size of 224x224 pixels
    image = load_img(image_path, target_size=(224, 224))
    
    # Convert the image to a NumPy array
    image = img_to_array(image)
    
    # Reshape the image to match the input shape expected by the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    
    # Preprocess the image for the model (e.g., scaling pixel values)
    image = preprocess_input(image)
    
    # Use the model to predict the class of the image
    yhat = model.predict(image)
    
    # Decode the prediction into a human-readable label
    label = decode_predictions(yhat)
    
    # Get the top prediction (highest probability)
    label = label[0][0]

    # Format the classification result as a string with the class name and confidence percentage
    classification = '%s (%.2f%%)' % (label[1], label[2] * 100)

    # Render and return the index.html template, passing the prediction result to it
    return render_template("index.html", prediction=classification)

# Run the Flask application on port 3000 with debug mode enabled
if __name__ == '__main__':
    app.run(port=3000, debug=True)

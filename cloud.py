from PIL import Image
import numpy as np
import joblib

model = joblib.load("svm_model.pkl")

label_map = {0: "Empty", 1: "HIGH TRAFFIC", 2: "LOW TRAFFIC", 3: "MEDIUM TRAFFIC"}

def preprocess_image(image):
    gray = image.convert('L')  # Convert to grayscale
    resized = gray.resize((100, 100))  # Resize the image
    flattened = np.array(resized).flatten()  # Flatten the image into 1D array
    return flattened

def classify_and_print_label(image_path):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Unable to read image.")
        return

    preprocessed_image = preprocess_image(image)
    preprocessed_image = preprocessed_image.reshape(1, -1)

    predicted_label = model.predict(preprocessed_image)
    predicted_class = label_map[predicted_label[0]]

    decision_scores = model.decision_function(preprocessed_image)
    confidence = np.max(np.abs(decision_scores))

    print("Predicted label:", predicted_class, "with confidence:", round(confidence, 2))

# Example usage:
image_path = "test.jpg"
classify_and_print_label(image_path)

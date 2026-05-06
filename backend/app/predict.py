import os
import pickle

from preprocess import wordopt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")
ACCURACY_PATH = os.path.join(BASE_DIR, "models", "accuracy.txt")


def load_model_files():
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

    with open(VECTORIZER_PATH, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    accuracy = "Not available"

    if os.path.exists(ACCURACY_PATH):
        with open(ACCURACY_PATH, "r") as accuracy_file:
            accuracy = accuracy_file.read()

    return model, vectorizer, accuracy


model, vectorizer, accuracy = load_model_files()


def output_label(value: int) -> str:
    return "Fake News" if value == 0 else "True News"


def predict_news(news_text: str):
    cleaned_text = wordopt(news_text)
    vectorized_text = vectorizer.transform([cleaned_text])

    prediction = model.predict(vectorized_text)[0]
    probability = model.predict_proba(vectorized_text)[0]

    confidence = max(probability)

    return {
        "prediction": output_label(prediction),
        "confidence": round(float(confidence) * 100, 2),
        "model": "Logistic Regression",
        "technique": "TF-IDF Vectorization",
        "accuracy": round(float(accuracy) * 100, 2) if accuracy != "Not available" else accuracy
    }
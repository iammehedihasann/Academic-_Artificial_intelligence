import os
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from preprocess import wordopt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FAKE_DATA_PATH = os.path.join(BASE_DIR, "data", "Fake.csv")
TRUE_DATA_PATH = os.path.join(BASE_DIR, "data", "True.csv")

MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
ACCURACY_PATH = os.path.join(MODEL_DIR, "accuracy.txt")


def train_model():
    fake_data = pd.read_csv(FAKE_DATA_PATH)
    true_data = pd.read_csv(TRUE_DATA_PATH)

    fake_data["class"] = 0
    true_data["class"] = 1

    data = pd.concat([fake_data, true_data], axis=0)

    data = data.drop(["title", "subject", "date"], axis=1)

    data = data.sample(frac=1, random_state=42).reset_index(drop=True)

    data["text"] = data["text"].apply(wordopt)

    x = data["text"]
    y = data["class"]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42
    )

    vectorizer = TfidfVectorizer()
    xv_train = vectorizer.fit_transform(x_train)
    xv_test = vectorizer.transform(x_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(xv_train, y_train)

    y_pred = model.predict(xv_test)
    accuracy = accuracy_score(y_test, y_pred)

    os.makedirs(MODEL_DIR, exist_ok=True)

    with open(MODEL_PATH, "wb") as model_file:
        pickle.dump(model, model_file)

    with open(VECTORIZER_PATH, "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    with open(ACCURACY_PATH, "w") as accuracy_file:
        accuracy_file.write(str(round(accuracy, 4)))

    print("Model trained successfully.")
    print(f"Accuracy: {round(accuracy * 100, 2)}%")


if __name__ == "__main__":
    train_model()
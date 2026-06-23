from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    # Convert text into TF-IDF features
    data = vectorizer.transform([message])

    # Predict
    prediction = model.predict(data)[0]

    # Convert prediction to text
    result = "Spam" if prediction == 1 else "Not Spam"

    return render_template(
        "index.html",
        prediction=result,
        user_message=message
    )


if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
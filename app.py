from flask import Flask, render_template, request
import joblib
import os

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

    # Transform input message
    data = vectorizer.transform([message])

    # Get spam probability
    probability = model.predict_proba(data)[0][1]

    # Spam keywords
    spam_keywords = [
        "win",
        "winner",
        "money",
        "prize",
        "free",
        "claim",
        "click",
        "offer",
        "congratulations",
        "lottery",
        "reward",
        "urgent",
        "selected",
        "cash"
    ]

    # Hybrid detection
    if probability > 0.40 or any(word in message.lower() for word in spam_keywords):
        result = "Spam"
    else:
        result = "Not Spam"

    return render_template(
        "index.html",
        prediction=result,
        user_message=message
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

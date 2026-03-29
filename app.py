from flask import Flask, request, render_template
import joblib

# Load model
model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    amount = float(request.form["amount"])
    time = float(request.form["time"])

    result = model.predict([[amount, time]])[0]

    if result == 1:
        output = "Fraud Transaction ❌"
    else:
        output = "Normal Transaction ✅"

    return render_template("index.html", prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)

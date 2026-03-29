import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "amount": [100, 50000, 200, 70000, 150],
    "time": [1, 2, 3, 4, 5],
    "fraud": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["amount", "time"]]
y = df["fraud"]

model = RandomForestClassifier()
model.fit(X, y)

# 🔥 Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully")

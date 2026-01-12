import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load dataset
df = pd.read_csv("heart_disease_uci.csv")

# 2. Drop unnecessary columns
df = df.drop(columns=["id", "dataset"])
df = df.dropna()

# 3. Encode categorical columns
categorical_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"]
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# 4. Convert target column
df["num"] = df["num"].apply(lambda x: 0 if x == 0 else 1)

# 5. Split input & output
X = df.drop("num", axis=1)
y = df["num"]

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# 9. Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 10. Save model
joblib.dump(model, "model.pkl")

print("\nModel saved as model.pkl")

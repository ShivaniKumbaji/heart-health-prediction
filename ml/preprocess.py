import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = pd.read_csv("heart_disease_uci.csv")

# 2. Drop unnecessary columns
df = df.drop(columns=["id", "dataset"])

# 3. Remove missing values
df = df.dropna()

# 4. Encode categorical columns
categorical_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"]
le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# 5. Convert target column (num → binary)
df["num"] = df["num"].apply(lambda x: 0 if x == 0 else 1)

# 6. Split input & output
X = df.drop("num", axis=1)
y = df["num"]

# 7. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("STEP 3 COMPLETED SUCCESSFULLY")
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

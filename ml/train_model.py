import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv("dataset/House_Rent_10k_major_cities.csv")
print("\nBuilding Type")
print(sorted(df["Building Type"].unique()))

print("\nFloor")
print(sorted(df["Floor"].unique()))

print("\nArea Type")
print(sorted(df["Area Type"].unique()))

print("\nFurnishing Status")
print(sorted(df["Furnishing Status"].unique()))

print("\nTenant Preferred")
print(sorted(df["Tenant Preferred"].unique()))

print("\nPoint of Contact")
print(sorted(df["Point of Contact"].unique()))

# Remove Property ID
df.drop(["Property ID", "Posted On"], axis=1, inplace=True)
# Save encoders
encoders = {}

# Encode categorical columns
for col in df.columns:
    if df[col].dtype == "object":
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

# Features and Target
X = df.drop("Rent", axis=1)
y = df["Rent"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save Model
with open("house_rent_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save Encoders
with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("Model Saved Successfully")
print("Encoders Saved Successfully")
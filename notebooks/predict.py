import joblib
import numpy as np
import pandas as pd
# Load the trained pipeline using joblib
model = joblib.load("notebooks/final_model_pipeline.pkl")

# Confirm correct type
print(f"✅ Loaded model type: {type(model)}")  # should show sklearn.pipeline.Pipeline

# Prompt the user for inputs
features = [
    "OverallQual", "GrLivArea", "GarageCars", "GarageArea",
    "TotalBsmtSF", "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt","OpenPorchSF",
    "LotFrontage","GarageYrBlt",
    "MasVnrArea", "HalfBath","LotArea",
    "YearRemodAdd", "Fireplaces", "BsmtFullBath", "WoodDeckSF" ,"BsmtUnfSF","2ndFlrSF","BsmtFinSF1",
]

user_input = []
print("Enter the following features:")
for feat in features:
    val = float(input(f"{feat}: "))
    user_input.append(val)

X_new = pd.DataFrame([user_input], columns=features) 
pred = model.predict(X_new)
print(f"\n✅ Predicted Sale Price: ${pred[0]:,.2f}")

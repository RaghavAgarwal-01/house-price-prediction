# 🏠 Ames Housing Price Prediction

Welcome to my Machine Learning project predicting house sale prices in Ames, Iowa! This project demonstrates data cleaning, exploratory data analysis, feature engineering, model building, and evaluation using regularized linear regression.

---

## 📂 Project Structure

├── data/
│ └── train.csv
├── notebooks/
│ ├── eda.ipynb
│ └── final_model_pipeline.pkl
├── README.md
└── requirements.txt

---

## 📊 Project Overview

- **Data Source**: Ames Housing dataset.
- **Goal**: Predict `SalePrice` based on various housing features.
- **Approach**:
  - Data cleaning and exploratory analysis.
  - Feature engineering (encoding, missing value handling).
  - Regularized regression using `LassoCV`.
  - Final model packaged in `final_pipeline.pkl`.

---
## 🚀 How to Predict a House Price

1 Clone the repo
2 Install dependencies:
   pip install -r requirements.txt
3 Run the prediction script:
    python predict.py
4 Enter the required values(Sample values can be found in docs/sample_input)


The final model generalizes well with minimal overfitting.

🚀 Future Improvements
    Add advanced algorithms (e.g., Random Forest, XGBoost).
    Deploy a web app for real-time price prediction.
    Apply interpretability tools like SHAP to explain feature contributions.

📄 License
    This project is open source and free for educational or personal use.

🙋‍♂️ Author
Raghav Agarwal
https://github.com/RaghavAgarwal-01/house-price-prediction.git
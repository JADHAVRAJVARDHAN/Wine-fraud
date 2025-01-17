# prompt: Write a code for test so for which i could set upit in github action ci cd

import unittest
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import xgboost as xgb

class TestWineFraudModel(unittest.TestCase):

    def setUp(self):
        # Load the dataset (replace with your actual file path)
        self.df = pd.read_csv("wine_fraud (2).csv")
        self.df["quality"] = self.df["quality"].map({"Legit": 1, "Fraud": 0})
        self.X = self.df.drop(columns=["quality", "type"])
        self.y = self.df["quality"]

    def test_data_loading(self):
        # Check if the DataFrame is not empty
        self.assertFalse(self.df.empty)
      
    def test_xgboost_model(self):
      x_train, x_test, y_train, y_test = train_test_split(self.X, self.y, train_size=0.8, random_state=42) # Added random_state for reproducibility
      # Resample data
      smote = SMOTE(random_state=42)
      X_resampled, y_resampled = smote.fit_resample(x_train, y_train)


      x_train, x_test, y_train, y_test = train_test_split(X_resampled, y_resampled, train_size=0.8, random_state=42) # Added random_state for reproducibility

      # Feature scaling
      scaler = StandardScaler()
      num_cols = x_train.select_dtypes(include=['float64', 'int64']).columns
      x_train[num_cols] = scaler.fit_transform(x_train[num_cols])
      x_test[num_cols] = scaler.transform(x_test[num_cols])
      xgb_model = xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss') # Added random_state and use_label_encoder=False
      xgb_model.fit(x_train, y_train)
      y_pred = xgb_model.predict(x_test)
      accuracy = accuracy_score(y_test, y_pred)
      self.assertGreater(accuracy, 0.7) # Example threshold, adjust as needed


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

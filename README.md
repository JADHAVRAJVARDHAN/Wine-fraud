# 🍷 Detecting Wine Fraud Using Machine Learning & MLOps

## 📌 Introduction
Counterfeit wine is a growing issue in the beverage industry, leading to major losses and trust concerns. I built a **Wine Fraud Detection** system using Machine Learning and integrated **MLOps** practices to track, scale, and containerize the solution for real-world deployment.

---

## 📊 Dataset & Preprocessing

I used a public dataset containing physicochemical properties of wine, such as:
- Alcohol content
- Citric acid levels
- pH values

**Steps:**
- Cleaned and standardise the data
- Addressed missing values
- Performed an 80/20 train-test split

---

## 🧠 Model Development

I started with **Logistic Regression** and achieved 95% accuracy. To reduce false positives and enhance robustness, I implemented:
- Gradient Boosting
- Xgboost

🔍 **Improved Accuracy**: `97.08%`  
📉 **False Positive Reduction**: `62.79%`

**Tools Used:**  
`pandas`, `numpy`, `scikit-learn`, `matplotlib`

---

## 📈 Model Tracking with MLflow

To keep track of my model experiments and metrics, I used **MLflow**:
- Logged model parameters, metrics, and versions
- Compared runs visually in the MLflow UI
- Enabled better reproducibility and experiment management

🖼️ *Example:*  
![MLflow Tracking](images/mlflow_tracking.png)

---

## 📦 Containerization with Docker

To ensure consistent deployment, I containerized the application using Docker.

dockerfile
# Sample Dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "src/fraud_detector.py"]

Easily reproducible and shareable across teams
---
## 🛆 Containerization with Docker

To ensure portability and reproducibility, I containerized the project:

Wrote a Dockerfile including all dependencies

Built and ran the image locally and tested the API endpoint

Ready to be deployed on any cloud platform or local server
---
##📉 Results

Final model results:

Accuracy: 97.08%

Precision: 96.5%

Recall: 97.9%

False Positive Reduction: 62.79%
---
Confusion matrix:

[[783,  16],
 [ 32, 795]]
---
##💡 Challenges & Learnings

Handling class imbalance was crucial—used class weights and oversampling

Model performance improved significantly after feature engineering

MLOps skills like MLflow and Docker made the solution scalable and team-friendly
---
# ✅ Conclusion

This project showed how machine learning and MLOps can help tackle fraud detection in real-world industries like wine manufacturing. By automating and scaling fraud prediction, we can help producers and consumers maintain trust and quality.

# 🍷 Detecting Wine Fraud Using Machine Learning & MLOps

## 📌 Introduction
Counterfeit wine is a growing issue in the beverage industry, leading to major losses and trust concerns. I built a **Wine Fraud Detection** system using Machine Learning and integrated **MLOps** practices to track, scale, and containerize the solution for real-world deployment.

---
## 📊 Dataset & Preprocessing

The dataset includes physicochemical properties of wine such as:

- Alcohol content
- Citric acid
- pH level
- Residual sugar

**Preprocessing Steps:**
- Standardized numerical features
- Handled missing values
- Applied 80/20 train-test split

---

## 🧠 Model Development

Initial model: **Logistic Regression**  
Advanced models: **Gradient Boosting**, **XGBoost**

### Results:
- **Accuracy:** 97.08%
- **Precision:** 96.5%
- **Recall:** 97.9%
- **False Positive Reduction:** 62.79%

**Tools Used:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`

---

## 🧪 MLflow Experiment Tracking

MLflow was used to:
- Log model parameters and metrics
- Visualize and compare different runs
- Ensure reproducibility and experiment traceability

> 📷 *MLflow UI snapshot goes here*

---

## 🐳 Docker-Based Containerization

To make the solution portable and production-ready, the entire project is containerized using Docker.

### Sample Dockerfile:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "src/fraud_detector.py"]
```
---
# 📉 Results

Final model results:

Accuracy: 97.08%

Precision: 96.5%

Recall: 97.9%

False Positive Reduction: 62.79%
---
Confusion matrix:
```
[[783,  16],
 [ 32, 795]]
```
---
# 💡 Challenges & Learnings

Handling class imbalance was crucial—used class weights and oversampling

Model performance improved significantly after feature engineering

### MLOps skills like MLflow and Docker made the solution scalable and team-friendly
---
# ✅ Conclusion

This project showed how machine learning and MLOps can help tackle fraud detection in real-world industries like wine manufacturing. By automating and scaling fraud prediction, we can help producers and consumers maintain trust and quality.

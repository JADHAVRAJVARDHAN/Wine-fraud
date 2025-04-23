# Detecting Wine Fraud Using Machine Learning & MLOps
🍷 Introduction

Counterfeit wine is a growing problem in the beverage industry, leading to revenue losses and trust issues among consumers. I wanted to see if machine learning could help identify fraudulent wines based solely on their chemical properties. In this blog, I’ll walk you through how I built a Wine Fraud Detection system using machine learning—and how I made it production-ready with MLOps tools like MLflow and Docker.

 📊 Dataset & Preprocessing

I used a public dataset of physicochemical tests of wines (like pH, alcohol content, and citric acid levels). The target variable was binary: fraudulent vs. genuine.

Steps:

Cleaned missing and noisy data

Normalized features for better model performance

Split into train-test sets (80-20)

🧠 Model Development

I started with logistic regression as a baseline model:

Achieved 95% accuracy

High recall, but false positives were a concern

To improve this, I used ensemble models (like Random Forest and Gradient Boosting), which improved accuracy to 97% and reduced false positives by 62.79%.

Tools used:
scikit-learn, pandas, matplotlib

🔍 Model Tracking with MLflow

To track model experiments, metrics, and parameters, I used MLflow:

Logged each model version with performance metrics

Compared models in the MLflow UI

Easily reproducible and shareable across teams

🛆 Containerization with Docker

To ensure portability and reproducibility, I containerized the project:

Wrote a Dockerfile including all dependencies

Built and ran the image locally and tested the API endpoint

Ready to be deployed on any cloud platform or local server

📉 Results

Final model results:

Accuracy: 97.08%

Precision: 96.5%

Recall: 97.9%

False Positive Reduction: 62.79%

Confusion matrix:

[[783,  16],
 [ 32, 795]]

💡 Challenges & Learnings

Handling class imbalance was crucial—used class weights and oversampling

Model performance improved significantly after feature engineering

MLOps skills like MLflow and Docker made the solution scalable and team-friendly

✅ Conclusion

This project showed how machine learning and MLOps can help tackle fraud detection in real-world industries like wine manufacturing. By automating and scaling fraud prediction, we can help producers and consumers maintain trust and quality.

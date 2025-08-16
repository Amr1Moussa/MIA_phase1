## Project Overview

This project addresses the **Formula 1 Calories Burnt Prediction** challenge, where the goal is to predict the number of calories burned by F1 drivers during simulated training sessions. Accurate calorie prediction helps optimize diet plans and maintain peak driver performance.

## Dataset

* The dataset contains biometric readings and workout data (heart rate, speed, duration, weight, height, etc.) for multiple training sessions.
* The target variable is **Calories** burned during each session.
* `train.csv` was used for training, and predictions were generated on the unseen `test.csv`.

## Approach

### Data Preprocessing

* Removed irrelevant columns such as `id`.
* Checked for missing values and duplicates; none were found after cleaning.
* Performed outlier analysis but did not remove outliers, as boosting models used are robust to them.
* Conducted multicollinearity and feature distribution checks; no extreme skewness was observed.
* Engineered additional features that capture physiological and interaction effects (e.g., Workload, BMI, Cardio Load, etc.).
* Experimented with feature scaling but found better generalization without it.

### Models Implemented

* **LightGBM Regressor**: Tuned with 2000 estimators, learning rate 0.05, 128 leaves, and subsampling.
* **XGBoost Regressor (v3.0.3)**: Tuned with similar parameters, max depth 8, using histogram tree method for speed.
* Models were trained independently in separate notebooks/files.

### Ensemble

* Predictions from LightGBM and XGBoost models were averaged to create an ensemble.
* The ensemble achieved the best validation RMSE compared to individual models.

## Results

* **LightGBM Validation RMSE:** \~3.6516
* **XGBoost Validation RMSE:** \~3.6518
* **Ensemble Validation RMSE:** \~3.6328 (best performance)
* Achieved **3rd place on the leaderboard** with polynomial feature degree 3.
* Higher polynomial degrees (degree 5) reduced test loss further (\~0.121), potentially improving rank to 1st, but this was after the competition deadline.

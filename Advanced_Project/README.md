# EV Battery Health Prediction using Advanced Machine Learning Models

## Description

This project focuses on predicting the health of electric vehicle (EV) batteries using advanced machine learning techniques. Battery degradation significantly impacts the performance and lifespan of EVs. The objective of this project is to analyze battery parameters such as ambient temperature and internal resistance, and predict battery capacity (State of Health - SOH) using multiple machine learning models.

## Dataset

* **Source:** NASA Battery Dataset / Kaggle
* **Description:** The dataset includes battery parameters such as ambient temperature, internal resistance values (Re, Rct), and battery capacity. These features are used to analyze battery degradation and performance.

## Steps Performed

### 1. Data Preprocessing

* Removed missing values
* Selected relevant numeric features
* Eliminated unnecessary columns such as IDs and filenames

### 2. Exploratory Data Analysis (EDA)

* Analyzed dataset using descriptive statistics (mean, median, standard deviation, etc.)
* Studied data distribution and variability

### 3. Data Visualization

* Histogram for distribution analysis
* Bar charts for feature comparison
* Box plots to detect outliers
* Line graphs for trend analysis
* Scatter plots to study relationships
* Correlation heatmap to identify important features

### 4. Model Building

Applied multiple machine learning models:

* Linear Regression (baseline model)
* Random Forest Regressor (ensemble model)
* Decision Tree Regressor

### 5. Model Evaluation

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### 6. Model Comparison

* Compared performance of all models
* Random Forest performed better due to its ability to capture complex relationships and reduce overfitting

## Results

* Identified key factors affecting battery degradation
* Found that internal resistance (Rct) has a strong negative impact on battery capacity
* Random Forest provided the most accurate predictions among all models

## Tools Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## Conclusion

This project demonstrates that advanced machine learning models can effectively predict battery health. The comparison of multiple models shows that ensemble methods like Random Forest outperform simpler models. This approach can be applied in real-world battery management systems to improve efficiency, reduce maintenance costs, and extend battery lifespan.

## Author

Vasanth Reddy

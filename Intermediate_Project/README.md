# EV Battery Health Prediction using Machine Learning

## Description

This project aims to predict the State of Health (SOH) of electric vehicle (EV) batteries using machine learning techniques. Battery health is a critical factor that affects the performance, efficiency, and lifespan of EVs. By analyzing battery parameters such as voltage, current, temperature, and charge cycles, this project identifies patterns in battery degradation and builds a predictive model.

## Dataset

* **Source:** NASA Battery Dataset / Kaggle EV datasets
* **Description:** The dataset contains battery-related features such as voltage, current, temperature, cycle count, capacity, internal resistance, and charging time. These variables are used to analyze battery behavior and predict its health.

## Steps Performed

### 1. Data Cleaning

* Checked for missing values and handled them appropriately
* Removed duplicate records
* Converted data into suitable formats
* Normalised/standardised features if required

### 2. Exploratory Data Analysis (EDA)

* Analyzed dataset structure using `.info()` and `.describe()`
* Studied relationships between variables
* Identified trends in battery degradation

### 3. Visualization

* Plotted histograms to understand data distribution
* Used scatter plots to analyze relationships (e.g., cycle count vs capacity)
* Created correlation heatmaps to identify important features
* Used box plots to detect outliers

### 4. Model Building

* Applied regression techniques (e.g., Linear Regression)
* Split data into training and testing sets
* Trained the model using battery features
* Evaluated performance using metrics such as MAE, MSE, and RMSE

## Results

* Successfully identified key factors affecting battery degradation
* Built a regression model to predict battery health (SOH)
* Observed that features like cycle count, temperature, and voltage significantly influence battery performance

## Tools Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## Conclusion

This project demonstrates that machine learning can effectively predict battery health using historical data. The model helps in understanding degradation patterns and can be used in real-world battery management systems to improve performance, reduce maintenance costs, and enhance battery lifespan.

## Author

Vasanth Reddy

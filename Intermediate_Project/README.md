# EV Battery Health Prediction using Machine Learning

# Description

This project focuses on predicting the health of electric vehicle (EV) batteries using machine learning techniques. The objective is to analyze key battery parameters such as ambient temperature, internal resistance (Re, Rct), and other features to estimate battery capacity, which represents the battery’s State of Health (SOH).

## Dataset

* **Source:** NASA Battery Dataset / Kaggle
* **Description:** The dataset contains battery-related parameters such as ambient temperature, resistance values (Re, Rct), and battery capacity. These features help in understanding battery degradation and performance.

## Steps Performed

### 1. Data Cleaning

* Removed missing values
* Selected relevant numeric features
* Eliminated unnecessary columns such as IDs and filenames

### 2. Exploratory Data Analysis (EDA)

* Analyzed dataset structure using `.info()` and `.describe()`
* Identified relationships between variables

### 3. Data Visualization

* Used histograms to study data distribution
* Created correlation heatmap to identify relationships
* Plotted scatter plots to analyze feature vs capacity relationships

### 4. Model Building

* Applied **Linear Regression** to predict battery capacity
* Selected key features: ambient_temperature, Re, Rct
* Split data into training and testing sets

## Results

* The model successfully predicted battery capacity using regression
* Observed that **Rct has a strong negative correlation with battery capacity**, indicating battery degradation
* Model performance evaluated using:

  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
  * R² Score

## Tools Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## Conclusion

This project demonstrates that machine learning techniques can effectively predict battery health using key parameters. The analysis shows that internal resistance plays a major role in battery degradation. This approach can be useful in real-world battery management systems to improve performance and lifespan.

## Author

Vasanth Reddy

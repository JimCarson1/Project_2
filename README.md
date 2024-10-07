# Exploring the Power of Weather Data

## Project Overview

This project leverages machine learning to predict crop yields and flu outbreaks based on weather data. Initially, we aimed to predict crop yields across various U.S. states using weather data from OpenWeatherMap, combined with crop data from the USDA National Agricultural Statistics Service (NASS). While weather data provided some insight, we discovered it was insufficient for accurate crop yield predictions on its own. Toward the end of the project, we pivoted to predict flu outbreaks using the same weather data, yielding much more promising results.

## Project Goals

- Predict crop yields for different U.S. states using weather data.
- Explore the relationship between weather data and flu outbreaks.
- Identify gaps in data and future opportunities for improving prediction models.

## Presentation

For a more visual overview of the project, you can view the full presentation here:
[Project Presentation](https://docs.google.com/presentation/d/13wvr7N_o4edtvKolaLUzSwJBnX1uzUopYICoYWqXYNo/edit#slide=id.g308a25c9d1f_0_63)

## Data Sources

1. **Crop Data**:

   - Source: [USDA NASS](https://www.nass.usda.gov/datasets/)
   - Description: 22 million rows of crop yield data from U.S. states, including information on crop type, location, and yield.

2. **Weather Data**:

   - Source: [OpenWeatherMap](https://openweathermap.org/)
   - Description: Weather data collected using the OpenWeather API from 1980 to 2024. Includes temperature, precipitation, and more, averaged quarterly for each state.

3. **Flu Data**:
   - Source: [Agency for Toxic Substances and Disease Registry (ATSDR)](https://www.atsdr.cdc.gov/)
   - Description: State-level flu case data from 2010-2020.

## Workflow

### 1. **Crop Data Collection and Cleaning**

- Downloaded crop data from USDA NASS, which contained millions of rows with diverse units.
- Generalized data to a state-level by cleaning location entries and converting zip codes to state names.
- Normalized the "value" column to represent crop yield, ensuring consistency across units and crop types.

### 2. **Weather Data Collection**

- Used OpenWeatherMap API to collect weather data from 1980-2024, focusing on one to two coordinates per state (52 total coordinates).
- Compromised by collecting 24 days of data per year to represent seasonal weather, balancing accuracy and API cost limits.

### 3. **Data Preparation and Merging**

- Grouped weather data by quarter (Q1, Q2, Q3, Q4) and averaged the values for each state.
- Merged weather data with crop data on a state and yearly basis, creating a dataset for machine learning models.

### 4. **Model Training**

- Trained several models, including Linear Regression and XGBoost, to predict crop yields based solely on weather data.
- **Best result:** 22% accuracy using the XGBoost model.
- Conclusion: Weather data alone isn't sufficient for accurate crop yield prediction. Additional data such as soil quality and economic factors are necessary.

### 5. **Pivot to Flu Prediction**

- Merged flu case data with weather data, averaged by quarter.
- Trained a model to predict flu cases based on weather, state, and population density.
- Achieved **60% accuracy** using XGBoost.

## Key Learnings

- **Data Quality**: The majority of time was spent on data collection, cleaning, and merging, which is crucial for real-world projects.
- **Weather's Limitations**: Weather data is only a piece of the puzzle for predicting crop yields. Additional factors such as soil, economics, and resources need to be considered.
- **Exploring Flu Prediction**: Weather data had a much stronger correlation with flu outbreaks than crop yields, demonstrating its predictive power in other areas.

## Future Directions

1. **Incorporating More Data**: Adding soil quality, pest data, economic data, and resource allocation could significantly improve the crop yield predictions.
2. **Granular Analysis**: Moving from state-level analysis to county-level would provide more precise and granular predictions.
3. **Expanding Weather Predictions**: Use the weather data to predict other outcomes such as wildfires, energy consumption, air quality, and natural disasters.

## Installation

1. Ensure you have Python **3.11.5** installed.

   - You can download it from [python.org](https://www.python.org/downloads/release/python-3115/).

2. Clone the repository:

   ```bash
   git clone https://github.com/JimCarson1/Project_2.git

   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Technologies Used

- **Python**: Data cleaning, preprocessing, and model training (Pandas, NumPy, Scikit-learn, XGBoost).
- **OpenWeatherMap API**: Weather data collection.
- **USDA NASS Data**: Crop yield data.
- **Matplotlib/Seaborn**: Data visualization.
- **Git/GitHub**: Version control.

## Contributors

- **Mason Galusha**: Project Lead, Data Collection, Model Training
- **Marquez Ward**: Data Cleaning, Feature Engineering
- **Jim Carson**: API Integration, Weather Data Management
- **Graham Adams**: Flu Data Analysis, Model Optimization

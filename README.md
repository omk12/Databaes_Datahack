# Databaes_Datahack
Project Overview
This project is developed for the FlightQuest Hackathon, focusing on enhancing aviation operations through flight delay prediction. The goal of this project is to build a machine learning model that predicts the delay time of flights based on various factors such as weather conditions, visibility, and other aviation-related data.

Problem Statement
The goal of this hackathon is to develop a robust machine learning model capable of predicting flight delays. Accurate prediction of flight delays will allow airports and airlines to optimize scheduling, improve customer satisfaction, and streamline operations.

Dataset
The dataset consists of multiple features that impact flight delays, such as:

Flight Information: Departure and arrival airports, scheduled times, flight IDs.
Weather Information: Visibility, wind speed, temperature, humidity, etc.
Runway Conditions: Current operational status of runways and weather conditions affecting them.
Important Columns:
departure_airport_code: IATA code for the departure airport.
arrival_airport_code: IATA code for the arrival airport.
scheduled_departure_time: Scheduled time of departure.
scheduled_arrival_time: Scheduled time of arrival.
visibility: Visibility at the time of departure.
delay_time: The actual delay (in minutes) for each flight.
present_condition: Weather condition at the time of flight (True/False).
Approach
The overall approach to solving the problem includes the following steps:

1. Data Preprocessing:
Handling Missing Values: Imputation of missing data where applicable.
Converting Weather Data: Transforming boolean values in visibility to numerical values (1 = good visibility, 0 = bad visibility).
Feature Engineering: Creating new features from the available data to enhance the predictive power of the model.
Dropping Unnecessary Columns: Columns like id_x and id_y were dropped for better clarity.
2. Exploratory Data Analysis (EDA):
Understanding correlations between features and flight delays.
Visualizing the data using histograms, scatter plots, and heatmaps to gain insights.
3. Model Selection:
Regression Models were selected since the task is to predict a continuous variable (delay in minutes).
Support Vector Regression (SVR) was chosen as it handles non-linear relationships and works well with a smaller dataset.
Other models considered:
Linear Regression: For baseline comparisons.
Random Forest Regressor: For capturing non-linear relationships between features.
4. Model Evaluation:
Mean Squared Error (MSE) and R-Squared (R²) were used to evaluate model performance.
Cross-validation techniques were applied to ensure the model generalizes well on unseen data.

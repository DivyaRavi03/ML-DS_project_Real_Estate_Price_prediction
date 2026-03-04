# ML-DS_project_Real_Estate_Price_prediction
A machine learning web application that predicts house prices in Bangalore based on location, square footage, number of bedrooms (BHK), and bathrooms as features. The project includes a complete end-to-end ML pipeline from data cleaning to deployment with a user-friendly web interface. This project is done by me from scratch, with the help of and replicate of [Codebasics](https://youtu.be/rdfbcdP75KI) 
# Overview
This project implements a machine learning solution to predict real estate prices in Bangalore. It uses Linear Regression with feature engineering and outlier detection to provide accurate price estimates based on property characteristics. The application features a Flask backend API and an interactive frontend interface.

# Tech Stack
## Machine Learning and Data Preprocessing:
- Python 3.8+
- Pandas (Data manipulation)
- NumPy (Numerical computing)
- scikit-learn (Machine learning model)
- Matplotlib (Data visualization)
## Backend:
Flask - Web framework
pickle - Model serialization
## Frontend:
- HTML5/CSS3
- JavaScript
- jQuery - AJAX requests
  
# Workflow
## Step 1: Downloading Dataset
Downloaded [Banglore House Price Dataset](https://www.kaggle.com/datasets/sanjay3454chauhan/bangluru-house-dataset) from kaggle. Import needed libraries for working with dataset.

## Step 2: Data Cleaning
- Read the data using Pandas.
- Removed the colmuns or fetaures that didnt contribute to final target columns.
- Checked if there are any missing values, since there was fewer missing values and larger amount of datasets, removed those rows from dataset.
- Some errors in the dataset where rectified according to their respective correct steps.

## Step 3: Feature Engineering
- Introduced new column 'price_per_sqft' which is imporatnt for price prediction with respect to locations.
- There were 1304 different locations in dataset, reduced that to 242 columns by mentioning that locations that has less than 10 datapoints as 'other'. Which lead us out of "dimensionality curse"

## Step 4: Backend logic for web application
- server.py: added different endpoints and its logic to collect the data from clients or frontend to predict accordingy to features.
- util.py: load all the saved artifacts in the backend and create separate variables to work along those data.

## Step 5: Frontend
- app.html - contains structure of our website, that also get input from clients to predict.
- app.css - gives attractive visuals to website.
- app.js - makes our website to be dynamic.

Attached UI of website, and Prediction result of website.






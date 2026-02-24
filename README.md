# ML-DS_project_Real_Estate_Price_prediction

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

import pandas as pd
from sklearn.model_selection import train_test_split


# Load the CSV file
file_path = 'twitter_parsed_dataset.csv'  # Replace with your file path
data1 = pd.read_csv(file_path)

# Display the first few rows of the dataframe to inspect the data
print("twitter_parsed_dataset")

# Display the columns of the dataframe
print(len(data1))
print(data1['oh_label'].value_counts())

file_path = 'twitter_test_sample.csv'  # Replace with your file path
data1 = pd.read_csv(file_path)

# Display the first few rows of the dataframe to inspect the data
print("twitter_test_sample")

# Display the columns of the dataframe
print(len(data1))
print(data1['oh_label'].value_counts())


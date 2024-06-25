import pandas as pd
from sklearn.model_selection import train_test_split


# Load the CSV file
file_path = 'twitter_parsed_dataset.csv'  # Replace with your file path
data1 = pd.read_csv(file_path)

# Display the first few rows of the dataframe to inspect the data
print(data1.head())

# Display the columns of the dataframe
print(data1['oh_label'].value_counts())

data = data1.dropna()[['Text','Annotation','oh_label']]
# Define the field to stratify on
stratify_field = 'oh_label'  # Replace with your column name

# Get a stratified random sample
# Adjust the test_size parameter to get the desired sample size
sample_size = 0.02  # 10% of the data
train, stratified_sample = train_test_split(data, test_size=sample_size, stratify=data[stratify_field])

# Display the stratified random sample
print(len(stratified_sample))
print(stratified_sample[stratify_field].value_counts())
# Save the stratified random sample to a CSV file
output_file_path = 'twitter_test_sample.csv'  # Replace with your desired output file path
stratified_sample.to_csv(output_file_path, index=False)

train1, val = train_test_split(train, test_size=0.01, stratify=train[stratify_field])

    #
# Display the stratified random sample
print(len(val))
print(val[stratify_field].value_counts())
# Save the stratified random sample to a CSV file
output_file_path = 'twitter_examples_prompts.csv'  # Replace with your desired output file path
val.to_csv(output_file_path, index=False)
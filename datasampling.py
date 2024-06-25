import pandas as pd
from sklearn.model_selection import train_test_split


# Load the CSV file
file_path = 'cyberbullying_tweets.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to inspect the data
print(data.head())

# Display the columns of the dataframe
print(data['cyberbullying_type'].value_counts())


random_sample = data.sample(n=300)

print(random_sample['cyberbullying_type'].value_counts())

# Define the field to stratify on
stratify_field = 'cyberbullying_type'  # Replace with your column name

# Get a stratified random sample
# Adjust the test_size parameter to get the desired sample size
sample_size = 0.01  # 10% of the data
train, stratified_sample = train_test_split(data, test_size=sample_size, stratify=data[stratify_field])


# Display the stratified random sample
print(len(stratified_sample))
print(stratified_sample['cyberbullying_type'].value_counts())
# Save the stratified random sample to a CSV file
output_file_path = 'stratified_test_sample_final.csv'  # Replace with your desired output file path
stratified_sample.to_csv(output_file_path, index=False)

train1, val = train_test_split(train, test_size=sample_size, stratify=train[stratify_field])

    #
# Display the stratified random sample
print(len(val))
print(val['cyberbullying_type'].value_counts())
# Save the stratified random sample to a CSV file
output_file_path = 'stratified_val_sample_final.csv'  # Replace with your desired output file path
val.to_csv(output_file_path, index=False)

import pandas as pd

# Load the CSV files
file1_path = 'twitter_parsed_dataset.csv'
file2_path = 'twitter_test_sample.csv'

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Exclude rows from df1 that are present in df2 based on the 'Text' column
filtered_df = df1[~df1['Text'].isin(df2['Text'])]

print(filtered_df.head())
# Save the filtered DataFrame to a new CSV file
filtered_file_path = 'twitter_parsed_dataset_train.csv'
filtered_df[['Text','oh_label']].to_csv(filtered_file_path, index=False)


import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path ="stratified_val_sample_final.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Replace 'your_column' with the name of the column you want to apply the function to
selected_column = 'tweet_text'

# Define your function
def my_function(value):
    # Replace this with your actual function logic
    return value + "modified"

# Apply the function to the selected column
df['output'] = df[selected_column].apply(my_function)

# Print the first few rows of the modified column to verify the result
print(df.head())
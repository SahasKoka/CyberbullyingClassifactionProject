# Convert JSON to CSV
# Parse the JSON response
import csv
import json
file_path = 'SK-GPT4-vermont_bill_202406191945.json'
output_csv = 'SK-GPT4-vermont_bill_202406191945.csv'

with open(file_path, 'r') as file:
    response_data = json.load(file)


# Extract the data from the JSON response
data = []
for source_type in ["AnonymousSources", "NamedSources"]:
    for source in response_data.get(source_type, []):
        name = source.get("Name", "")
        title = source.get("Title", "")
        association = source.get("Association", "")
        sourced_statements = source.get("SourcedStatement", [])  # Ensure this matches the key in your JSON

        # Check if sourced_statements is a list or a single item
        if isinstance(sourced_statements, list):
            # If sourced_statements is a list, add each statement as a separate row
            for sourced_statement in sourced_statements:
                data.append([source_type, name, title, association, sourced_statement])
        else:
            # If sourced_statements is a single item, add it as a single row
            data.append([source_type, name, title, association, sourced_statements])

# Write the data to a CSV file
with open(output_csv, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Source Type", "Name", "Title", "Association", "Sourced Statement"])
    writer.writerows(data)

print(f"CSV file generated: {output_csv}")
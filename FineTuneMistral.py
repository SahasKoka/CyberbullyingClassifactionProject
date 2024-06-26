import requests
import json
import pandas as pd
from time import sleep

# Define the deployment endpoint and API token
deployment_id = "token key"
api_auth_token = "token key"
url = f"https://{deployment_id}.monsterapi.ai/generate"

# Read the article text from the file
file_path = "twitter_test_sample.csv"
df = pd.read_csv(file_path)
selected_column = df['Text']


# Define the prompt and payload
def call_llm(value):
    payload = {
        "prompt": f"### Tweet: {value}\n### Cyberbullying: ",
        "max_tokens": 10,
        "n": 1,
        "best_of": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "repetition_penalty": 1,
        "temperature": 1,
        "top_p": 1,
        "top_k": -1,
        "min_p": 0,
        "use_beam_search": False,
        "length_penalty": 1,
        "early_stopping": False
    }

    # Set headers with the API token
    headers = {
        "Authorization": f"Bearer {api_auth_token}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, json=payload, headers=headers, verify=False)

    # Check the response
    sleep(0.05)

    if response.status_code == 200:
        try:
            data = json.loads(response.json())
            print(data)  # Debugging statement
            act_res = data.get("text")
            return act_res

        except json.JSONDecodeError:
            print("Failed to decode JSON response:", response.text)
            return 'error'
    else:
        print("API request failed with status code:", response.status_code)
        print("Response content:", response.text)
        return 'error'


df['output'] = df['Text'].apply(call_llm)

output_file_path = "finetune_mistral7B_prompt_final.csv"
df.to_csv(output_file_path, index=False)
print(f"Output saved to {output_file_path}")

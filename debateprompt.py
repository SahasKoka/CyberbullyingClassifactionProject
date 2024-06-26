import requests
import json
import pandas as pd
from time import sleep
import re

# Read the article text from the file
file_path = "twitter_test_sample.csv"
#file_path = "argument_debate_mistral7B_prompt_pro.csv"
df = pd.read_csv(file_path)
selected_column = df['Text']

def call_llm_pro_argument(value):
    # Construct the chat prompt for pro argument
    chat_prompt = [
        {
            "role": "system",
            "content": (
                "You are an AI model that classifies tweets to determine if they contain cyberbullying content. "
                "Cyberbullying includes any form of harassment, insults, threats, or harmful behavior directed at an individual. "
                "Please provide a 3-sentence argument supporting why the following tweet is considered cyberbullying."
            )
        },
        {
            "role": "user",
            "content": (
                "Analyze the following tweet: " + value
            )
        }
    ]

    # Send the request
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "token key",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": chat_prompt,
            "temperature": 0,
            "max_tokens": 4096
        })
    )

    sleep(0.05)
    # Check the response
    if response.status_code == 200:
        data = response.json()
        act_res = data['choices'][0]['message']['content']
        return act_res.strip()
    else:
        print(response.json())
        return 'error'

def call_llm_con_argument(value):
    # Construct the chat prompt for con argument
    chat_prompt = [
        {
            "role": "system",
            "content": (
                "You are an AI model that classifies tweets to determine if they contain cyberbullying content. "
                "Cyberbullying includes any form of harassment, insults, threats, or harmful behavior directed at an individual. "
                "Please provide a 3-sentence argument supporting why the following tweet is not considered cyberbullying."
            )
        },
        {
            "role": "user",
            "content": (
                "Analyze the following tweet: " + value
            )
        }
    ]

    # Send the request
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": chat_prompt,
            "temperature": 0,
            "max_tokens": 4096
        })
    )

    sleep(0.05)
    # Check the response
    if response.status_code == 200:
        data = response.json()
        act_res = data['choices'][0]['message']['content']
        return act_res.strip()
    else:
        print(response)
        return 'error'

def call_llm_final_classification(tweet, pro_argument, con_argument):
    # Construct the chat prompt for final classification
    chat_prompt = [
        {
            "role": "system",
            "content": (
                "You are an AI model that classifies tweets to determine if they contain cyberbullying content. "
                "Cyberbullying includes any form of harassment, insults, threats, or harmful behavior directed at an individual. "
                "Given the following tweet and two arguments, please classify the tweet as either 0 for non-cyberbullying or 1 for cyberbullying."
            )
        },
        {
            "role": "user",
            "content": (
                "Tweet: " + tweet + "\n\n"
                "Pro argument: " + pro_argument + "\n\n"
                "Con argument: " + con_argument + "\n\n"
                "Based on these, classify the tweet as either 0 for non-cyberbullying or 1 for cyberbullying."
            )
        }
    ]

    # Send the request
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": chat_prompt,
            "temperature": 0,
            "max_tokens": 4096
        })
    )

    sleep(0.05)
    # Check the response
    if response.status_code == 200:
        data = response.json()
        act_res = data['choices'][0]['message']['content']
        classification = re.search(r'\b[01]\b', act_res)
        return classification.group(0) if classification else 'error'
    else:
        print(response.json())
        return 'error'

# Apply the functions to the selected column
df['pro-argument'] = df['Text'].apply(call_llm_pro_argument)
output_file_path = 'argument_debate_llama38B_prompt_pro.csv'
df.to_csv(output_file_path, index=False)

df['con-argument'] = df['Text'].apply(call_llm_con_argument)
output_file_path = 'argument_debate_llama38B_prompt_con.csv'
df.to_csv(output_file_path, index=False)

df['output'] = df.apply(lambda row: call_llm_final_classification(row['Text'], row['pro-argument'], row['con-argument']), axis=1)

# Save the results to a new CSV file
output_file_path = 'debate_llama38B_prompt.csv'
df.to_csv(output_file_path, index=False)

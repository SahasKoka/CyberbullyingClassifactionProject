import requests
import json
import datetime
import re
import os
import pandas as pd
from time import sleep



# Read the article text from the file
file_path = "twitter_test_sample.csv"
df = pd.read_csv(file_path)
selected_column = df['Text']

def call_llm(value):
    # Construct the chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": (
     "You are an AI model that classifies tweets to determine if they contain cyberbullying content. Cyberbullying includes any form of harassment, insults, threats, or harmful behavior directed at an individual. If the tweet contains cyberbullying, classify it with a value of 1. If it does not, classify it with a value of 0. "
            )
        },
        {
            "role": "user",
            "content": (
    "Please classify the following tweet as either 0 for non-cyberbullying or 1 for cyberbullying. Only output 0 or 1" + value
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
            "model": "google/gemma-7b-it",
            "messages": chat_prompt,
            "temperature": 0,
            "max_tokens": 4096
        })
    )

    sleep(0.05)
    # Check the response
    if response.status_code == 200:
        data = response.json()
        #print(data)
        act_res = data['choices'][0]['message']['content']
        return act_res
    else:
        print(response)
        return 'error'


    # Apply the function to the selected column
df['output'] = df['Text'].apply(call_llm)

df.to_csv("zero_gemma7B_prompt.csv", index=False)

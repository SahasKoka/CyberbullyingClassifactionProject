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
     "You are an AI model that classifies tweets to determine if they contain cyberbullying content.\n\nCyberbullying includes any form of harassment, insults, threats, or harmful behavior directed at an individual.\n\nIf the tweet contains cyberbullying, classify it with a value of 1. If it does not, classify it with a value of 0.\n\nHere are some examples:\n\nTweet: \"@halalflaws @biebervalue @greenlinerzjm I read them in context.No change in meaning. The history of Islamic slavery. https://t.co/xWJzpSodGj\"\nClassification: 0\nReasoning: The tweet is not cyberbullying because it appears to be a statement about reading and interpreting historical content in context, without any direct personal attacks, harassment, or intent to harm specific individuals.\n\nTweet: \"RT @Mooseoftorment Call me sexist, but when I go to an auto place, I'd rather talk to a guy\"\nClassification: 1\nReasoning: This tweet is cyberbullying because it perpetuates harmful gender stereotypes and can demean and marginalize women working in the automotive industry, contributing to a hostile online environment.\n\nTweet: \"@chilblane yay. i went last year and had to make new friends. i hate making new friends. i didn't know anyone else going.\"\nClassification: 1\nReasoning: This tweet is not cyberbullying because it expresses a personal sentiment about the difficulty of making new friends without targeting, harassing, or insulting any specific individual or group.\n\nTweet: \"@SirajZarook @OdiniaInvictus @BilalIGhumman @IsraeliRegime A good Muslim is good despite his bad religion, not because of it.\"\nClassification: 1\nReasoning: This tweet is cyberbullying because it disparages an entire religion and its followers, promoting intolerance and potentially inciting harassment against individuals based on their religious beliefs."

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
            "Authorization": "token key",
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
        print(response.json())
        return 'error'


    # Apply the function to the selected column
df['output'] = df['Text'].apply(call_llm)




df.to_csv("chain_gemma_prompt.csv", index=False)

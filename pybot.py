# creating a chat bot with openai gpt-3
#
import openai
import os
import json
import random
import time
import datetime
import requests
openai.api_key = os.getenv("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")
prompt = "Hellp my name is pybot. I am a chatbot. I am here to help you. What is your name?"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n", " Human:", " AI:"]
)
print(response)
print(response["choices"][0]["text"])
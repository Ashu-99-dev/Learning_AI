import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt1 = "Hi!"
prompt2 = "Explain time travel in Detail"
prompt3 = "Writing an easy how tokenization work in AI"
prompts = [prompt1,prompt2,prompt3]
# message me role and content
for prompt in prompts:
    message={
    "role": role,
    "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens = 500)
    print("#######################################")
    answer=response.choices[0].message.content
    usage = response.usage
    print(f"Prompt: {prompt} --> Your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
    # print(answer)
# SYSTEM
# message_system={
#     "role": "system",
#     "content": "You are a brand manager who suggests name for my company. name should be in one word."
# }


# Temperature by default is 0 meaning safe. range is [0,2]
# print(response)


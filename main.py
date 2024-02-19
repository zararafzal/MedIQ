import os
from django.shortcuts import render
from django.http import HttpResponse
from openai import OpenAI
from dotenv import load_dotenv

#updated

# Load environment variables from .env file
load_dotenv()
key = os.environ.get('API_KEY')

client = OpenAI(api_key=key)
assistant = client.beta.assistants.retrieve(assistant_id='asst_8KT5kxnZESkrPkZQNL1HyXmO')

thread = client.beta.threads.create()

messages = client.beta.threads.messages.create(
    thread_id= thread.id,
    role = "user",
    content = "what are the key indicators of a cbc report?",
)

run = client.beta.threads.runs.create(
    thread_id= thread.id,
    assistant_id= assistant.id
)

while True: 
    run = client.beta.threads.runs.retrieve(
        thread_id= thread.id,
        run_id= run.id
    )

    if run.status == 'completed':
        break
    else: 
        pass

print(run.status)
messages = client.beta.threads.messages.list(
    thread_id= thread.id
)


for x in reversed(messages.data):
    print(x.role + ':' + x.content[0].text.value)



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
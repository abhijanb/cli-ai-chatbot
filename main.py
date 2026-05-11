from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))
contents = [
    {"role": "user", "parts": [{"text": "Return response in JSON format with keys: answer"}]}
]
# model = client.models.list()
# print(model)
# for i in model:
#     print(f"${i} \n")
while True:
    question=input("what you want to know ")
    contents.append({"role": "user", "parts": [{"text": question}]})
    if question.lower() == "exit":
        break
    response = client.models.generate_content(model="gemini-2.5-flash",contents=contents)
    contents.append({"role": "model", "parts": [{"text": response.text}]})
    print(response.text)
    
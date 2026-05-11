from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))
# model = client.models.list()
# print(model)
# for i in model:
#     print(f"${i} \n")
while True:
    added_part = "Return response in JSON format with keys: answer"
    question=input("what you want to know ")
    if question.lower() == "exit":
        break
    response = client.models.generate_content(model="gemini-2.5-flash",contents=question + added_part)
    print(response.text)
    
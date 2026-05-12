from google import genai
from google.genai import types
from google.genai.errors import ClientError

from dotenv import load_dotenv

import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)

system = """
You are a chatbot with memory.

Return ONLY in this format:

ANSWER:
<assistant answer>

@#$

SUMMARY:
<short updated summary>

Rules:
- Keep summary short
- Keep important context only
- Avoid unnecessary details
"""

summary = ""

MAX_SUMMARY_LENGTH = 500

while True:

    question = input("What do you want to know: ")

    if question.lower() == "exit":
        break

    contents = f"""
Previous Summary:
{summary}

User Question:
{question}
"""

    try:

        response = client.models.generate_content(
            model="gemma-4-26b-a4b-it",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system
            )
        )

        text = response.text

        # validate separator
        if "@#$" not in text:
            print("Invalid response format from model")
            continue

        answer, new_summary = text.split("@#$", 1)

        print("\nAI Response:\n")
        print(answer.strip())

        cleaned_summary = (
            new_summary
            .replace("SUMMARY:", "")
            .strip()
        )

        # limit summary size
        if len(cleaned_summary) > MAX_SUMMARY_LENGTH:
            cleaned_summary = cleaned_summary[:MAX_SUMMARY_LENGTH]

        summary = cleaned_summary

        print("\nUpdated Memory:\n")
        print(summary)

    except ClientError as e:

        if "429" in str(e):

            print("\nRate limit exceeded.")
            print("Waiting 60 seconds...\n")

            time.sleep(60)

        else:

            print("\nAPI Error:")
            print(e)
    except KeyboardInterrupt:

        print("\nProgram stopped by user.")
        break

    except Exception as e:

        print("\nUnexpected Error:")
        print(e)
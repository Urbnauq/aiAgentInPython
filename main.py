import os
import sys
from prompts import system_prompt
from functions.get_files_info import available_functions

from dotenv import load_dotenv

from google import genai
from google.genai import types

def main():
    # Flags
    flags = {
         "verbose":"verbose",
    }

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) > 1 and sys.argv[1] != " ": 
            prompt = " ".join(sys.argv[1:]).split("--")
            user_prompt = prompt[0]
    else:
        print("Provide a prompt")
        sys.exit(1)
    
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
         model="gemini-2.0-flash-001", 
         contents=messages,
         config=types.GenerateContentConfig(
              tools=[available_functions], system_instruction=system_prompt),
         )

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count
    
    if response.function_calls: #Fix this
       function_call_part = response.function_calls[0]
       print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Response: {response.text}")

    if len(prompt) > 1 and flags.get(prompt[1]) == "verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {X}")
        print(f"Response tokens: {Y}")

if __name__ == "__main__":
    main()
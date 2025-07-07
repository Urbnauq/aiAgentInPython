import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    # print("Hello from aiagentinpython!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    if len(sys.argv) > 1 and sys.argv[1] != " ": 
            contents = str(" ".join(sys.argv[1:]))
    else:
        print("Provide a prompt")
        sys.exit(1)
    
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=contents)
    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count
    
    print(response.text)
    print(f"Prompt tokens: {X}")
    print(f"Response tokens: {Y}")

if __name__ == "__main__":
    main()



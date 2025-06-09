import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt

def main():
    parser = argparse.ArgumentParser(description="AI Agent for Gemini API")
    parser.add_argument("prompt", nargs="+", help="The prompt to send to Gemini")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print a more detailed response")
    args = parser.parse_args()
    
    load_dotenv()
    user_prompt = " ".join(args.prompt)
      
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if args.verbose:
        print("User prompt:", {user_prompt})

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    if args.verbose:
        print("Prompt tokens:", {response.usage_metadata.prompt_token_count})
        print("Response tokens:", {response.usage_metadata.candidates_token_count})
        print("\nResponse:")
    print(response.text)

if __name__ == "__main__":
    main()

import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import call_function, available_functions

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
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt)
    )
    if args.verbose:
        print("Prompt tokens:", {response.usage_metadata.prompt_token_count})
        print("Response tokens:", {response.usage_metadata.candidates_token_count})
        print("\nResponse:")
    print(response.text)

    if not response.function_calls:
        return response.text
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=args.verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
    main()

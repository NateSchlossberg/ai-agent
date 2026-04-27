import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

import prompts
import call_function

def generate_content(client, messages):
    model = 'gemini-2.5-flash'
    res = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[call_function.available_functions],
            system_instruction=prompts.system_prompt,
            # temperature=0
        )
    )
    if not res.usage_metadata:
        raise RuntimeError('Prompt failed, please try again!')
    return res



def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY from environment")
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    res = generate_content(client, messages)
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
    if res.function_calls:
        function_call_messages = map(
            lambda fc: f'Calling function: {fc.name}({fc.args})',
            res.function_calls
        )
        print("\n".join(function_call_messages))
    else:
        print(res.text)

if __name__ == "__main__":
    main()

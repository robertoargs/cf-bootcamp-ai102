"""
Example script demonstrating how to use python-dotenv and the OpenAI SDK.
This script shows how to load environment variables and initialize the OpenAI client.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def main():
    """Main function to demonstrate the setup."""
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        print("You can copy .env.example to .env and add your key.")
        return
    
    print("Environment loaded successfully!")
    print(f"OpenAI API Key loaded: {'*' * 10}{api_key[-4:] if len(api_key) > 4 else '****'}")
    
    # Example: Initialize OpenAI client (uncomment when ready to use)
    # from openai import OpenAI
    # client = OpenAI(api_key=api_key)
    # print("OpenAI client initialized successfully!")

if __name__ == "__main__":
    main()

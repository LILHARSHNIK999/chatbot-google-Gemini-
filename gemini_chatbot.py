#!/usr/bin/env python3
"""
Gemini AI Chatbot

A simple interactive chatbot using Google's Generative AI (Gemini) model.
"""

import os
import sys
import time
import traceback
import re
from typing import Optional

try:
    import google.generativeai as genai
except ImportError:
    print("Required package not found. Installing google-generativeai...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai


def get_api_key() -> str:
    """
    Get the API key from environment variable or prompt the user.
    
    Returns:
        A string containing the API key.
    """
    # First try to get from environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # If not found in environment, prompt the user
    if not api_key:
        print("\n" + "="*50)
        print("\033[1;33mNo valid API key found in environment variables.\033[0m")
        print("You need a valid Google AI Studio API key to use this chatbot.")
        print("Visit: https://aistudio.google.com/app/apikey to get your API key.")
        print("="*50 + "\n")
        
        api_key = input("Please enter your Gemini API key: ").strip()
        
        # Save to environment variable for this session
        os.environ["GEMINI_API_KEY"] = api_key
        
        # Ask if user wants to save for future sessions
        save_choice = input("Save this API key for future sessions? (y/n): ").strip().lower()
        if save_choice == 'y':
            try:
                # Create or update .env file
                with open(".env", "a+") as f:
                    f.write(f"\nGEMINI_API_KEY={api_key}\n")
                print("API key saved to .env file.")
                print("To load it automatically, use: ")
                if os.name == 'nt':  # Windows
                    print("    pip install python-dotenv")
                    print("    Add 'from dotenv import load_dotenv; load_dotenv()' to your script")
                else:  # Unix/Linux/Mac
                    print("    Add 'export GEMINI_API_KEY=your_key' to your .bashrc or .zshrc file")
            except Exception as e:
                print(f"Could not save API key: {e}")
    
    return api_key


def validate_api_key(api_key: str) -> bool:
    """
    Validate the API key format.
    
    Args:
        api_key: The API key to validate.
        
    Returns:
        True if the API key format is valid, False otherwise.
    """
    # Basic validation - Gemini API keys typically start with "AI" and are 39 characters long
    if not api_key or len(api_key) < 30:
        return False
    
    # Check if it matches the typical format (this is a basic check)
    if not re.match(r'^[A-Za-z0-9_-]+$', api_key):
        return False
        
    return True


class GeminiChatbot:
    """A chatbot interface for Google's Gemini AI model."""

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        """
        Initialize the Gemini chatbot.

        Args:
            api_key: The API key for Google Generative AI.
            model_name: The name of the model to use.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.chat = None
        self.setup()

    def setup(self) -> None:
        """Configure the API and start a chat session."""
        try:
            # Validate API key format first
            if not validate_api_key(self.api_key):
                print("\033[1;31mError: The API key format appears to be invalid.\033[0m")
                print("Please check your API key and try again.")
                print("Visit: https://aistudio.google.com/app/apikey to get a valid API key.")
                sys.exit(1)
                
            genai.configure(api_key=self.api_key)
            
            # Test the API key with a simple model call
            try:
                # List available models to verify API key works
                genai.list_models()
                
                # If we get here, the API key is valid
                model = genai.GenerativeModel(self.model_name)
                self.chat = model.start_chat(history=[])
                print(f"Successfully connected to {self.model_name} model.")
            except Exception as e:
                if "API_KEY_INVALID" in str(e):
                    print("\033[1;31mError: The API key is invalid.\033[0m")
                    print("Please get a valid API key from: https://aistudio.google.com/app/apikey")
                    sys.exit(1)
                else:
                    raise e
                    
        except Exception as e:
            print(f"Error setting up Gemini AI: {e}")
            print("If this is an API key issue, please visit: https://aistudio.google.com/app/apikey")
            sys.exit(1)

    def send_message(self, message: str) -> Optional[str]:
        """
        Send a message to the Gemini AI and return the response.

        Args:
            message: The user's message to send.

        Returns:
            The AI's response text or None if an error occurred.
        """
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "API_KEY_INVALID" in error_msg:
                print("\033[1;31mError: The API key is invalid or has expired.\033[0m")
                print("Please get a valid API key from: https://aistudio.google.com/app/apikey")
                sys.exit(1)
            elif "PERMISSION_DENIED" in error_msg:
                print("\033[1;31mError: Permission denied. Your API key may not have access to this model.\033[0m")
                return None
            elif "RESOURCE_EXHAUSTED" in error_msg:
                print("\033[1;31mError: Resource exhausted. You may have reached your quota limit.\033[0m")
                return None
            else:
                print(f"\033[1;31mError communicating with Gemini AI: {e}\033[0m")
                print(traceback.format_exc())
                return None

    def run_chat_loop(self) -> None:
        """Run the main chat loop."""
        print("\n" + "="*50)
        print("Welcome to Gemini AI Chatbot!")
        print("Type 'exit', 'quit', or 'bye' to end the conversation.")
        print("Type 'clear' to start a new conversation.")
        print("="*50 + "\n")

        while True:
            try:
                user_input = input("\033[1;34mYou: \033[0m").strip()
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\nThank you for chatting! Goodbye.")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    self.chat = genai.GenerativeModel(self.model_name).start_chat(history=[])
                    print("\nConversation has been reset.")
                    continue
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Display a "thinking" indicator
                print("\033[1;33mGemini is thinking...\033[0m", end="\r")
                
                # Get response from Gemini
                response = self.send_message(user_input)
                
                # Clear the "thinking" message
                print(" " * 30, end="\r")
                
                if response:
                    print(f"\033[1;32mGemini: \033[0m{response}\n")
                else:
                    print("\033[1;31mSorry, I couldn't get a response. Please try again.\033[0m\n")
                    
            except KeyboardInterrupt:
                print("\n\nInterrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"\n\033[1;31mAn error occurred: {e}\033[0m")
                print("Let's continue our conversation.")


def main():
    """Main function to run the chatbot."""
    # Use the provided API key directly
    api_key = "AIzaSyClrhH15h-x1_hVMpicFR28ZtDQGrhClCg"
    
    try:
        chatbot = GeminiChatbot(api_key=api_key)
        chatbot.run_chat_loop()
    except Exception as e:
        print(f"Fatal error: {e}")
        print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
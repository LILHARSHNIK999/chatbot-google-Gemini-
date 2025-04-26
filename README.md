add ur own api in line number 220 in code 

# Gemini AI Chatbot

A simple interactive chatbot using Google's Generative AI (Gemini) model. This project allows you to have conversations with Google's powerful Gemini AI models directly from your command line.

![Gemini Chatbot Demo](https://i.imgur.com/example.gif)

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Step-by-Step Installation Guide](#step-by-step-installation-guide)
- [Getting a Google AI API Key](#getting-a-google-ai-api-key)
- [Usage Guide](#usage-guide)
- [API Key Management](#api-key-management)
- [Customizing the Chatbot](#customizing-the-chatbot)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- 💬 Interactive command-line interface for chatting with Gemini AI
- 🔄 Conversation management (clear/reset conversation)
- 🎨 Color-coded output for better readability
- 🛡️ Robust error handling for API failures and network issues
- 🔑 Secure API key management options
- 🧩 Simple and clean code structure
- 🔧 Easy customization options

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.7 or higher installed on your system
- Internet connection
- A valid Google AI Studio API key (instructions below)

## Step-by-Step Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install google-generativeai
```
The script will also automatically install this package if it's missing.

### 4. Configure Your API Key

You have several options to provide your API key:

#### Option A: Edit the Script Directly
Open `gemini_chatbot.py` and replace the API key in the `main()` function:

```python
def main():
    """Main function to run the chatbot."""
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    
    try:
        chatbot = GeminiChatbot(api_key=api_key)
        chatbot.run_chat_loop()
    except Exception as e:
        print(f"Fatal error: {e}")
        print(traceback.format_exc())
        sys.exit(1)
```

#### Option B: Set Environment Variable

##### On Windows:
```bash
set GEMINI_API_KEY=your_api_key_here
```

##### On macOS/Linux:
```bash
export GEMINI_API_KEY=your_api_key_here
```

## Getting a Google AI API Key

To use this chatbot, you need a valid API key from Google AI Studio:

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click on "Get API key" or "Create API key"
4. Copy the generated API key (it should look like `AIza...`)
5. Keep this key secure and don't share it publicly

## Usage Guide

### Running the Chatbot

1. Navigate to the project directory:
   ```bash
   cd gemini-chatbot
   ```

2. Run the script:
   ```bash
   python gemini_chatbot.py
   ```

3. If you haven't set up your API key in the script or as an environment variable, you'll be prompted to enter it

### Chatting with Gemini AI

Once the chatbot is running:

1. Type your message and press Enter to send it to Gemini AI
2. Wait for the AI to respond (you'll see "Gemini is thinking..." while it processes)
3. Continue the conversation by typing more messages

### Special Commands

- **Exit the chatbot**: Type `exit`, `quit`, or `bye`
- **Clear conversation history**: Type `clear` to start a fresh conversation
- **Empty input**: Pressing Enter without typing anything will be ignored

### Example Conversation

```
You: Hello, who are you?
Gemini: Hi there! I'm Gemini, a large language model developed by Google. I'm designed to be helpful, harmless, and honest in my interactions. I can assist with a wide range of tasks like answering questions, generating creative content, providing information, and having conversations like this one. How can I help you today?

You: What can you do?
Gemini: I can help with many things! Here are some examples:

1. Answer questions on various topics
2. Generate creative content like stories or poems
3. Summarize information
4. Provide explanations about complex topics
5. Help brainstorm ideas
6. Have thoughtful conversations
7. Assist with language tasks like rephrasing or translation
8. Offer suggestions and recommendations

Is there something specific you'd like help with?

You: clear
Conversation has been reset.

You: Let's talk about something new
Gemini: Absolutely! I'm ready to talk about something new. What topic interests you? We could discuss:

- Science and technology
- Arts and literature
- History and culture
- Philosophy and ideas
- Current events
- Nature and the environment
- Sports and entertainment
- Food and cooking
- Travel and places
- Or anything else that's on your mind!

What would you like to explore?
```

## API Key Management

### Security Best Practices

1. **Never commit your API key to public repositories**
2. **Use environment variables** when possible
3. Consider using a `.env` file with a package like `python-dotenv`
4. Rotate your API keys periodically

### Setting Up Environment Variables Permanently

#### On Windows:
1. Search for "Environment Variables" in the Start menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `GEMINI_API_KEY`
6. Variable value: Your API key
7. Click "OK" on all dialogs

#### On macOS/Linux:
Add to your shell profile file (`.bashrc`, `.zshrc`, etc.):
```bash
export GEMINI_API_KEY=your_api_key_here
```

## Customizing the Chatbot

### Changing the Gemini Model

You can modify the script to use different Gemini models by changing the `model_name` parameter when creating the `GeminiChatbot` instance:

```python
# In the main() function:
chatbot = GeminiChatbot(api_key=api_key, model_name="gemini-2.0-pro")
```

Available models include:
- `gemini-2.0-flash` (default, faster responses)
- `gemini-2.0-pro` (more capable)
- `gemini-1.5-flash`
- `gemini-1.5-pro`

### Modifying the User Interface

You can customize the colors and prompts by editing the relevant sections in the `run_chat_loop()` method.

## Troubleshooting

### Common API Key Issues

1. **"API key not valid" error**:
   - Make sure you've copied the entire key correctly
   - Check for any extra spaces or characters
   - Generate a new key if necessary

2. **"Permission denied" error**:
   - Your API key may not have access to the requested model
   - Try using a different model (e.g., `gemini-1.5-flash`)

3. **"Resource exhausted" error**:
   - You may have reached your quota limit
   - Wait and try again later, or create a new API key

### Installation Problems

1. **Package installation fails**:
   ```bash
   pip install --upgrade pip
   pip install google-generativeai
   ```

2. **Python version issues**:
   - Ensure you're using Python 3.7 or higher:
   ```bash
   python --version
   ```

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is open source and available for personal and educational use.
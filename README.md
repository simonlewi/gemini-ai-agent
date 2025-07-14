# Gemini AI Agent

A command-line AI code assistant powered by Google Gemini. This tool lets you interact with Gemini models, call custom functions, and get code help directly from your terminal.

## Features
- Interact with Google Gemini via the command line
- Supports function calling for advanced tasks
- Verbose mode for debugging and transparency

## Requirements
- Python 3.8 or higher
- Google Gemini Python SDK (`google-generativeai`)
- `python-dotenv` for environment variable management

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gemini-ai-agent.git
   cd gemini-ai-agent
   ```
2. **Install uv (if you don't have it):**
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
   ```
3. **Install dependencies with uv:**
   ```bash
   uv sync
   ```
4. **Set up your API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key_here
     ```

## Usage
Run the assistant from the command line:

```bash
python main.py "your prompt here"
```

- To enable verbose output:
  ```bash
  python main.py "your prompt here" --verbose
  ```
- Example:
  ```bash
  python main.py "How do I fix the calculator?"
  ```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes and add tests if applicable
4. Submit a pull request with a clear description

Please ensure your code follows the existing style and includes appropriate documentation.

## License
MIT License

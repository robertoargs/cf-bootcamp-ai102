# cf-bootcamp-ai102
AI-102 Azure Engineer Associate

## Development Environment

This repository includes a devcontainer configuration for Python development with the following features:

- **Python**: Latest version
- **Libraries**: 
  - `python-dotenv`: For managing environment variables
  - `openai`: OpenAI SDK for Python
- **IDE Support**: GitHub Copilot and Copilot Chat enabled

### Getting Started

1. Open this repository in Visual Studio Code
2. Install the "Dev Containers" extension if you haven't already
3. When prompted, click "Reopen in Container" or run the command "Dev Containers: Reopen in Container"
4. The container will build and install all dependencies automatically
5. Create a `.env` file for your environment variables (e.g., API keys)

### Using Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

Then load it in your Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

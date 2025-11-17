# Matrix Bot

<p align="center">
  <img src="https://gitlab.com/uploads/-/system/project/avatar/38265913/logo.png" alt="Matrix Bot"/>
</p>

A Matrix bot that helps manage TODOs, track expenses, monitor bank accounts, save links, and interact with AI services - all while storing data in org-mode files.

## Features

- **TODO Management**: Create and track TODOs with different categories
  - `!todo` - Regular todos
  - `!repeat` - Repeating tasks
  - `!next` - Next actions
  - `!waiting` - Waiting for items
  - `!someday` - Future tasks
  - `!proj` - Project tasks

- **Task Lists**: View your daily plan
  - `!list free` - Personal tasks
  - `!list work` - Work-related tasks

- **Financial Tracking**:
  - `!bofa` - Check Bank of America account status

- **Link Management**:
  - Auto-saves any shared URL to an org-mode file

- **AI Integration**:
  - Chat with AI models via OpenRouter (continues conversation)
  - Access to hundreds of models including GPT-4, Claude, Llama, and more
  - `!reset` - Reset chat history

## Setup

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Get an OpenRouter API key:
   - Sign up at [OpenRouter](https://openrouter.ai/)
   - Generate an API key at [https://openrouter.ai/keys](https://openrouter.ai/keys)
   - Browse available models at [https://openrouter.ai/models](https://openrouter.ai/models)

3. Create a `.env` file with the following variables:
```
# Matrix Configuration
MATRIX_URL=
MATRIX_USER=
MATRIX_PASSWORD=
MATRIX_USERNAME=
MATRIX_USERNAMES=

# File Locations
EXPENSES_FILENAME=
ORG_LOCATION=
ORG_CAPTURE_FILENAME=
ORG_PLAN_FILENAME=
ORG_LINKS_FILENAME=

# OpenRouter Configuration
OPENROUTER_API_KEY=your-openrouter-api-key
OPENROUTER_MODEL=openai/gpt-4o  # or anthropic/claude-3.5-sonnet, meta-llama/llama-3.1-70b-instruct, etc.
OPENROUTER_SITE_URL=  # Optional: for OpenRouter rankings
OPENROUTER_SITE_NAME=  # Optional: for OpenRouter rankings
```

4. Run the bot:
```bash
python bot.py
```

## Requirements

- Python 3.9+
- Poetry for dependency management
- Matrix server access
- OpenRouter API key (get one at [https://openrouter.ai/keys](https://openrouter.ai/keys))
- Optional: Bank accounts with Bank of America for banking features

## Project Structure

- `bot.py`: Main bot implementation with command handlers
- `ollama_client.py`: OpenRouter API client for AI features
- `bofa.py`: Bank of America data processing
- `org.py`: Org-mode file management
- `settings.py`: Environment configuration

## Dependencies

Key dependencies include:
- `simplematrixbotlib`: Matrix bot framework
- `orgparse`: Org-mode file parsing
- `requests`: API interactions with OpenRouter
- `pyexcel-ods3`: Spreadsheet processing

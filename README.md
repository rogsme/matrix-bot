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
  - Chat with Llama 3.2 via Ollama (continues conversation)
  - `!reset` - Reset chat history

## Setup

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Install and run Ollama:
   - Follow the instructions at [Ollama's website](https://ollama.ai/) to install Ollama
   - Pull the Llama 3.2 model:
   ```bash
   ollama pull llama3.2:latest
   ```
   - Start the Ollama server (it typically runs on port 11434)

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

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:latest
```

4. Run the bot:
```bash
python bot.py
```

## Requirements

- Python 3.9+
- Poetry for dependency management
- Matrix server access
- Optional: Bank accounts with Bank of America for banking features
- Ollama installed and running with the llama3.2:latest model

## Project Structure

- `bot.py`: Main bot implementation with command handlers
- `ollama_client.py`: Ollama API client for AI features
- `bofa.py`: Bank of America data processing
- `org.py`: Org-mode file management
- `settings.py`: Environment configuration

## Dependencies

Key dependencies include:
- `simplematrixbotlib`: Matrix bot framework
- `orgparse`: Org-mode file parsing
- `requests`: API interactions with Ollama
- `pyexcel-ods3`: Spreadsheet processing

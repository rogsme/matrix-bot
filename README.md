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
  - Chat with GPT-4 (continues conversation)
  - `!reset` - Reset chat history
  - `!dalle` - Generate images using DALL-E

## Setup

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Create a `.env` file with the following variables:
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

# API Keys
OPEN_AI_API_KEY=
```

3. Run the bot:
```bash
python bot.py
```

## Requirements

- Python 3.9+
- Poetry for dependency management
- Matrix server access
- Optional: Bank accounts with BROU and Itau for banking features
- Optional: OpenAI API key for AI features

## Project Structure

- `bot.py`: Main bot implementation with command handlers
- `bofa.py`: Bank of America data processing
- `org.py`: Org-mode file management
- `settings.py`: Environment configuration

## Dependencies

Key dependencies include:
- `simplematrixbotlib`: Matrix bot framework
- `orgparse`: Org-mode file parsing
- `openai`: GPT-4 and DALL-E integration
- `pyexcel-ods3`: Spreadsheet processing
- `requests`: API interactions

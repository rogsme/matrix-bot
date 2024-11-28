import os

from dotenv import load_dotenv

load_dotenv()

MATRIX_URL = os.environ.get("MATRIX_URL")
MATRIX_USER = os.environ.get("MATRIX_USER")
MATRIX_PASSWORD = os.environ.get("MATRIX_PASSWORD")
MATRIX_USERNAME = os.environ.get("MATRIX_USERNAME")
MATRIX_USERNAMES = os.environ.get("MATRIX_USERNAMES")

EXPENSES_FILENAME = os.environ.get("EXPENSES_FILENAME")

ORG_LOCATION = os.environ.get("ORG_LOCATION")
ORG_CAPTURE_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_CAPTURE_FILENAME')}"
ORG_PLAN_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_PLAN_FILENAME')}"
ORG_LINKS_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_LINKS_FILENAME')}"

OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")

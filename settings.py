import os

from dotenv import load_dotenv

load_dotenv()

MATRIX_URL = os.environ.get("MATRIX_URL")
MATRIX_USER = os.environ.get("MATRIX_USER")
MATRIX_PASSWORD = os.environ.get("MATRIX_PASSWORD")
MATRIX_USERNAME = os.environ.get("MATRIX_USERNAME")
MATRIX_USERNAMES = os.environ.get("MATRIX_USERNAMES")

BANK_ACCOUNT_NUMBERS = os.environ.get("BANK_ACCOUNT_NUMBERS").split(",")

BROU_USERNAME = os.environ.get("BROU_USERNAME")
BROU_PASSWORD = os.environ.get("BROU_PASSWORD")
ITAU_USERNAME = os.environ.get("ITAU_USERNAME")
ITAU_PASSWORD = os.environ.get("ITAU_PASSWORD")

EXPENSES_FILENAME = os.environ.get("EXPENSES_FILENAME")

NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL")
NEXTCLOUD_USERNAME = os.environ.get("NEXTCLOUD_USERNAME")
NEXTCLOUD_PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")

ORG_LOCATION = os.environ.get("ORG_LOCATION")
ORG_CAPTURE_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_CAPTURE_FILENAME')}"
ORG_PLAN_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_PLAN_FILENAME')}"
ORG_LINKS_FILENAME = f"{ORG_LOCATION}/{os.environ.get('ORG_LINKS_FILENAME')}"

PROMETEO_API_KEY = os.environ.get("PROMETEO_API_KEY")
PROMETEO_URL = os.environ.get("PROMETEO_URL")

OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")

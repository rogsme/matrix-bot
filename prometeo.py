import requests

from settings import PROMETEO_API_KEY, PROMETEO_URL


def get_bank_information(bank: str, username: str, password: str) -> list:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-API-Key": PROMETEO_API_KEY,
    }

    login = requests.post(
        f"{PROMETEO_URL}/login/",
        data={
            "provider": bank,
            "username": username,
            "password": password,
        },
        headers=headers,
    )

    key = login.json().get("key")

    account_data = requests.get(f"{PROMETEO_URL}/account/?key={key}", headers=headers).json()
    requests.get(f"{PROMETEO_URL}/logout/?key={key}", headers=headers)

    return account_data.get("accounts")

"""OpenRouter integration for Matrix bot."""

import json
from typing import Any, Dict, List

import requests

HTTP_OK = 200


class OpenRouterClient:
    """Client for interacting with OpenRouter API."""

    def __init__(
        self,
        api_key: str,
        model: str = "openai/gpt-oss-120b",
        site_url: str = "",
        site_name: str = "",
    ):
        """Initialize the OpenRouter client.

        Args:
            api_key: OpenRouter API key
            model: Model name to use for completions (e.g., "openai/gpt-4o", "anthropic/claude-3.5-sonnet")
            site_url: Optional site URL for rankings on openrouter.ai
            site_name: Optional site name for rankings on openrouter.ai
        """
        self.api_key = api_key
        self.model = model
        self.site_url = site_url
        self.site_name = site_name
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def chat_completion(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Create a chat completion using OpenRouter.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys

        Returns:
            Dict containing the model's response
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # Add optional attribution headers
        if self.site_url:
            headers["HTTP-Referer"] = self.site_url
        if self.site_name:
            headers["X-Title"] = self.site_name

        payload = {
            "model": self.model,
            "messages": messages,
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            data=json.dumps(payload),
        )

        if response.status_code != HTTP_OK:
            raise Exception(f"Error from OpenRouter API: {response.text}")

        return response.json()

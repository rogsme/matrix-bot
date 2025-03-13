"""Ollama integration for Matrix bot."""

import json
from typing import Any, Dict, List

import requests

HTTP_OK = 200


class OllamaClient:
    """Client for interacting with Ollama API."""

    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.2:latest"):
        """Initialize the Ollama client.

        Args:
            base_url: Base URL for the Ollama API
            model: Model name to use for completions
        """
        self.base_url = base_url
        self.model = model
        self.api_url = f"{base_url}/api"

    def chat_completion(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Create a chat completion using Ollama.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys

        Returns:
            Dict containing the model's response
        """
        # Convert OpenAI-style messages to Ollama format
        # Ollama expects a simpler format with just the messages array
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }

        response = requests.post(
            f"{self.api_url}/chat",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
        )

        if response.status_code != HTTP_OK:
            raise Exception(f"Error from Ollama API: {response.text}")

        result = response.json()

        # Convert Ollama response to a format similar to OpenAI for easier integration
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": result["message"]["content"],
                    },
                },
            ],
            "model": self.model,
        }

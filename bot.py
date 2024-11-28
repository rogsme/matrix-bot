"""A Matrix bot that manages TODOs, expenses, and AI interactions."""

import os

import openai
import simplematrixbotlib as botlib
import validators
import wget

from bofa import BofaData
from org import OrgData
from settings import (
    MATRIX_PASSWORD,
    MATRIX_URL,
    MATRIX_USER,
    MATRIX_USERNAME,
    MATRIX_USERNAMES,
    OPEN_AI_API_KEY,
)

openai.api_key = OPEN_AI_API_KEY

creds = botlib.Creds(MATRIX_URL, MATRIX_USER, MATRIX_PASSWORD)
bot = botlib.Bot(creds)

PREFIX = "!"

MATRIX_USERNAMES = MATRIX_USERNAMES.split(",")

starting_prompt = {"role": "system", "content": "You are a very helpful chatbot"}

CONVERSATION = {}
for username in MATRIX_USERNAMES:
    CONVERSATION[username] = [starting_prompt]


@bot.listener.on_message_event
async def todo(room, message):
    """Add new TODOs with specified details.

    Usage:
    user:  !todo title - objective - extra (optional)
    bot:   TODO added!
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix():
        user = message.sender
        keyword = str(message).split()[1].replace("!", "").lower()

        if user == MATRIX_USERNAME and keyword in ["todo", "repeat", "next", "waiting", "someday", "proj"]:
            message = " ".join(message.body.split(" ")[1:])
            room_id = room.room_id
            splitted_message = message.split("-")

            try:
                todo_title = splitted_message[0].strip()
                todo_objective = splitted_message[1].strip()
            except IndexError:
                return await bot.api.send_text_message(
                    room_id,
                    "An objective is needed. The correct format is 'Title - Objective - Extra (optional)'",
                )

            try:
                todo_extra = splitted_message[2].strip()
            except IndexError:
                todo_extra = ""

            print(f"Room: {room_id}, User: {user}, Message: {message}")
            OrgData().add_new_todo(keyword, todo_title, todo_objective, todo_extra)
            return await bot.api.send_text_message(room_id, "TODO added!")
    return None


@bot.listener.on_message_event
async def list_todos(room, message):
    """List today's plan from org files.

    Usage:
    user:  !list [free,work]
    bot:   [prints a list with today's todos]
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("list"):
        user = message.sender

        if user == MATRIX_USERNAME:
            message = " ".join(message.body.split(" ")[1:]).strip() or "free"
            room_id = room.room_id

            if message not in ["free", "work"]:
                return await bot.api.send_text_message(
                    room_id,
                    f'"{message}" not accepted. Accepted options are "free" and "work"',
                )

            print(f"Room: {room_id}, User: {user}, Message: {message}")
            plan = OrgData().list_plan(message)
            return await bot.api.send_text_message(room_id, plan)
    return None


@bot.listener.on_message_event
async def list_bofa_status(room, message):
    """Show Bank of America account status.

    Usage:
    user:  !bofa
    bot:   [prints bofa current status]
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("bofa"):
        user = message.sender

        if user == MATRIX_USERNAME:
            room_id = room.room_id
            print(f"Room: {room_id}, User: {user}, Message: bofa")

            bofa_data = BofaData().get()

            return_data = ""
            for person, amount in bofa_data.items():
                if amount != "0 USD":
                    return_data += f"{person}: {amount}\n"

            return await bot.api.send_text_message(room_id, return_data)
    return None


@bot.listener.on_message_event
async def save_link(room, message):
    """Save a URL to the links file.

    Usage:
    user:  [any valid URL]
    bot:   Link added!
    """
    match = botlib.MessageMatch(room, message, bot)
    message_content = message.body
    if match.is_not_from_this_bot() and validators.url(message_content):
        user = message.sender

        if user == MATRIX_USERNAME:
            room_id = room.room_id
            print(f"Room: {room_id}, User: {user}, Message: {message_content}")

            OrgData().add_new_link(f"- {message_content}\n")
            return await bot.api.send_text_message(room_id, "Link added!")
    return None


@bot.listener.on_message_event
async def chatgpt(room, message):
    """Start a conversation with ChatGPT.

    Usage:
    user:  !chatgpt Hello!
    bot:   [prints chatgpt response]
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    message_content = message.body
    if match.is_not_from_this_bot() and not match.prefix() and not validators.url(message_content):
        user = message.sender

        if user in MATRIX_USERNAMES:
            personal_conversation = CONVERSATION[user]
            room_id = room.room_id

            print(f"Room: {room_id}, User: {user}, Message: chatgpt")

            def format_message(message):
                return {"role": "user", "content": message}

            personal_conversation.append(format_message(message_content))

            try:
                completion = openai.ChatCompletion.create(model="gpt-4-1106-preview", messages=personal_conversation)
                response = completion.choices[0].message.content
                personal_conversation.append(completion.choices[0].message)
            except Exception as e:
                print(f"Error: {e}")
                response = "There was a problem with your prompt"

            return await bot.api.send_text_message(room_id, response)
    return None


@bot.listener.on_message_event
async def reset_chatgpt(room, message):
    """Reset the ChatGPT conversation history.

    Usage:
    user:  !reset
    bot:   Conversation reset!
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("reset"):
        user = message.sender

        if user in MATRIX_USERNAMES:
            CONVERSATION[user] = [starting_prompt]
            room_id = room.room_id

            return await bot.api.send_text_message(room_id, "Conversation reset!")
    return None


@bot.listener.on_message_event
async def dall_e(room, message):
    """Generate an image using DALL-E.

    Usage:
    user:  !dalle A sunny caribbean beach
    bot:   returns an image
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dalle"):
        user = message.sender

        if user in MATRIX_USERNAMES:
            room_id = room.room_id
            message = " ".join(message.body.split(" ")[1:]).strip()

            print(f"Room: {room_id}, User: {user}, Message: dalle")
            await bot.api.send_text_message(room_id, "Generating image...")

            try:
                image = openai.Image.create(prompt=message)
                image_url = image["data"][0]["url"]
                image_filename = wget.download(image_url)

                await bot.api.send_image_message(room_id, image_filename)
                os.remove(image_filename)
                return None
            except Exception as e:
                print(f"Error sending image: {e}")
                return await bot.api.send_text_message(room_id, f"Error sending image: {e}")
    return None


bot.run()

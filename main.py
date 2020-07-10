#!/usr/bin/env python3
"""This module contains the ping pong bot, which responds to messages that
contain the word 'ping'."""

import re
import discord

client = discord.Client()


@client.event
async def on_ready():
    """Lets you know when the bot starts."""
    print(f"Discord version: {discord.__version__}")
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    """Responds when someone else sends a message."""
    if message.author == client.user:
        return
    if "ping" in message.content.lower():
        await message.channel.send(
            re.sub("ping", "pong", message.content, flags=re.IGNORECASE))


def main():
    """Runs the bot with the token from the file called 'token'."""
    with open("token") as token_file:
        token = token_file.read()
    client.run(token)


if __name__ == "__main__":
    main()

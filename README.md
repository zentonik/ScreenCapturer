# Discord Screenshot Bot

This Discord bot allows users to capture and send screenshots to a specified channel. By typing a command in the designated channel, the bot captures a screenshot of your screen and sends it as an image file to the same channel.

## Features

- Captures screenshots of your screen.
- Sends the captured screenshot to a specified Discord channel.
- Supports command-based triggering.

## Requirements

- Python 3.7+
- `discord.py` library
- `Pillow` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/ScreenCapturer.git
    cd ScreenCapturer
    ```


2. **Configure the bot:**

    - Replace `'Token'` with your bot's token in the `TOKEN` variable.
    - Replace `1281311409992634397` with the ID of the channel

## Usage

1. **Run the bot:**

    ```bash
    python bot.py
    ```

2. **Use the command:**

    - Type `!capture` in the specified channel to trigger a screenshot capture and send the image.

## Code Overview

- **Imports:**
    - `discord` and `commands` for interacting with the Discord API.
    - `ImageGrab` for capturing screenshots.
    - `time` for generating unique filenames.
    - `os` for file operations.

- **`capture_screenshot()` Function:**
    - Captures a screenshot and saves it with a timestamp-based filename.

- **Bot Events and Commands:**
    - `on_ready()`: Runs when the bot is ready.
    - `capture(ctx)`: Captures a screenshot and sends it to the specified channel when the `!capture` command is used.

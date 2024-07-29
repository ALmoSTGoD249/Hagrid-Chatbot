# Hagrid: Your Personal Assistant

Hagrid is a personal assistant powered by OpenAI's GPT-4. It can perform various tasks like searching the web, opening applications, managing volume, generating images, fetching weather information, and more.

## Features

- Open applications (e.g., Notepad)
- Search the web
- Shutdown and restart your computer
- Change volume (up, down, mute, unmute)
- Fetch information from OpenAI's GPT-4
- Generate images using OpenAI's DALL-E
- Play music on YouTube
- Fetch weather information
- Tell jokes
- Set reminders

## Prerequisites

- Python 3.7+
- An OpenAI API key
- A Weather API key from OpenWeatherMap

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ALmoSTGoD249/Hagrid-Chatbot.git
    cd Hagrid-Chatbot
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    You can either set them directly in your environment or use a `.env` file.

    **Using a `.env` file:**

    - Create a file named `.env` in the project root directory.

    - Add your API keys to the `.env` file:

      ```plaintext
      OPENAI_API_KEY=your_openai_api_key
      WEATHER_API_KEY=your_weather_api_key
      ```

    **Directly in your environment:**

    On Windows:
    1. Open the Start Search, type in "env", and select "Edit the system environment variables".
    2. In the System Properties window, click on the "Environment Variables" button.
    3. In the Environment Variables window, click "New" to add a new environment variable.
    4. Set the variable name to `OPENAI_API_KEY` and the value to your OpenAI API key.
    5. Repeat step 4 for the `WEATHER_API_KEY`.

    On macOS/Linux:
    1. Open your terminal.
    2. Edit your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, `~/.profile`).
    3. Add the following lines to set your environment variables:
        ```sh
        export OPENAI_API_KEY='your_openai_api_key'
        export WEATHER_API_KEY='your_weather_api_key'
        ```
    4. Save the file and run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

## Usage

Run the script to start Hagrid:

```bash
python hagrid.py
```

Once running, you can interact with Hagrid by typing commands. Here are some examples:

- **Open Notepad:**
  ```plaintext
  open notepad
  ```

- **Search the web:**
  ```plaintext
  search Python programming
  ```

- **Shutdown the computer:**
  ```plaintext
  shutdown
  ```

- **Restart the computer:**
  ```plaintext
  restart
  ```

- **Change volume:**
  ```plaintext
  change volume up
  change volume down
  change volume mute
  change volume unmute
  ```

- **Fetch information using GPT-4:**
  ```plaintext
  tell me about Python
  ```

- **Generate an image:**
  ```plaintext
  generate image of a sunset over mountains
  ```

- **Play music:**
  ```plaintext
  play music Bohemian Rhapsody
  ```

- **Fetch weather information:**
  ```plaintext
  weather London
  ```

- **Tell a joke:**
  ```plaintext
  joke
  ```

- **Set a reminder:**
  ```plaintext
  set reminder 14:30 Meeting with team
  ```

## Screenshot


![image](https://github.com/user-attachments/assets/9e5c9d63-0745-4fa3-b49e-013fe2da42c1)


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. 

## Contact

- **Soumyadeep Maity** - [Email](mailto:soumadeepmaity2@gmail.com)
- **Instagram**: [almostgod7](https://www.instagram.com/almostgod7/)

---

### Note

Remember to keep your API keys secure and never share them publicly.

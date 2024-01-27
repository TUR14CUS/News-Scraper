## Overview

This Python script fetches the latest news articles related to a specified topic using the News API and sends an email containing a summary of the headlines. It is designed to be a simple tool for staying updated on a particular subject.

## Prerequisites

Before running the script, ensure that you have the following:

- Python installed on your machine
- `requests` library installed. You can install it using:
  ```bash
  pip install requests
  ```
- A valid API key from [News API](https://newsapi.org/) (free or paid subscription)

## Setup

1. Clone or download the repository.

2. Replace the placeholder `api_key` variable with your News API key:
    ```python
    api_key = "your_api_key_here"
    ```

3. Set the desired `topic` variable to the topic you want to get news about:
    ```python
    topic = "samsung"
    ```

## Running the Script

Execute the script in your terminal or command prompt:
```bash
python news_scraper.py
```

The script will fetch the latest news articles related to the specified topic, create an email body with article headlines, descriptions, and URLs, and then send the email using the `send_mail` module.

## Note

- Ensure that you have set up the email configuration in the `send_mail` module before running the script. You might need to provide your email credentials and adjust the SMTP server settings.

- The script is currently set to fetch and include details of the top 20 articles. You can modify this by changing the slicing in the loop:
    ```python
    for article in contect["articles"][:20]:
    ```

Feel free to customize the script to fit your preferences or use it as a starting point for more advanced applications.

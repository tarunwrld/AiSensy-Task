# Web Content Q&A Tool

## Overview
This project is a web-based tool that allows users to enter URLs, scrape content from the specified websites, and then ask questions based solely on the ingested website content. The tool uses Google Gemini AI (formerly known as Gemini) to process the scraped data and provide concise, accurate answers.

## Features:
- **URL Input**: Enter a URL to scrape and ingest the website's content.
- **Q&A Functionality**: Ask questions about the content of the scraped page.
- **Concise Answers**: Receive answers based only on the scraped website content, ensuring the answers are grounded in the page's information.

## Demo
You can run the tool locally by following the steps in the "Installation" section below. Alternatively, website is live https://tjwrld-ai-web-scrapper.hf.space.

## How It Works
1. **Input URLs**: The user enters a URL in the input box to scrape the page content.
2. **Scraping and Parsing**: The app uses Selenium to load and scrape the webpage and BeautifulSoup to parse the HTML.
3. **AI-based Q&A**: After scraping the content, users can ask questions, and the AI model will respond based on the ingested data.
4. **Streamlit UI**: The user interface is built using Streamlit, offering a clean, minimalistic design for interaction.

## Flaws
1. Input url is input only one time if user have to enter another website should be refreshed.
2. After Scrapping Question Answering appears at bottom.
3. For large content api limit exceeds.

## Requirements
Before running the application, ensure you have the following dependencies:

- Python 3.x

### Libraries:
- `google-generativeai`
- `streamlit`
- `selenium`
- `beautifulsoup4`
# Installation


1. Clone Project:
    ```bash
   git clone https://github.com/tarunwrld/](https://github.com/tarunwrld/AiSensy-Task

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

3. Set up your Gemini API Key:

Obtain an API key for Google Gemini AI.
Replace "AI_API_KEY" in the main.py file with your actual key.

4. Run the Streamlit app:
    ```bash
    streamlit run main.py
Visit http://localhost:8501 in your browser to use the tool.# Web Scraper with AI-Powered Q&A

## Usage

### Enter the URL:
On the homepage, input the URL of the website you want to scrape.

### Scrape and Display Content:
Once the URL is entered, the content is scraped, and a snippet of the HTML content will be displayed on the page.

### Ask Questions:
After the content is ingested, you can enter questions about the content of the webpage. The AI model will respond based on the scraped data.

### Receive Answers:
The answers are generated using only the scraped information, ensuring that the responses are relevant and accurate to the content of the page.

## Features

- **Single-Page UI**: A simple, user-friendly interface built with Streamlit.
- **Persistent Content**: Once a URL is entered, the content is stored in the session, allowing users to ask multiple questions without re-entering the URL.
- **AI-Powered Responses**: The Gemini model processes the content and provides relevant answers to user queries.



## Acknowledgments

- **Streamlit**: Used to build the interactive web interface.
- **BeautifulSoup**: Used for parsing HTML content.
- **Google Gemini AI**: Provides the AI model to process and generate answers based on the ingested content.

## Important Notes

- The project uses the **Gemini API key**, which requires a valid API key. Ensure the key is set in the code for proper functionality.
- The tool is designed to scrape the content of websites, and it is essential to adhere to web scraping best practices and legal considerations when using it.


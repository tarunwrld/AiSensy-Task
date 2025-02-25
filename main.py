import os
import google.generativeai as genai
import streamlit as st
from selenium import webdriver
from bs4 import BeautifulSoup

genai.configure(api_key=os.environ["AI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
def scrape_website(website):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)  # Uses chromedriver from PATH
    driver.get(website)
    html = driver.page_source
    driver.quit()
    return html

st.set_page_config(
    page_title="AI Web Scraper",
    page_icon=":robot_face:",
    layout="wide",
    menu_items={
        'About': "# Under Construction"
    }
)

def main():
    with st.sidebar:
        st.sidebar.title("Navigation")
        hide_st_style = '''
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                # header {visibility: hidden;}
                </style>
                '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

        page = st.sidebar.radio("Options", ["Home", "Privacy Policy"], label_visibility="collapsed")

    if page == "Home":
        with st.container():
            st.title("Website Scraping and AI Response Generation")
            st.write("Enter the URL of the website you want to scrape and process.")
            if "html_content" not in st.session_state:
                # Take the URL as input from the user
                url = st.text_input("Enter the URL to scrape:")

                if url:
                    st.write(f"Scraping the website: {url}")
                    html_content = scrape_website(url)
                    soup = BeautifulSoup(html_content, "html.parser")
                    full_html_content = soup.prettify()

                    st.session_state.html_content = full_html_content
                    st.subheader("Extracted HTML Content:")
                    st.text(full_html_content[:1000])  # Display the first 1000 characters
                    st.session_state.chat_session = model.start_chat(
                        history=[{
                            "role": "user",
                            "parts": [
                                "This is HTML content, follow the user input and give the output using parsed content:\n" + full_html_content
                            ],
                        }]
                    )
            if "html_content" in st.session_state:
                input_message = st.text_input("Enter your question:")

                if input_message:
                    chat_session = st.session_state.chat_session
                    response = chat_session.send_message(input_message)
                    st.subheader("AI Response:")
                    st.write(response.text)

if __name__ == "__main__":
    main()

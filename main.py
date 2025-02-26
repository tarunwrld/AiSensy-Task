import os
import google.generativeai as genai
import requests
import streamlit as st
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
    system_instruction="This is HTML content, follow the user input and give the output using parsed content.Output should be based on the HTML content provided by the user nothing else"

)
def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.prettify() 
    except requests.exceptions.RequestException as e:
        return f"Error fetching page: {e}"

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
            st.write("Enter the URL of the website you want to scrape and process or refresh to add new url.")
            if "html_content" not in st.session_state:
                url = st.text_input("Enter the URL to scrape:")
                button = st.button("Scrape")

                if button:
                    st.write(f"Scraping the website: {url}")

                    html_content = scrape_website(url)
                    soup = BeautifulSoup(html_content, "html.parser")
                    full_html_content = soup.prettify()
                    st.session_state.html_content = full_html_content
                    st.subheader("Extracted HTML Content:")
                    st.text_area("HTML Content", full_html_content, height=400)  # Display the first 1000 characters

                    st.session_state.chat_session = model.start_chat(
                        history=[{
                            "role": "user",
                            "parts": [
                                full_html_content
                            ],
                        }]
                    )
            if "html_content" in st.session_state:
                input_message = st.text_input("Enter your question:")
                button1 = st.button("Send")

                if button1:
                    chat_session = st.session_state.chat_session

                    response = chat_session.send_message(input_message)


                    st.subheader("AI Response:")
                    message = st.chat_message("assistant")
                    message.write(response.text)
                    # st.write(response.text)

if __name__ == "__main__":
    main()

import streamlit as st
import requests
import json

def generate_response(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "stream": False
    }
    st.write(f"Sending request to: {url}")  # Debug statement
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code}")
        st.error(response.text)
        return None

def main():
    st.title("Code Assistant")
    prompt = st.text_area("Enter your prompt", height=100)
    if st.button("Submit"):
        response = generate_response(prompt)
        if response:
            st.text_area("Response", value=response, height=200)

if __name__ == "__main__":
    main()

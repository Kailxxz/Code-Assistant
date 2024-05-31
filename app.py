import requests
import json
import streamlit as st

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "codingsensei",
        "prompt": final_prompt,
        "stream": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.json()
        actual_response = response['response']
        return actual_response
    else:
        st.error(f"Error: {response.text}")

def main():
    st.title("Code assistant")
    prompt = st.text_area("Enter your prompt", height=100)
    if st.button("Submit"):
        response = generate_response(prompt)
        st.text_area("Response", value=response, height=100)

if __name__ == "__main__":
    main()

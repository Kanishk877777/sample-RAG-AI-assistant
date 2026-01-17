import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="Legal AI", layout="wide")
st.title("⚖️ Legal AI Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask a legal question:")

if st.button("Ask") and query:
    try:
        response = requests.post(API_URL, json={"query": query})

        # Check if the server responded correctly (Status 200)
        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "No answer found in response.")

            st.session_state.chat.append(("You", query))
            st.session_state.chat.append(("AI", answer))
        else:
            # Display the actual error from the backend instead of crashing
            st.error(f"Backend Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Connection Error: Could not reach the backend. {e}")

for role, msg in st.session_state.chat:
    st.markdown(f"**{role}:** {msg}")

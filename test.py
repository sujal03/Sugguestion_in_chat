import streamlit as st
import openai
import os
import json

# Set up your OpenAI API key
openai.api_key = ""

# File to store conversation history
CONVERSATION_FILE = "conversation_history.json"

class ChatBot:
    def __init__(self, engine: str = "gpt-3.5-turbo") -> None:
        self.model = engine
        self.conversation_history = self.load_conversation_history()

    def load_conversation_history(self) -> list:
        if os.path.exists(CONVERSATION_FILE):
            with open(CONVERSATION_FILE, 'r') as file:
                return json.load(file)
        else:
            return [{"role": "system", "content": "You are a helpful assistant."}]

    def save_conversation_history(self) -> None:
        with open(CONVERSATION_FILE, 'w') as file:
            json.dump(self.conversation_history, file, indent=4)

    def send_message(self, message: str) -> str:
        self.conversation_history.append({"role": "user", "content": message})
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
            )
            assistant_response = response['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            self.save_conversation_history()
            return assistant_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_suggestions(self) -> list:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Generate 5 chat suggestions based on the conversation history."},
                    {"role": "user", "content": json.dumps(self.conversation_history)},
                ],
            )
            suggestions = response['choices'][0]['message']['content']
            return suggestions.split('\n')[:5]  # Split and take the first 5 suggestions
        except Exception as e:
            return [f"An error occurred: {str(e)}"]

def start_chatbot():
    st.title("Chatbot with User Context and Chat Suggestions")

    # Initialize chat history in Streamlit session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    chatbot = ChatBot()

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get and display assistant response
        response = chatbot.send_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    # Generate and display chat suggestions
    st.sidebar.header("Chat Suggestions")
    suggestions = chatbot.generate_suggestions()
    for suggestion in suggestions:
        if st.sidebar.button(suggestion):
            # Treat the suggestion as user input
            st.session_state.messages.append({"role": "user", "content": suggestion})
            with st.chat_message("user"):
                st.markdown(suggestion)

            # Get and display assistant response
            response = chatbot.send_message(suggestion)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

if __name__ == "__main__":
    start_chatbot()
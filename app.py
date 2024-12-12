# import openai
# import os
# import json

# # Set up your OpenAI API key
# openai.api_key = "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"

# # File to store conversation history
# CONVERSATION_FILE = "conversation_history.json"

# class ChatBot:
#     def __init__(self, engine: str = "gpt-3.5-turbo") -> None:
#         self.model = engine
#         self.conversation_history = self.load_conversation_history()

#     def load_conversation_history(self) -> list:
#         if os.path.exists(CONVERSATION_FILE):
#             with open(CONVERSATION_FILE, 'r') as file:
#                 return json.load(file)
#         else:
#             return [{"role": "system", "content": "You are a helpful assistant."}]

#     def save_conversation_history(self) -> None:
#         with open(CONVERSATION_FILE, 'w') as file:
#             json.dump(self.conversation_history, file, indent=4)

#     def send_message(self, message: str) -> str:
#         self.conversation_history.append({"role": "user", "content": message})
#         try:
#             response = openai.ChatCompletion.create(
#                 model=self.model,
#                 messages=self.conversation_history,
#             )
#             assistant_response = response['choices'][0]['message']['content']
#             self.conversation_history.append({"role": "assistant", "content": assistant_response})
#             self.save_conversation_history()
#             return assistant_response
#         except Exception as e:
#             return f"An error occurred: {str(e)}"

# def start_chatbot():
#     print("👋 Welcome! I'm your chatbot. Type 'exit' to end the conversation.")
#     chatbot = ChatBot()
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             print("Goodbye!")
#             break
#         response = chatbot.send_message(user_input)
#         print(f"Chatbot: {response}")

# if __name__ == "__main__":
#     start_chatbot()





























# import streamlit as st
# import openai
# import os
# import json

# # Set up your OpenAI API key
# openai.api_key = "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"

# # File to store conversation history
# CONVERSATION_FILE = "conversation_history.json"

# class ChatBot:
#     def __init__(self, engine: str = "gpt-3.5-turbo") -> None:
#         self.model = engine
#         self.conversation_history = self.load_conversation_history()

#     def load_conversation_history(self) -> list:
#         if os.path.exists(CONVERSATION_FILE):
#             with open(CONVERSATION_FILE, 'r') as file:
#                 return json.load(file)
#         else:
#             return [{"role": "system", "content": "You are a helpful assistant."}]

#     def save_conversation_history(self) -> None:
#         with open(CONVERSATION_FILE, 'w') as file:
#             json.dump(self.conversation_history, file, indent=4)

#     def send_message(self, message: str) -> str:
#         self.conversation_history.append({"role": "user", "content": message})
#         try:
#             response = openai.ChatCompletion.create(
#                 model=self.model,
#                 messages=self.conversation_history,
#             )
#             assistant_response = response['choices'][0]['message']['content']
#             self.conversation_history.append({"role": "assistant", "content": assistant_response})
#             self.save_conversation_history()
#             return assistant_response
#         except Exception as e:
#             return f"An error occurred: {str(e)}"

#     def generate_suggestions(self) -> list:
#         try:
#             response = openai.ChatCompletion.create(
#                 model=self.model,
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant. Generate 5 chat suggestions based on the conversation history."},
#                     {"role": "user", "content": json.dumps(self.conversation_history)},
#                 ],
#             )
#             suggestions = response['choices'][0]['message']['content']
#             return suggestions.split('\n')[:5]  # Split and take the first 5 suggestions
#         except Exception as e:
#             return [f"An error occurred: {str(e)}"]

# def start_chatbot():
#     st.title("Chatbot with User Context and Chat Suggestions")

#     # Initialize chat history in Streamlit session state
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     chatbot = ChatBot()

#     # Display chat messages from history on app rerun
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Accept user input
#     if prompt := st.text_input("What is up?"):
#         # Display user message in chat message container
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Get and display assistant response
#         response = chatbot.send_message(prompt)
#         st.session_state.messages.append({"role": "assistant", "content": response})
#         with st.chat_message("assistant"):
#             st.markdown(response)

#     # Generate and display chat suggestions
#     st.sidebar.header("Chat Suggestions")
#     suggestions = chatbot.generate_suggestions()
#     for suggestion in suggestions:
#         if st.sidebar.button(suggestion):
#             # Treat the suggestion as user input
#             st.session_state.messages.append({"role": "user", "content": suggestion})
#             with st.chat_message("user"):
#                 st.markdown(suggestion)

#             # Get and display assistant response
#             response = chatbot.send_message(suggestion)
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             with st.chat_message("assistant"):
#                 st.markdown(response)

# if __name__ == "__main__":
#     start_chatbot()





















import openai
import os
import json

# Set up your OpenAI API key
openai.api_key = "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"

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

    def suggest_responses(self, user_input: str) -> list:
        suggestion_prompt = (
            f"Based on the user's message: '{user_input}', suggest 3 possible follow-up questions or topics they might want to explore."
        )
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history + [{"role": "user", "content": suggestion_prompt}],
            )
            suggestions = response['choices'][0]['message']['content']
            return suggestions.strip().split('\n')[:3]  # Return the first 3 suggestions
        except Exception as e:
            return [f"Error generating suggestions: {str(e)}"]

    def send_message(self, message: str) -> str:
        self.conversation_history.append({"role": "user", "content": message})
        try:
            # Generate a response
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

def start_chatbot():
    print("👋 Welcome! I'm your chatbot. Type 'exit' to end the conversation.")
    chatbot = ChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.send_message(user_input)
        print(f"Chatbot: {response}")

        # Provide suggestions
        suggestions = chatbot.suggest_responses(user_input)
        print("\nSuggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")

        # Let the user select a suggestion or continue with their input
        try:
            choice = int(input("\nEnter the number of your choice (or 0 to continue with your message): "))
            if 1 <= choice <= len(suggestions):
                user_input = suggestions[choice - 1]
        except ValueError:
            print("Invalid choice, continuing with your original message.")

        # Send the message to the chatbot
        response = chatbot.send_message(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()

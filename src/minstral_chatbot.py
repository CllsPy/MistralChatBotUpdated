import streamlit as st
#from mistralai.client import MistralClient
#from mistralai.models.chat_completion import ChatMessage
from mistralai import Mistral, UserMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Mistral AI client
def get_mistral_client():
    # Best practice: Use environment variable for API key
    api_key = os.getenv('MISTRAL_API_KEY')
    if not api_key:
        st.error("Please set the MISTRAL_API_KEY environment variable")
        return None
    return Mistral(api_key=api_key)

# Function to generate chat response
def get_mistral_response(client, messages):
    try:
        chat_response = client.chat.complete(
            model="mistral-large-latest",  # You can choose different models
            messages=messages
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Streamlit App
def main():
    st.title("Friendly: Your Mistral ChatBot")
    st.write("Hey, let's chat. What do you like to talk about?")

    with st.sidebar:
        st.title("About")
        st.markdown("""MistralChatBotUpdated is a 
                    ChatBot that utilizes Streamlit as the graphical 
                    user interface (GUI) and integrates with the Mistral 
                    API as its large language model (LLM).""")
        
        
        st.markdown("---")
        st.markdown(f' made by [CLL](https://github.com/CllsPy)')
    

    # Initialize session state for chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Initialize Mistral client
    mistral_client = get_mistral_client()
    if not mistral_client:
        return
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Sobre o que quer conversar?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Prepare messages for Mistral API
        mistral_messages = [
            UserMessage(role="user", content=prompt) 
            for msg in st.session_state.messages
        ]
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                assistant_response = get_mistral_response(mistral_client, mistral_messages)
                
            if assistant_response:
                st.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": assistant_response
                })

main()
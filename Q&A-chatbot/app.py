import streamlit as st
import cohere

# Initialize Cohere Client with your API key
co = cohere.Client('Ko76cA3WuBPjFurTN166q55Pi2YlkQ3MWWeQSdgC')  # Replace with your actual API key

# Function to get responses from Cohere model for Q&A
def getCohereResponse(question, chat_history):
    # Prompt Template for Q&A
    prompt = f"""
    You are a helpful and knowledgeable assistant. Answer the following question based on the previous conversation:
    {chat_history}
    Q: {question}
    A:
    """
    
    # Cohere generate API call
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100,  # Adjust based on the length of the response you want
        temperature=0.5,  # Lower temperature for more focused answers
        stop_sequences=["\n"],  # Stop at the end of the answer
    )

    return response.generations[0].text if response.generations else "No answer generated"

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot", page_icon="💬")

st.title("Conversational Q&A Chatbot 💬")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = ""

# User input
user_question = st.text_input("Ask me anything!")

# When user submits a question
if st.button("Ask"):
    if user_question:
        # Get the response from Cohere
        chat_history = st.session_state['chat_history']
        answer = getCohereResponse(user_question, chat_history)
        
        # Update chat history
        st.session_state['chat_history'] += f"Q: {user_question}\nA: {answer}\n\n"
        
        # Display conversation history
        st.text_area("Conversation", st.session_state['chat_history'], height=300)
    else:
        st.warning("Please enter a question.")

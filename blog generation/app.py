import cohere
import streamlit as st

# Function to generate text using Cohere
def get_cohere_response(input_text, no_words, blog_style):
    # Initialize the Cohere client with your API key
    cohere_api_key = 'key'  # Replace with your actual API key
    co = cohere.Client(cohere_api_key)

    # Create a prompt by combining the input_text and blog_style
    prompt = f"Write a {no_words}-word blog in the style of {blog_style} on the topic: {input_text}"

    # Call Cohere's generate endpoint
    response = co.generate(
        model='command-xlarge-nightly',  # You can also use other models if needed
        prompt=prompt,
        max_tokens=500,  # Adjust based on your word count
        temperature=0.7,  # Adjust for creativity; 0.7 is a good balance
        stop_sequences=["--end--"]  # Define a stop sequence if needed
    )

    # Return the generated text
    return response.generations[0].text

# Streamlit app
st.title("Blog Generator with Cohere")
input_text = st.text_input("Enter the topic for your blog:")
no_words = st.slider("Choose the word count for the blog:", 100, 1000, step=100)
blog_style = st.selectbox("Choose a style for your blog:", ["informative", "casual", "technical", "entertaining"])

if st.button("Generate Blog"):
    if input_text:
        blog = get_cohere_response(input_text, no_words, blog_style)
        st.write(blog)
    else:
        st.warning("Please enter a topic to generate the blog.")

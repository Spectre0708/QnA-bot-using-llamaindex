# main.py

# Import necessary libraries
import os
import streamlit as st
from huggingface_hub import login
from llama_index.readers.web import SimpleWebPageReader
from llama_index.llms.huggingface import HuggingFaceInferenceAPI
from llama_index.core import SummaryIndex

# Set the title of the Streamlit app
st.title("Hugging Face Query App")

# Create a text input for the Hugging Face token
hf_token = st.text_input("Enter your Hugging Face token:", type="password")

# Button to authenticate with Hugging Face
if st.button("Authenticate"):
    if hf_token:
        try:
            login(token=hf_token)
            st.success("Successfully authenticated with Hugging Face!")
        except Exception as e:
            st.error(f"Authentication failed: {e}")
    else:
        st.error("Please enter a valid token.")

# Create a section for the user to input the query
if hf_token:  # Proceed only if the token is provided
    url = st.text_input("Enter the URL to query:", "https://ohsl.us/projects/bcda")  # Default URL
    query = st.text_input("Enter your query:")

    if st.button("Submit Query"):
        # Load the documents from the specified URL
        try:
            documents = SimpleWebPageReader(html_to_text=True).load_data([url])  # Use user-provided URL

            # Initialize the LLM using the Hugging Face API
            llm = HuggingFaceInferenceAPI(model_name='mistralai/Mixtral-8x7B-Instruct-v0.1', token=hf_token)

            # Create an index from the documents
            index = SummaryIndex.from_documents(documents)

            # Create a query engine
            query_engine = index.as_query_engine(llm=llm)

            # Execute the query
            response = query_engine.query(query)
            
            # Display the response in a formatted way
            st.success("Query executed successfully!")
            if hasattr(response, 'response'):
                st.write("Response:", response.response)
            else:
                st.write("Response:", response)

        except Exception as e:
            st.error(f"An error occurred: {e}")

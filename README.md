
# Hugging Face Query App

A Streamlit application that allows users to query information from web pages using Hugging Face's language models and LlamaIndex. This app provides a user-friendly interface for inputting website URLs and querying specific information.

## Features

- **Hugging Face Authentication**: Easily authenticate with your Hugging Face account using a personal access token.
- **Dynamic URL Input**: Specify any website URL you want to query for information.
- **Query Submission**: Enter questions related to the website content and receive summarized responses.
- **User-Friendly Interface**: Built with Streamlit for easy navigation and interaction.

## Requirements

- Python 3.7 or later
- Streamlit
- Hugging Face Hub
- LlamaIndex
- Other dependencies installed via `requirements.txt`

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required packages**:

   Create a `requirements.txt` file with the following content:

   ```plaintext
   streamlit
   huggingface_hub
   llama-index
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run main.py
   ```

5. **Open your web browser** and navigate to `http://localhost:8501`.

## Usage

1. **Authenticate**: Upon launching the app, enter your Hugging Face token in the designated input field.

2. **Specify URL**: Enter the URL of the website you want to query.

3. **Enter Your Query**: Type your question in the query box.

4. **Submit Query**: Click the "Submit Query" button to retrieve the response.

5. **View Response**: The application will display the summarized response based on the content of the specified webpage.

## Example

- **Default URL**: `https://ohsl.us/projects/bcda`
- **Example Query**: "Explain about BCDA?"

### Screenshot

(Include a screenshot of your application here if available)

## Error Handling

If you encounter issues with token authentication, ensure that your Hugging Face token is correctly set as an environment variable or directly input in the app.

## Troubleshooting

- **Installation Issues**: Make sure all packages are installed in your active virtual environment.
- **Token Not Found**: Ensure your Hugging Face token is set correctly.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Special thanks to Hugging Face for their API and documentation.
- Thanks to the developers of LlamaIndex for creating a robust framework for document querying.

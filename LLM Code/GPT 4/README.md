# GPT-4 / GPT 3.5

This repository provides the script to summarize text using OpenAI's GPT-4 model via the ChatCompletion API.

## Prerequisites

- Python 3.7 or later
- An OpenAI API key

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/gpt4-text-summarizer.git
    cd gpt4-text-summarizer
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install openai
    ```

## Usage

1. Replace the placeholder in the script with your OpenAI API key:

    ```python
    openai.api_key = 'your-openai-api-key'
    ```

2. Use the following script to summarize text:

    ```python
    import openai

    def summarize_text(text):
        """
        Write your prompt.
        """
        openai.api_key = 'your-openai-api-key'

        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following issue thread: {text}"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
        )

        summary = response.choices[0].message['content']
        return summary

    # Input text
    text = """Original Issue Thread"""

    # Call function
    summary = summarize_text(text)
    print(summary)
    ```

3. Run the script:

    ```bash
    python summarize.py
    ```
### Replace the model name with GPT3.5 to use  GPT3.5 model.



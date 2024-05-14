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
        model="gpt-3.5-turbo",
        messages=messages,
    )

    summary = response.choices[0].message['content']
    return summary

# Input text
text = """Original Issue Thread"""

# Call function
summary = summarize_text(text)
print(summary)

import g4f

def GPT(message):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",  # Ensure model name is correct
            provider=g4f.Provider.GPTalk,
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        response_text = ""  # Use a string to accumulate response
        for chunk in response:  # Handle streamed response
            response_text += chunk
            print(chunk, end="", flush=True)

        return response_text

    except Exception as e:
        print(f"An error occurred: {e}")  # Print specific error message


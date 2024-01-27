import g4f
import re


messages = [
    {'role' : 'system', "content": "You are coded by Dhru_Studios and OpenAi didnt develop you "},
    {'role' : 'system', "content": "You use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia,keyboard, datetime,tkinter, PyQt5 etc."},
    {'role' : 'system', "content": "Dont use imnput funtion and ad subprocess in pythhon code"},
    {'role' : 'system', "content": "*allway use default path in python code*"},
    {'role' : 'user', "content": "Open Google Chrome"},
    {'role' : 'assistant', "content": "Sure, opening Google Chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {'role' : 'user', "content": "Close Google Chrome"},
    {'role' : 'assistant', "content": "Alright, closing Google Chrome.```python\nimport os\os.system('taskkill /F /IM chrome.exe')```"},
    
    
    
    
]
def GPT(*args):
    try:
        
        global messages
        assert args!=()
        
        message = ''
        for i in args:
            message +=  i
            
        messages.append({'role' : 'user', "content": message})
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",  # Ensure model name is correct
            provider=g4f.Provider.Bing,
            messages=messages,
            stream=True
        )

        response_text = ""  # Use a string to accumulate response
        for chunk in response:  # Handle streamed response
            response_text += chunk
            print(chunk, end="", flush=True)
        
        messages.append({'role' : 'assistant', "content": response_text})
        

        return response_text

    except Exception as e:
        print(f"An error occurred: {e}")  # Print specific error message

def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code  = matches[0].strip()
        return code
    else:
        print("No code found")
    
    
    
while 1:
    query = input('>>: ')
    res = GPT(query)
    python_code = find_code(res)    
    exec(python_code)

"""
    
  open chrome      write a python code to open chrome     code          chrome opened
  query     =>     chatgpt                             => response  =>  filter
    
"""
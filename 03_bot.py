import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(api_key="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",
                base_url = "https://openrouter.ai/api/v1")
def is_last_message_from_sender(chat_log,sender_name= "Lokesh Dhau"):
    # Splite the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True
    return False
    


# Click on the chrome icon at position (1295, 1050)
pyautogui.click(1295, 1050)

time.sleep(1)  # Adding a short delay to ensure the click registers

while True:
    time.sleep(5)
    # Drag the mouse from (674, 218) to (1871, 910) to select text
    pyautogui.moveTo(674, 218)
    pyautogui.mouseDown()  # Press and hold the left mouse button to start selection
    pyautogui.moveTo(1871, 910, duration=1)  # Drag to the ending position
    pyautogui.mouseUp()  # Release the mouse button to complete the selection

    # Copy the selected text to the clipboard using Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait for the clipboard to update
    pyautogui.click(728,387)

    # Retrieve the text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text (or store it in a variable for further use)
    print(chat_history)

    if is_last_message_from_sender(chat_history):   
        chat = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                
                    {"role": "system", "content": "you are a person named is Lakshya who speaks hindi as well as english. you are from from India and you are a commedian. you analyze chat historyand respond like Lakshya. Output should be the next chat response (text message only)"},
                    {"role": "user", "content": chat_history}
                
            ]
        )

        response = chat.choices[0].message.content
        pyperclip.copy(response)


        # step 5: click at coordinates (1066,960)
        pyautogui.click(1066,960)
        time.sleep(1) # wait for 1 second to ensure the click is registered

        #step 6: Paste the text
        pyautogui.hotkey('ctrl','v')
        time.sleep(1) # wait for 1 second to ensure the paste command is completed

        # step 7: Press Enter
        pyautogui.press('enter')
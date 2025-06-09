import os

def send_notification(title, message):
    os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')

# Test it
send_notification("VS Code Test", "This is a test alert while running Python in VS Code.")

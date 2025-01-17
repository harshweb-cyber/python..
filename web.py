import requests
import webbrowser
import os

# Start a session
session = requests.session()

# URL and login data
url = "https://www.hackthissite.org/"
login_url = "https://www.hackthissite.org/index.php"

# Login credentials
data = {
    "username": "gamera",
    "password": "38378q",
    "btn_submit": "Login"
}

# Attempt login
response = session.post(login_url, data=data)

# Check if login was successful
if "Login failed" in response.text:
    print("Login failed. Please check your credentials.")
else:
    print("Login successful.")

    # Save the response to a local file
    file_path = os.path.abspath("file.html")
    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"File saved at: {file_path}")

    # Open the file in a web browser
    webbrowser.open(f"file://{file_path}")

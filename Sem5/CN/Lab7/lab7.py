import requests
import os


def request_file_from_server(file_name):
    url = f"http://localhost:8000/{file_name}"
    response = requests.get(url)
    if response.status_code == 200:
        save_path = os.path.join("saved", file_name)
        directory = os.path.dirname(save_path)
        os.makedirs(directory, exist_ok=True)
        with open(save_path, "w") as f:
            f.write(response.text)
        print(f"File saved to {save_path}")
    else:
        print(f"Error: {response.status_code} - File not found.")


file_name = input("Enter the file name you want to request: ")
if file_name:
    request_file_from_server(file_name)

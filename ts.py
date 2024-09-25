import os
import time
import uuid
import requests

def generate_key():
    return str(uuid.uuid4())

def check_approval(key):
    url = "https://github.com/azlanshahid94/T/blob/main/aprvl.txt"  # Replace with actual URL
    response = requests.get(url)
    approved_keys = response.text.splitlines()
    return key in approved_keys

def main():
    key = generate_key()
    print("Please send the following key to the owner for approval:", key)
    
    approval_status = check_approval(key)
    if approval_status:
        print("Approved! Tool running...")
        print('Follow My Whatsapp Channel For More Updates')
        os.system('xdg-open (google.com)')
        time.sleep(5)
        os.system('chmod 777 POST64; ./POST64')
    else:
        print("Access denied!")

if __name__ == "__main__":
    main()

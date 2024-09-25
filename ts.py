
import os
import time
import uuid
import requests
import pywhatkit

def generate_key():
    return str(uuid.uuid4())

def check_approval(key):
    url = "(https://github.com/azlanshahid94/T/blob/main/aprvl.txt)"
    response = requests.get(url)
    approved_keys = response.text.splitlines()
    return key in approved_keys

def send_key_via_whatsapp(key, phone_number):
    pywhatkit.sendwhatmsg_instantly(phone_number, f"Key: {key}")

def main():
    key = generate_key()
    print("Please send the following key to the owner for approval:", key)
    
    # Send key via WhatsApp
    phone_number = "+1234567890"  # Replace with your WhatsApp number
    send_key_via_whatsapp(key, phone_number)
    
    approval_status = check_approval(key)
    if approval_status:
        print("Approved! Tool running...")
        print('Follow My Whatsapp Channel For More Updates')
        os.system('xdg-open (link unavailable)')
        time.sleep(5)
        os.system('chmod 777 POST64; ./POST64')
    else:
        print("Access denied!")

if __name__ == "__main__":
    main()

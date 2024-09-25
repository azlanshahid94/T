import os
import time
import uuid
import requests

def generate_key():
    return str(uuid.uuid4())

def check_approval(key):
    url = "(https://github.com/azlanshahid94/T/blob/main/aprvl.txt)"
    response = requests.get(url)
    approved_keys = response.text.splitlines()
    return key in approved_keys

def main():
    key = generate_key()
    print("Please send the following key to the owner for approval:", key)
    
    input("Press Enter to send key via WhatsApp...")
    
    # Open WhatsApp with predefined message
    phone_number = "+994409764173"  # Replace with your WhatsApp number
    whatsapp_url = f"(https://wa.link/lzmfbn): {key}"
    os.system(f'xdg-open {wa.link/lzmfbn}')
    
    approval_status = check_approval(key)
    if approval_status:
        print("Approved! Tool running...")
        print('Follow My Whatsapp Channel For More Updates')
        time.sleep(5)
        os.system('chmod 777 POST64; ./POST64')
    else:
        print("Access denied!")

if __name__ == "__main__":
    main()

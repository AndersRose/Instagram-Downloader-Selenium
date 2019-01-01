"""
This project as the aim to scrape all the photos from a instagram profile,
trying to emulate the normal human-browser interactions.
Please mind that the private scraping can potentialy block your account, so use
it at your own risk. I recommend you to get a dummy account.
Public profiles:
-You can minimaze the window, it will keep running on the background.
-Your credentials aren't necessary.
Private profiles:
-While the login process is doing, keep the windown open. After that point
you can close it.
-Your credentials are necessary.
"""

import instadown_public_function as insta_public
import instadown_public_function as insta_private
print("1-Donwload a public profile, not account necessary")
print("2-Downalod a private profile, requires your login credentials")
option=input("Select an option: ")
if option=="1":
    url=input("Insert the url you want to check: ")
    insta_public.download(str(url))
elif option=="2":
    username=input("Insert your instagram's user name: ")
    password=input("Insert your password: ")
    url=input("Insert the url you want to check: ")
    insta_private.download(url, username,password)

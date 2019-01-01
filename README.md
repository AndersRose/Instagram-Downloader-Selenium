# Insta_Downloader
## An instagram photo downloader that mimics human interactions to avoid ban.

---
This project aims to scrape all photos of an instagram profile,
trying to emulate the normal interactions of a human using a regular browser.
Please keep in mind that private scraping can potentially block your account, so use
at your own risk. I recommend you get a fictitious account.

### Public profiles:
- You can minimize the window, the program will keep running on the background. 
- Your credentials aren't necessary.

### Private profiles:
- While the login process is doing, keep the window open. After that point you can close it.
- Your credentials are necessary.

## Usage

Just open the main script. There you will find options for both public and private profiles.

## Requirements
- **Selenium** : A python controlled browser, wich enables to render webpages the same way a normal browser does. With this we spoof our bot as a normal user, using a regular browser. It also is useful for dynamic pages, where you need to wait a few seconds until the page loads for example.
- **Requests** : Used as a html fetching tool in this project, is necessary to extract the images after we adquire their url. This can be done using requests because by that time we aren't anymore on the instagram domain
- **Time**: This package is used to stop the program for a few seconds, in order to wait the webpages to load completely and javascript execute in its entirety.
- **Random**: With this package we are able to randomize a waiting time between key presses, wich mimicks the way a normal user writes.
- **Bs4** : A useful tool for html parsing. It identifies the images on a profile and returns the url.
### Installation
On terminal:
```
pip install -r requirements.txt

```
## Possible issues
You should change the chromedriver for the one you want. I'm using the firefox. 
If you are having problems or want to change the browser, go to the function files and change this:

```
driver= webdriver.Firefox()
```
to:

```
driver= webdriver.Chrome()
```
This selects the chrome browser instead firefox.
Visit their documentation:
https://selenium-python.readthedocs.io/

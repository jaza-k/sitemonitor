import requests
from bs4 import BeautifulSoup
import smtplib

# webpage to be scraped
URL = 'https://www.ebgames.ca/PS5/Games/877523/playstation-5-digital-edition#'
# set headers as if we are a browser
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

def check_availability():
    # fetches the webpage
    page = requests.get(URL, headers=headers)
    # parses the webpage in order to be able to fetch individual items
    soup = BeautifulSoup(page.content, 'html.parser')

    product = soup.find("a", {"class": "megaButton"}).get_text()

def send_mail():
    """Sends mail to specified address if conditions met."""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    # command sent by an email server to start the process of sending an email
    server.ehlo()
    # puts the SMTP server connection into TLS mode
    server.starttls()
    server.ehlo()
    # log in using the generated password
    server.login('jaza3373@gmail.com', 'khzleolfpjtwthox')

    # build e-mail content
    subject = 'Item is in stock!'
    body = 'Check https://www.ebgames.ca/PS5/Games/877523/playstation-5-digital-edition#'
    message = f"Subject: {subject}\n\n{body}"

    # command to perform the entire e-mail transaction
    server.sendmail(
        'jaza3373@gmail.com',
        'jaza-k@protonmail.com',
        message
    )

    print('E-MAILL SENT')

    server.quit()

check_availability()
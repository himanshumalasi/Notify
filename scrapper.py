import requests
from bs4 import BeautifulSoup
import smtplib
import time

def get_info(url,email,expected_price):
	#url = 'https://www.amazon.in/Wireless-Bluetooth-Reinforced-Microphone-Playback/dp/B07F984ZH2/ref=lp_1388921031_1_1_sspa?s=electronics&ie=UTF8&qid=1570443580&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXOTBFSFEyQTRFNyZlbmNyeXB0ZWRJZD1BMDY1MTk1NTMxR085UjZQTVI1TFQmZW5jcnlwdGVkQWRJZD1BMDIwNDE3OTJTUzhES1BFNUI0WkEmd2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3NlJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
	header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
	
	r = requests.get(url,headers=header)
	
	soup = BeautifulSoup(r.content,'html.parser')
	
	title = soup.find(id='productTitle').text.strip()
	price = soup.find(id='priceblock_ourprice').text.strip()[1:].replace(',','')
	price = float(price)

	if price < expected_price:
		send_mail(url,email)

def send_mail(url,email):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	# Enter Server Email and password

	server.login('<Enter Server Email>','<Enter your app password>')

	subject = "Price are down"

	body = f'Check the Amazon link the price of the item you enter are under expected price \n {url}'

	msg = f'Subject:{subject}\n\n{body}'
	server.sendmail(
		'himanshumalasi1998@gmail.com',
		email,
		msg
		)
	print("EMAIL has been sent")
	server.quit()

def main():
	url = input('Enter Url')
	email = input('Enter your Email to notify you')
	price = int(input('enter expected price'))
	while True:
		get_info(url,email,price)
		# Check after a day again
		time.sleep(60*60*24)

if __name__ == '__main__':
	main()
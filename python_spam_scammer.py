import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'outlook.com']
names = json.loads(open('names.json').read())
surnames = json.loads(open('surnames.json').read())
words = json.loads(open('words.json').read())

url = 'https://paypal-login79.com/extra/stockers/step1.php'

for i in range(101):
	name = random.choice(names).lower() + random.choice(surnames).lower()
	name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1,4)))
	email_domain = random.choice(email_domains)
	word = random.choice(names).lower()[:random.randint(2,8)] + str(random.choice(words))[:random.randint(2,8)]
	word_extra = ''.join(random.choice(chars) for i in range(random.randint(1,4)))

	username = name + name_extra + '@' + email_domain
	password = word + word_extra
	password2 = word + word_extra

	requests.post(url, allow_redirects=False, data={
		'EML': username,
		'PWD': password,
        'PWD2': password2
	})

	print(f'sending username: {username} and password1: {password} and password2: {password2}')
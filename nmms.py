from splinter import Browser
import time

def main():

	a = 0
	b = 0

	num = input('cuantos mensajes: ')
	num = int(num)

	while True:
		try:
			with Browser('chrome') as browser:
				for i in range(num):
					a += 1
					url = "victima"
					browser.visit(url)
					browser.find_by_tag('textarea').fill('mensaje')
					button = browser.find_by_id('Send').click()
					time.sleep(1)
					print(a)
					if a > num:
						break
		except AttributeError:
			b += 1
			print(b)
			pass
		if a > num:
			break

if __name__ == "__main__":
	main()

# brew install chromedriver
# pip install splinter
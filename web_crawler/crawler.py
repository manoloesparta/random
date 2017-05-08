import urllib2
try:
	request = raw_input("DIME UNA PAGINA: ")
	respuesta = urllib2.urlopen(request)
	pagina = respuesta.read()
	print escanear()
except:
	print("ESA PAGINA NO EXISTE, TONTO")

def escanear(total = '',final = '',num = 0):
	while True:
		url = pagina.find('href="', len(total))
		final_url = pagina.find('"', url + 6)
		total = total + '\n' + pagina[url:final_url]
		if url == -1 or final_url == -1:
			return '\n'.join(set(total.split('href="')))
			break
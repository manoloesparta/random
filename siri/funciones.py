# -*- coding: utf-8 -*-
def mes(today):
	if today[1] == "01":
		today[1] = "Enero"
	elif today[1] == "02":
		today[1] = "Febrero"
	elif today[1] == "03":
		today[1]= "Marzo"
	elif today[1] == "04":
		today[1] = "Abril"
	elif today[1] == "05":
		today[1] = "Mayo"
	elif today[1] == "06":
		today[1] = "Junio"
	elif today[1] == "07":
		today[1] = "Julio"
	elif today[1] == "08":
		today[1] = "Agosto"
	elif today[1] == "09":
		today[1] = "Septiembre"
	elif today[1] == "10":
		today[1] = "Octubre"
	elif today[1] == "11":
		today[1] = "Noviembre"
	elif today[1] == "12":
		today[1] = "Diciembre"

def reloj(hora):
	if hora[0] == "13":
		hora[0] = "01"
	elif hora[0] == "14":
		hora[0] = "02"
	elif hora[0] == "15":
		hora[0] = "03"
	elif hora[0] == "16":
		hora[0] = "04"
	elif hora[0] == "17":
		hora[0] = "05"
	elif hora[0] == "18":
		hora[0] = "06"
	elif hora[0] == "19":
		hora[0] = "07"
	elif hora[0] == "20":
		hora[0] = "08"
	elif hora[0] == "21":
		hora[0] = "09"
	elif hora[0] == "22":
		hora[0] = "10"
	elif hora[0] == "23":
		hora[0] = "11"
	else:
		return 'am'

'''def existe_internet():
	import urllib2
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False'''
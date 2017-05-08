# -*- coding: utf-8 -*-
def date():
	import datetime
	from math import floor
	from funciones import mes
	from funciones import reloj

	today = str(datetime.date.today()).split('-',2)

	mes(today)

	print "\n" + today[1]+" "+today[2]+" del "+today[0]

	hora = str(datetime.datetime.now().time()).split(':',2)
	don = 'pm'

	if reloj(hora) == None:
		print hora[0] +":"+ hora[1] + don
	else:
		print hora[0] +":"+ hora[1] + str(reloj(hora))
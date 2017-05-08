# -*- coding: utf-8 -*-
import funciones
import date
import contactos
import send
import calculadora

print '\nHola usuario'
date.date()

while True:

	print "\n1. Contactos"
	print "2. Email"
	print "3. Calculadora (Beta)"
	print "4. Fecha y hora"
	print "5. Salir"
	
	respuesta = raw_input("\nQue quieres hacer: ")
	respuesta = int(respuesta)

	if respuesta == 1:
		print "\nCONTACTOS"
		contactos.contacts()
	elif respuesta == 2:
		print "\nEMAIL"
		send.mandar()
	elif respuesta == 3:
		print "\nCALCULADORA (BETA)"
		calculadora.calcular()
	elif respuesta == 4:
		date.date()
	elif respuesta == 5:
		break
	#elif respuesta == 6:
		#internet = funciones.existe_internet()
	else:
		print "\nEsa opcion no esta disponible"

print "\nAdios popo\n"
# -*- coding: utf-8 -*-
def calcular():
	while True:
		print "\n1. Entrar a calculadora"
		print "2. Salir de calculadora"

		respuesta = raw_input("\nQue quieres hacer: ")
		respuesta = int(respuesta) #agregar try, except, break cuando se termine este

		if respuesta == 1:
			print "\nNo escribas espacios entre numeros y simbolos"
			operacion = raw_input("\nEscribe una operacion: ")

			existe_suma = False
			existe_multi = False
			existe_resta = False
			existe_div = False

			suma = 0
			resta = 0
			multi = 0
			div = 0
			resultado = 0

			if operacion.find("+") != -1:
				suma = operacion.find("+")
				existe_suma = True

			if operacion.find("-") != -1:
				resta = operacion.find("-")
				existe_resta = True

			if operacion.find("*") != -1:
				multi = operacion.find("*")
				existe_multi = True

			if operacion.find("/") != -1:
				div = operacion.find("/")
				existe_div = True

			if (existe_suma and existe_resta) or (existe_suma and existe_multi) or (existe_suma and existe_div) or (existe_resta and existe_multi) or (existe_resta and existe_div) or (existe_multi and existe_div):
				print "\nExisten mas de 1 operacion"

			elif not existe_resta or not existe_multi or not existe_div:
				resultado = float(operacion[suma-1]) + float(operacion[suma+1])

			elif not existe_suma or not existe_multi or not existe_div:
				resultado = float(operacion[resta-1]) - float(operacion[resta+1])

			elif not existe_suma or not existe_resta or not existe_div:
				resultado = float(operacion[multi-1]) * float(operacion[multi+1])

			elif not existe_suma or not existe_resta or not existe_div:
				resultado = float(operacion[div-1]) / float(operacion[div+1])

			if resultado != 0:
				print "\n" + str(resultado)

		elif respuesta == 2:
			break
		else:
			print "\nNo tengo esa opcion"
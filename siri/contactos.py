# -*- coding: utf-8 -*-
def contacts():
	while True:
		print "\n1. Ver contactos"
		print "2. Registrar un nuevo contacto"
		print "3. Salir de contactos"
		hacer = raw_input("\nQue quieres hacer: ")
		hacer = int(hacer)

		if hacer == 1:

			archivo = open("gente.txt","r")

			contactos = archivo.read()
			contactos = contactos.split("_")
			del contactos[-1]

			i = 0
			while i < len(contactos):
				contactos_beta = contactos[i].split("-")
				print "\n"+str(contactos_beta[0])+" "+str(contactos_beta[1])+" "+str(contactos_beta[2])+" "+str(contactos_beta[3])
				i = i + 1

			archivo.close()

		elif hacer == 2:

			print("\nDame los datos de tu contacto:\n")

			nombre = raw_input("Nombre: ")
			apellido = raw_input("Apellido: ")
			email = raw_input("Email: ")
			celular = raw_input("Celular: ")

			archivo = open("gente.txt","a")
			archivo.write(nombre+"-"+apellido+"-"+email+"-"+celular+"_")
			archivo.close()

			print"REGISTRADO"

		elif hacer == 3:
			break
		else:
			print "\nNo tengo esa opcion\n"
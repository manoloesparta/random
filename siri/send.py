# -*- coding: utf-8 -*-
def mandar():
	while True:
		print "\n1. Mandar un correo"
		#print "2. Ver correos"
		print "2. Salir de Email"

		respuesta = raw_input("\nQue quieres hacer: ")
		try:
			respuesta = int(respuesta)
		except:
			break

		if respuesta == 1:

			import smtplib

			print "\n1. Outlook/Hotmail"
			print "2. Yahoo"

			respuesta_inception = raw_input("\nQue tipo de correo vas a usar: ")
			respuesta_inception = int(respuesta_inception)

			if respuesta_inception == 1:
				smtpserver = "smtp-mail.outlook.com"
			elif respuesta_inception == 2:
				smtpserver = "smtp.mail.yahoo.com"

			correo = smtplib.SMTP(smtpserver, 587)
			correo.ehlo()
			correo.starttls()

			usuario = raw_input("\nCual es tu correo: ")
			contra = raw_input("Cual es tu contraseña: ")

			try:
				correo.login(usuario, contra)

				receptor = raw_input("\nDestinataro: ")
				mensaje = raw_input("Mensaje: ")
					
				correo.sendmail(usuario, receptor)

				correo.quit()
				
			except SMTPAuthenticationError:
				print "\nContraseña incorrecta"

		elif respuesta == 2:
			break

		else:
			print "No tengo esa opcion"
'''
if respuesta == 2:

	import imapclient

	print "\n1. Outlook/Hotmail"
	print "2. Yahoo"

	respuesta_inception = raw_input("Que tipo de correo vas a usar: ")
	respuesta_inception = int(respuesta_inception)

	if respuesta_inception == 1:
		imapserver = "imap-mail.outlook.com"
	elif respuesta_inception == 2:
		imapserver = "imap.mail.yahoo.com"

	correo = imapclient.IMAPClient(imapserver, ssl=True)

	usuario = raw_input("Cual es tu correo: ")
	contra = raw_input("Cual es tu contraseña: ")

	try:
		correo.login(usuario, contra)
'''


from instabot import Bot 

#@uthor: backup_python.dev

bot = Bot() 
bot.login(username = "tu_usuario", 
		password = "tu_contraseña") 

caption="""
No olvides seguirme como @backup_python.dev para mas contenido 
como este.
PD: Esta imagen fue subida desde python para el siguiente POST
.
.
.
.
#python3#pythonlove#linux#pythoncode#programmer#programmers
#indiaprogrammers#developers#meme#pythontutorial#programmerlife#
#stackoverflow#programming#webdeveloper#pythonprojects#USA#india
"""
photo="meme.jpg" # Solo imagenes .jpg 

bot.upload_photo(photo, 
				caption =caption) 

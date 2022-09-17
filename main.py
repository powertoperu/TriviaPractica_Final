BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import time
# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = 0

iniciar_trivia=True #Iniciamos la variable con True
intentos=0 # variable que alamacenara el numero de veces que el usuario intenta nuestra trivia 
while iniciar_trivia==True: #Mientras inicia la trivia sera True 
  intentos+=1
  puntaje=0
  # Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
  print ("Bienvenid@ a mi trivia sobre computación")
  print ("Pondremos a prueba tus conocimientos")
  print("Tienes", puntaje, "puntos")
  print("\n Intento número:",intentos)
  print("Presiona ENTER para continua")  
  # Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
  nombre = input("Ingresa tu nombre: ")

  # Es importante dar instrucciones sobre cómo jugar:
  # Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
  print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
  
  # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
  print("Primera pregunta\n")
  time.sleep(1)
  # Pregunta 1
  print (BLUE+"1) ¿Quién fue el creador de windows?"+RESET)
  print ("a) Linus Torvalds")
  print ("b) Bill Gates")
  print ("c) Mark Zuckerberg")
  print ("d) Dennis Ritchie")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d","p"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "a":
    puntaje -= 10
    print("Incorrecto", nombre, "!")
  elif respuesta_1 == "b":
    puntaje += 10
    print("Muy bien", nombre, "!")
  elif respuesta_1 == "c":
    puntaje -=10
    print("Incorrecto",nombre,"!")
  elif respuesta_1=="p":
    puntaje+=1
    print("Respuesta secreta ganas un punto",nombre,"!")
  else:
    print("Incorrecto", nombre, "!")
    puntaje-=10
  print("Gracias",nombre,"tienes acumulado",puntaje,"puntos\n")

  print("Segunda pregunta")
  time.sleep(1)
  # Pregunta 2
  print (BLUE+"\n2) ¿Cual de estos lenguajes de programación es de más bajo nivel?"+RESET)
  print ("a) Python")
  print ("b) Java")
  print ("c) PHP")
  print ("d) Assembly")
  
  # Almacenamos la rspuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d","x"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    puntaje-=10
    print ("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
  elif respuesta_2 == "b":
    puntaje-=10
    print ("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
  elif respuesta_2 == "c":
    puntaje-=10
    print ("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
  elif respuesta_2=="x":
    puntaje+=1
    print("La respuesta es secreta",nombre,"tienes un punto por descubrirla")
  else:
    puntaje += 10
    print (GREEN+"Muy bien", nombre, "!")
  
  print ("Excelente,has obtenido", puntaje, "puntos"+RESET)
  print("\n¿Deseas intentar nuevamente la trivia?")
  repetir_trivia=input("Ingresa 'si' para repetir o cualquier tecla para finalizar:").lower()
  if repetir_trivia !="si": # != significa "distinto"
    print(YELLOW+f"\n Espero {nombre} que lo hayas pasado bien,hasta pronto!"+RESET)
    iniciar_trivia=False
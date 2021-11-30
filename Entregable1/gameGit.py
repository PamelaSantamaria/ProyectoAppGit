# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:02:28 2021

@author: PamSH
"""
import time
import os
from Question import Question

print("Bienvenidx a GitGame!\n")
name=input("¿Podrías decirme tu nombre?\n")

unstod=1
while(unstod!=0):
    print("\n ¡Mucho gusto, " + name + "! Esta aplicación está diseñada para ayudarte a aprender Git de una manera eficiente y divertida.")
    print('''Antes de comenzar, quisiéramos dejar todo bien claro para que tengas una mejor experiencia:
          1-. Estamos aprendiendo, no nos juzgues si la app tiene muchos bugs:'c
          2-. Trabajaremos por niveles (próximamente), enseñándote desde lo más básico hasta lo avanzado.
          3-. Durante cada nivel tendrás pruebas que debes superar para pasar a los siguientes niveles.
          4-. Si necesitas ayuda, puedes pedir una pista o incluso la respuesta, pero recuerda que para aprender hay que intentar:)''')
    print("Todo claro, " + name + "?")
    unstod=int(input("Escribe '0' si no tienes dudas o '1' si necesitas más tiempo para leer\n"))
    if(unstod!=0):
        print("Tranquilx,  " + name + ", tómate el tiempo necesario para leer hasta entender<3")
        time.sleep(5)
       
os.system("cls")

print("\nOk, " + name + " a todo esto, ¿qué es Git?\n")
print('''Git es un sistema de control de versiones distribuido. Esto significa que un clon local del proyecto es un repositorio de control de versiones 
        completo. Estos repositorios locales plenamente funcionales permiten trabajar sin conexión o de forma remota fácilmente. Los desarrolladores 
        confirman su trabajo localmente y, a continuación, sincronizan su copia del repositorio con la copia en el servidor.''')

time.sleep(10)
print("\nTenemos una prueba para ti, estás listx, " + name + "?")
time.sleep(0.5)
questions_prompts = [
    "¿Qué es Git? \na: Un repositorio web \nb: Un entorno de desarrollo de Python \nc: Un sistema de control de versiones\n\n",
    "¿Dónde se sincroniza el clon del repositorio local? \na: En la computadora del vecino \nb: En los servidores de Git \nc: En una libreta\n\n",
    "Como desarrollador, ¿sirve conocer Git? \na: Nop \nb: Para nada \nc: Ninguna de las anteriores\n\n"
]

question_list = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
]

print("\nEscribe la letra que corresponda a la respuesta correcta\n")


def run_test(question_list):
        score = 0
        for question in question_list :
            ans = input(question.prompt)
            if ans.lower() == question.answer:
                print("Correcto!:D")
                score += 1
            else:
                print("Incorrecto:(")
        print("Tuviste " + str(score) + " de " + str(len(question_list))+ " preguntas correctas.\n")
        score=score   
        if score==3:
            print("¡Felicidades, " + name + "! Todas tus respuestas estuvieron correctas. Continúa con tu aprendizaje.")
        elif score<3:
            print("No tuviste todas las respuestas correctas, ¿quieres volver a intentarlo?\n")
    
run_test(question_list)


newchance=int(input("Escribe 1 si quieres volver a intentarlo, o 0 si quieres continuar\n"))
if newchance==1:
    run_test(question_list)
else:
    pass
time.sleep(0.5)
        
os.system("cls")
print("\nSecuencia Introductoria \n")
print("Hola de nuevo, " + name + ". Este es el primer nivel, donde veremos una breve introducción a la mayoría de los comandos de git \n")

print('''\n Empecemos con el subnivel 1: Commits de Git.\n
      Un commit en un repositorio git registra una captura de todos los archivos en tu directorio. Es como el viejo 'copy-paste', ¡pero mejorado!\n
      Git pretende mantener los commits tan ligeros como sea posible, por lo que no copia total e indiscriminadamente el directorio completo cada
      vez que haces un commit. Puede comprimir un commit como un conjunto de cambios entre una versión de tu repositorio y la siguiente\n
      Git mantiene un historial de qué commits se hicieron por quién y cuándo. Es por eso que la mayoría de los commits tienen commits precursores arriba suyo.
      En esta app, indicamos con flechas este flujo para una visualización más sencilla.\n 
      Hay un montón de cosas por saber, pero por ahora centrémonos en que los commits son 'capturas' de tu proyecto. Son livianos y cambiar de uno a otro es muy rápido.\n''')


os.system("cls")
time.sleep(4)      
print("¡Excelente, " + name + "! Ya sabes lo que son los commits, ahora comencemos con una pequeña prueba...\n")
print('''INSTRUCCIONES: Esta prueba es una Trivia, a diferencia de la prueba inicial, aquí si te daremos pistas o la respuesta si fallas tus intentos.\n
      Escribe la letra de la opción correcta, si necesitas una pista escribe 'P' o 'PISTA'.\n
      Pero cuidado, sólo tienes 3 pistas por juego. ¡Mucha suerte!\n''')

trivia_com = [
    {
        'question': '¿Qué podríamos decir que es un commit?',
        'options': ["Un algoritmo complicado", "Una instántanea o captura de mi proyecto", "Un apartado donde poner mi nombre de usuario", "Un espacio en el servidor local", "Una plataforma para ver las diferencias entre mi código y el de mi rival"],
        'answerIndex': 1,
        'hint': "Es como 'sacarle una foto' a tu trabajo"
    },
    {
        'question': '¿Por qué Git a veces no hace copias idénticas del repositorio?',
        'options': ["Porque es egoísta", "Porque Microsoft le cobra por cada archivo que se suba", "Porque trata que los commits pesen lo más poquito posible", "Porque el tráfico de datos propicia este tipo de comportamientos", "Porque tienen una API que realiza esto"],
        'answerIndex': 2,
        'hint': 'La respuesta es liviana como una pluma...'
    }
]

# Puntos
total_points = 0

# Pistas
hint = 0


#TODO: Agregar un while para repetir la pregunta cuando se pida una pista.
for t in trivia_com:

    options = '\n'.join(f'{chr(65 + i)}: {opt}' for i, opt in enumerate(t['options']))
    answer = input(t['question'] + '\n' + options + "\n\nTu respuesta: ").upper()

    if (ord(answer) - 65) == t['answerIndex']:
        print("Correcto!:D\n")
    elif answer == "P" or answer == "PISTA":
        hint += 1
        print(f"* {t['hint']}, {3 - hint} pista(s) restante(s). * \n")
        if hint > 3:
            print("Lo sentimos, has agotado tus pistas:'(.")
            continue
        
    else:
        print(f"Oops! Te equivocaste. La respuesta es {chr(65 + t['answerIndex'])}.\n")

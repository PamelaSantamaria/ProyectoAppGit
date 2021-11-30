# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:02:28 2021

@author: PamSH
"""
import time
import os
class Question:
    def __init__(self, prompt, answer):
        self.prompt= prompt
        self.answer= answer

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

print("\n Ok, " + name + " a todo esto, ¿qué es Git?\n")
print('''Git es un sistema de control de versiones distribuido. Esto significa que un clon local del proyecto es un repositorio de control de versiones completo. Estos repositorios locales plenamente funcionales permiten trabajar sin conexión o de forma remota fácilmente. Los desarrolladores confirman su trabajo localmente y, a continuación, sincronizan su copia del repositorio con la copia en el servidor.''')

questions_prompts = [
    "¿Qué es Git? \n(a) Un repositorio web \n(b) Un entorno de desarrollo de Python \n(c) Un sistema de control de versiones\n\n",
    "¿Dónde se sincroniza el clon del repositorio local? \n(a) En la computadora del vecino \n(b) En los servidores de Git \n(c) En una libreta\n\n",
    "Como desarrollador, ¿sirve conocer Git? \n(a) Nop \n(b) Para nada \n(c) Ninguna de las anteriores\n\n"
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
        
        
os.system("cls")
print("\nSecuencia Introductoria \n")
print("Hola de nuevo, " + name + ". Este es el primer nivel, donde veremos una breve introducción a la mayoría de los comandos de git \n")
print('''\n Empecemos con el subnivel 1: Commits de Git.
      Un commit en un repositorio git registra una captura de todos los archivos en tu directorio. Es como el viejo "copy-paste", pero mejorado;)
''')

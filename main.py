import Cat1
import Cat2
import Cat3
import Cat4
import Cat5
import Config


i=0
while (i<1):
    print('Bienvenido al juego de Preguntas y Respuesas!')
    print('¿Antes de emprezar deseas agregar una pregunta a la lista de preguntas? -->  Si (s), No (n)')
    config=input()
    if(config=='s'):
     Config.Configuracion()
    print('¿Deseas agregar otra pregunta?  -->  Si (s), No (n)')
    Res=input()
    if(Res=='s'):
        c=1;
    else:
        print('En colaboracion con SOFTKA TECNOLOGIES')
        print('Espera un momento!')
        print('Cargando.....')
        print('Empieza Ya!!')
        Decision=''
        Premio = 0
        PremioAcumulado = 0
        print('Ingresa tu nombre:   ')
        Nombre=input()
        Premio,Decision=Cat1.Pregunta(Nombre, Premio)
        if(Premio==0 or Decision=='s'):
            c=1
            print('Game Over :( ')
        else:
            Premio,Decision=Cat2.Pregunta2(Nombre, Premio)
            if(Premio==0 or Decision=='s'):
                c=1
                print('Game Over :( ')
            else:
                Premio,Decision=Cat3.Pregunta3(Nombre, Premio)
                if(Premio==0 or Decision=='s'):
                    c=1
                    print('Game Over :( ')
                else:
                    Premio,Decision=Cat4.Pregunta4(Nombre, Premio)
                    if(Premio==0 or Decision=='s'):
                        c=1
                        print('Game Over :( ')
                    else:
                        Premio,Decision=Cat5.Pregunta5(Nombre, Premio)
                        if(Premio==0 or Decision=='s'):
                            c=1


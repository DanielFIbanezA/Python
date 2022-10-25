#Este programa le imprime la informacion que el usuario quiera consultar. Se hace uso de un diccionario y de consultas para este proceso
person = {"name": "Alejandra", "gender": "female", "age": "24", "address": "Guaduales", "phone": "3203160700"}
ask = input("¿Que informacion quiere conocer?").lower()
#se utiliza la propiedad .lower() para convertir el string recibido por el usuario a todo minusculas para que no haya problema al hacer la consulta al diccionario
consulta =  person.get(ask, "Esta informacion no fue encontrada")
resultado = print("la informacion solicitada es : ", consulta )


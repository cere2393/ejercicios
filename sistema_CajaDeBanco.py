# #definir el diccionario para almacenar los valores por usuario
usuarios={}
# #definir datos de pruebas
usuarios["gustavo"]= 400.00
usuarios["carlos"]= 100.00

# def depositar():
#     nombre=input("introduce  el nombre del usuario")
#     monto=float(input("introduce el monto a depositar"))
#     usuarios[nombre] += monto

# print(usuarios)   
# depositar()    
# print (usuarios)


# usuarios=[]
# cuentas=[]

# usuario={"nombre":"Gustavo","estado":"A"}
# usuarios.append(usuario)



def depositar():
    nombre=input("introduce  el nombre del usuario")
    
   
    
    if nombre in usuarios:
        monto=float(input("introduce el monto a depositar"))
        usuarios[nombre]+=monto
        
    else:
       print(f"usuario {nombre} no existe")
       
       
def registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado.")
    else:
        usuarios[nombre_usuario]=0.00
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")            


def retirar():
    nombre=input("ingrese el nombre del usuario")
    
    if nombre in usuarios:
        retiro=float(input("ingrese el monto del retiro"))
        if retiro>usuarios[nombre]:
            print ("saldo insuficiente")
        else:    
            usuarios[nombre]-= retiro
    else:
        print ("usuario no existente")    



retirar()
print(usuarios)
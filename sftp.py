import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# Datos del Servidor:
ip = input('Ingrese ip del servidor: ')
user = input('Ingrese usuario: ')
passw = input('Ingrese contraseña: ')
port = int(input('Ingrese puerto: '))
# Programa:
with pysftp.Connection(ip, username=user, password=passw, port=port, cnopts=cnopts) as sftp:
    print("Conecction stablished")
    localpath = input('Ingrese ruta de su computadora, por ejemplo "C:/Users/" ')
    print(localpath)
    remotepath = input('Ingrese ruta del server remoto, por ejemplo "C:/server/" ')
    esta = sftp.listdir(remotepath)
    print(esta)
    sftp.get_d(remotepath,localpath)
    sftp.close()

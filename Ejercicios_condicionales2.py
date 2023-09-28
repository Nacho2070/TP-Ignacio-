entrada_fecha = input("Ingrese la fecha en formato 'día, DD/MM': ").lower()  # Convertir a minúsculas
datos_fecha = entrada_fecha.split(', ')
if len(datos_fecha) != 2:
    print("Error: Formato de fecha incorrecto.")
else:
    dia_semana, fecha_num = datos_fecha[0], datos_fecha[1]
    dia, mes = fecha_num.split('/')
    dia = int(dia)
    mes = int(mes)
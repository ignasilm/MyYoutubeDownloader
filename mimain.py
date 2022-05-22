import pytube


def progress_function(chunk,file_handle, bytes_remaining):
    print((float(bytes_remaining) / float(descarga.filesize)) * float(100),'%')


def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

print("Descarga videos de youtube a partir de la URL")
print("Introduce la URL del video que quieres descargar")

link = input("URL: ")

video = pytube.YouTube(link, on_progress_callback=progress_function)
#lista_opciones = video.streams.filter(file_extension='mp4')
lista_opciones = video.streams.order_by('resolution').desc()
print("")
print("Titulo del video: ", video.title )
print("Autor: ", video.author)
print("")
print("El video que has seleccionado tiene estas opciones de descarga:")
for opcion in lista_opciones:
    print(opcion)

print("")
itag = input("Introduce el 'itag' de la opcion que quieras descargar de las disponibles:")
descarga = video.streams.get_by_itag(itag)
print("")
print("Se va a descargar el video: ", descarga.default_filename)
print("El video a descargar tiene un tamaño de:", descarga.filesize_approx) 
print('FileSize : ' + str(round(descarga.filesize/(1024*1024))) + 'MB')
print("")
print("Empezamos la descarga, se paciente...")
descarga.download()
print("¡¡Descarga terminada!!")



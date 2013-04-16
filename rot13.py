# _*_ conding: utf-8 _*_


# Convertir la cadena en una list de valores
# @param string cadena
# @return list arr
# 
def strSplit(cadena):
  arr = []
	for iStr in range(0, len(cadena)):
		arr.append(cadena[iStr])
	return arr

#
# @param string string
# @return string cadena
#
def rot13(string):
	abc = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	arrAbs = strSplit(abc);
	char = cadena = ''
	metodo = (26 / 2)
	for char in strSplit(string):
		posChr = abc.find(char.upper())
		if posChr > 0:
			letra = (metodo + posChr) if posChr <= metodo else (posChr - metodo)
			newChr = arrAbs[letra]
			char = newChr.upper() if ord(newChr) > ord(char) else newChr.lower()
		cadena += char
	return cadena


# ----- Fin -------- 
print rot13(raw_input())

import math

def areaCirculo(radio):
	area= (radio**2) * math.pi
	return area

def main():
	radio=int(input("Ingrese el radio de la circunferencia: "))
	resp = areaCirculo(radio)
	print ("el area es: "+str(round(resp,3)))

main()
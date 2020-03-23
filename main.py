from imgsaver import GetImage
from datacrawler import datacrao

lista = GetImage('pb')
respostas = datacrao('paraiba','joao pessoa')
print(respostas[0])


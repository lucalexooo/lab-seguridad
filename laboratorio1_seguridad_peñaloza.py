import requests

def cifrado_vigenere(texto, clave):
    resultado = []
    clave_repetida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        if 'a' <= texto[i] <= 'z':
            offset = ord('a')
            resultado.append(chr(((ord(texto[i]) - offset + ord(clave_repetida[i]) - offset) % 26) + offset))
        elif 'A' <= texto[i] <= 'Z':
            offset = ord('A')
            resultado.append(chr(((ord(texto[i]) - offset + ord(clave_repetida[i]) - offset) % 26) + offset))
        else:
            resultado.append(texto[i])

    return ''.join(resultado)

def descifrado_vigenere(texto_cifrado, clave):
    resultado = []
    clave_repetida = clave * (len(texto_cifrado) // len(clave)) + clave[:len(texto_cifrado) % len(clave)]

    for i in range(len(texto_cifrado)):
        if 'a' <= texto_cifrado[i] <= 'z':
            offset = ord('a')
            resultado.append(chr(((ord(texto_cifrado[i]) - ord(clave_repetida[i]) + 26) % 26) + offset))
        elif 'A' <= texto_cifrado[i] <= 'Z':
            offset = ord('A')
            resultado.append(chr(((ord(texto_cifrado[i]) - ord(clave_repetida[i]) + 26) % 26) + offset))
        else:
            resultado.append(texto_cifrado[i])

    return ''.join(resultado)
def cifrado_rotn(texto, n):
    resultado = []
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            offset = ord('a')
            resultado.append(chr(((ord(caracter) - offset + n) % 26) + offset))
        elif 'A' <= caracter <= 'Z':
            offset = ord('A')
            resultado.append(chr(((ord(caracter) - offset + n) % 26) + offset))
        else:
            resultado.append(caracter)
    return ''.join(resultado)

def descifrado_rotn(texto_cifrado, n):
  
    return cifrado_rotn(texto_cifrado, -n)


mensaje = "hola mundo"


mensaje_rot15 = cifrado_rotn(mensaje,15)
print("Rot15:", mensaje_rot15)


mensaje_vigenere = cifrado_vigenere(mensaje_rot15, "cvqnoteshrwnszhhksorbqcoas")
print("Vigenere:", mensaje_vigenere)


mensaje_rot7 = cifrado_rotn(mensaje_vigenere, 7)
print("Rot7:", mensaje_rot7)


headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"ffxj bubgb"}' 

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)
print(response.text)

#desafio 2

headers = {
    'Content-Type': 'text/plain',
}

response2 = requests.get('http://finis.malba.cl/GetMsg', headers=headers)
print(response2.text)

import json


mensaje_dire = response2.text


mensaje_obj = json.loads((mensaje_dire))


mensaje1 = mensaje_obj["msg"]


print(mensaje1)
message_dire2=descifrado_rotn(mensaje1,7)
message_dire3=descifrado_vigenere(message_dire2,"aobkqolrzsrigpknkufezioer")
message_dire4=descifrado_rotn(message_dire3,15)
print(message_dire4)
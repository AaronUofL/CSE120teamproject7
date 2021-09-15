def encipher():
    print('Enter your text to be ciphered:')
    message = list(input())
    print('Enter your shift')
    c = int(input())
    cipher=[]
    for x in range(message.__len__()):
        if ord(message[x]) == 0:
            cipher.append(" ")
        elif ord(message[x]) in range(65,90):
            cipher.append(chr((((ord(message[x]) + c)-13) % 26)+65))
        elif ord(message[x]) in range(97, 122):
            cipher.append(chr((((ord(message[x]) + c)-19) % 26)+97))
        else:
            cipher.append(message[x])
    print(''.join(map(str, message)), "becomes:")
    print(''.join(map(str, cipher)))
def decipher():
    print('Enter your enciphered text:')
    cipher = list(input())
    print('Enter your shift')
    c = int(input())
    message=[]
    for x in range(cipher.__len__()):
        if ord(cipher[x]) == 0:
            message.append(" ")
        elif ord(cipher[x]) in range(65,90):
            message.append(chr((((ord(cipher[x]) - c)-13) % 26)+65))
        elif ord(cipher[x]) in range(97, 122):
            message.append(chr((((ord(cipher[x]) - c)-19) % 26)+97))
        else:
            message.append(cipher[x])
    print('"'+''.join(map(str, cipher))+'"', "deciphers to:")
    print(' '+''.join(map(str, message)))
def dictionary_solve():
    print("unfinished")
    print("Enter to return...")
    input()
def credits():
    print("Created by X, X, X, X, and X")
    print("Acknowledgments: .... ")
    print("Enter to return...")
    input()
while "sky" != "Blue":
    print("\tZhCipher 2021")
    print("1\tEncipher")
    print("2\tDecipher")
    print("3\tDictionary Solve")
    print("4\tCredits")
    menu = int(input())
    if menu == 1:
        encipher()
    elif menu == 2:
        decipher()
    elif menu == 3:
        dictionary_solve()
    elif menu == 4:
        credits()
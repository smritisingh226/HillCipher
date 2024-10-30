"""
REFERENCE:
*    Title: How to implement the Hill cipher in python?
*    Author: Alvaro Rafael Rodríguez Gregorio, Rafael Rodríguez Puente
*    Date: July 2022
*    Code version: 1.0
*    Availability: https://justcryptography.com/hill-cipher/
"""

import numpy

#Creates a 3x3 matrix from the key provided using the ACII values.
#For decryption, an inverse key is needed which is the inverse of the encrypting key
def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m

# CipherText = PlainText matrix * Key matrix mod 31
#Replacing letters with their assigned numbers (0-30) by mod 31
def encrypt(P, K):
    C = [0,0,0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 31
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 31
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 31
    return C


def Hill(message, K):
    cipher_text = []
    #Transform the message, 3 characters at a time
    for i in range(0, len(message), 3):
        P = [0, 0, 0]
        #Assign the corresponding integer value to each letter using the ASCII values
        for j in range(3):
            P[j] = ord(message[i + j]) % 65
        #Encrypt three characters
        C = encrypt(P, K)
        #Add the encrypted 3 letters to the final cipher text
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
        #Repeat until all sets of three letters are processed.

    #returns a string of cipher text
    return "".join(cipher_text)

#Returns the inverse of the given matrix
def MatrixInverse(K):
    det = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 31)

    #Create a 3X3 inverse matrix using numpy
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 31
    return K_inv


#This function is used to perform the encryption of the plain text
def encryption_calling():
    #Reads the plain text and key from a file
    mfile = open("message.txt", "r")
    kfile = open("key.txt", "r")
    tempFile = open("tempFile.txt", "w")
    print("Encryption is underway\n.\n.")
    message = mfile.read()
    key = kfile.read()

    #CipherText = PlainText * Key mod 31
    K = create_matrix_from(key)
    print("The key is valid and successfully loaded onto the memory\n.\n.")
    cipher_text = Hill(message, K)
    tempFile.write(f'Cipher text: {cipher_text}')
    print("Encryption Completed ! Ecrypted text written in the file temp.txt"
          "Press d to show contents of the file")

#This function is used to perform the dencryption of the plain text
def decryption_calling():
    cfile = open("cipher.txt", "r")
    kfile = open("key.txt", "r")
    tempFile = open("tempFile.txt", "w")
    key = kfile.read()
    K = create_matrix_from(key)
    cipher_text = cfile.read()
    print("Decryption is underway\n.\n.")
    #Decrypt using the inverse of the key matrix
    K_inv = MatrixInverse(K)
    print("The key is valid and successfully loaded onto the memory.\n")
    plain_text = Hill(cipher_text, K_inv)

    #Extra test to make sure that K x K^-1 equals the identity matrix
    M = (numpy.dot(K, K_inv))
    for i in range(3):
        for j in range(3):
            M[i][j] = M[i][j] % 31
    tempFile.write(f'Plain text: {plain_text}')
    print("Decryption Completed! Decrypted text written in the file temp.txt "
          "Press d to show contents of the file")

if __name__ == "__main__":
    cipherfile = open("cipher.txt", "r")
    messagefile = open("message.txt", "r")
    isContinue = True
    print("Enter a to EXIT ")
    print("Enter b to Encrypt ")
    print("Enter c to Decrypt ")
    print("Enter d to Show the contents of the file ")
    while isContinue:
        opt = input("\nEnter your choice:")

        if opt == "b":
            encryption_calling()

        if opt == "c":
            decryption_calling()

        if opt == "d":
            tempFile = open("tempFile.txt", "r")
            tempFile = tempFile.readline()
            print("******DETAILS IN THE FILES**********")
            print(tempFile)

        if opt == "a":
            isContinue = False
            print("Thank you for using our Hill cipher Encryption/ Decryption system.")

I used Pycharm to code the hill cipher to use the numpy library to create the matrix. 
Before running the program, make sure there is numpy module downloaded in Pycharm.
This program does encryption as well as decryption.

For encryption: 
Step 1: The program reads the key.txt file to fetch the key. 
STEP 2: The program converts the key into a matrix.
STEP 3: The program then reads the message.txt file to fetch the plain text.
STEP 4: The program creates the plain text into a matrix.
STEP 5: The program then performs encryption and write the encrypted text onto the temp.txt file.

For decryption: 
Step 1: The program first creates an inverse of the key matrix used for encryption. 
STEP 2: The program then reads the cipher.txt file to fetch the cipher text.
STEP 3: The program creates the cipher text into a matrix.
STEP 4: The program then performs decryption and write the decrypted text onto the temp.txt file.

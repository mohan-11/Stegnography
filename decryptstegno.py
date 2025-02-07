import cv2

img = cv2.imread("encryptedImage.jpg")  

pas = input("Enter passcode for Decryption: ")

password = "12345"  


d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)


if password == pas:
    message = ""
    n = 0
    m = 0
    z = 0
   
    for i in range(len(img)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED TO DECRYPT")

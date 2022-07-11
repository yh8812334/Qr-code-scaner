import pyzbar.pyzbar as pyzbar  # pip install pyzbar
import numpy as np  # pip install numpy
import cv2  # pip install opencv-python
from ff3 import FF3Cipher

def ff3_decrypt(ciphertext):
    key = "2DE79D232DF5585D68CE47882AE256D6"
    tweak = "CBD09280979564"
    c = FF3Cipher(key, tweak, radix=62)
    decrypted = c.decrypt(ciphertext)
    print(f"{ciphertext} -> {decrypted}")
    return decrypted

# QR코드 탐지하는 함수
def decode(im):
    #QR코드 찾기
    decodedObjects = pyzbar.decode(im)
    #크기가 작은 Qr코드는 인식하지 못함.
    if len(decodedObjects) == 0:
        print("QR Code not found.")


    # 결과 출력
    for obj in decodedObjects:
        print('Type : ',  ' QR Code ')
        print('Data : ', obj.data)  # 데이터 읽은 값

        qr_data=str(obj.data)[2:].replace("'","") # 데이터 복호화 할 수 있게 가공
        # print(qr_data)

        plaintext=ff3_decrypt(qr_data) # 복호화

    return decodedObjects

# Display barcode and QR code location
def display(im, decodedObjects):
    # Loop over all decoded objects

    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im);
    cv2.waitKey(0);


# Main
if __name__ == '__main__':
    # Read image
    im = cv2.imread(input("input : "))

    decodedObjects = decode(im)
    display(im, decodedObjects)

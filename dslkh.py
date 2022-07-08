import pyzbar.pyzbar as pyzbar  # pip install pyzbar
import numpy as np              # pip install numpy
import cv2                      # pip install opencv-python

def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    if len(decodedObjects) == 0:
        print("QR code not found.")
    # print(len(decodedObjects))

    # Print results
    for obj in decodedObjects:  # type: object
        print('Type : ', 'QR Code' )
        print('Data : ' , obj.data, )

    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):
    # Loop over all decoded objects

    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], =np.float32))
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
    im = cv2.imread('zxcv.png')

    decodedObjects = decode(im)
    display(im, decodedObjects)
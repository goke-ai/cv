import sys
import cv2 as cv
import matplotlib.pyplot as plt

print("commandline argument array \n", sys.argv)
print()
print("first argument: ", sys.argv[0])

if len(sys.argv) >= 3:
    print("second argument: ", sys.argv[1])
    print("third argument: ", sys.argv[2])


    filePath = sys.argv[1]

    # read image file
    img = cv.imread(filePath)

    # check if file found
    if img is None:
        sys.exit("Could not read the image.")

    # display file
    cv.imshow("Display window", img)

    # pause execution here by waiting for a user to press a key
    k = cv.waitKey(0)

    # if user typed s save file as PNG file
    if k == ord("s"):
        cv.imwrite("test.png", img)

    cv.destroyAllWindows()



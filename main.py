import cv2
import numpy as np
from PIL import *
from sklearn.cluster import KMeans
from collections import Counter
from matplotlib import pyplot as plt

def find_bear(path):
    img = cv2.imread(path)
    img_median = cv2.medianBlur(img, 5)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img_median, cv2.COLOR_BGR2HSV)
    img_hsv = img_hsv[:,:,0]
    # cv2.imshow('pic', img_hsv)

    # img_hsv[0] = 110

    # _, thr = cv2.threshold(img_hsv, 0, 255, cv2.THRESH_OTSU)
    thr = cv2.adaptiveThreshold(img_hsv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 30)

    # cv2.imshow('pic', thr)

    def get_domination_color(image, k=1):
        image = image.reshape((image.shape[0] * image.shape[1], -1))

        clt = KMeans(n_clusters=k)
        labels = clt.fit_predict(image)

        label_counts = Counter(labels)

        dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

        return list(dominant_color)

    is_bear_founded = False
    count = 0
    # while not is_bear_founded:
    while count <= 15:
        h = 50
        w = 50
        position = np.unravel_index(np.argmax(thr), thr.shape)
        y = position[0] - 25
        x = position[1] - 25
        # cv2.rectangle(thr, (x, y), (x + w, y + h), (0, 0, 0), -1)

        thr_crop = thr[y:y+50, x:x+50]




        color = get_domination_color(thr_crop)
        print(color)

        count = 16

        count+=1
        is_bear_founded = True

    cv2.imshow('pic', thr_crop)
    # plt.imshow(thr_crop)
    # plt.show()







    # light_orange = (50, 10, 20)
    # dark_orange = (60, 20, 80)
    # mask = cv2.inRange(thr, (0, 0, 0), (100, 100, 100))
    # cv2.imshow('pic',mask)

    # position = np.unravel_index(np.argmax(thr), thr.shape)
    # print(position)
    # закрашивать часть
    # y = position[0] - 100
    # x = position[1] - 100
    # h = 200
    # w = 200
    # crop = img_RGB[y:y + h, x:x + w]
    # print(position)
    #
    # cv2.rectangle(img_RGB, (x, y), (x + w, y + h), (0, 255, 255), 10)
    # plt.imshow(img_RGB)
    # plt.show()

    cv2.waitKey(0)



find_bear('D:/Projects/Python/PolarBear/img/test.png')

# bear_bgr = cv2.imread('img/test.png')
#
# # bear_bgr_blurred = cv2.blur(bear_bgr, (9, 9))
# # bear_hsv_blurred = cv2.cvtColor(bear_bgr_blurred, cv2.COLOR_BGR2HSV)
#
# bear_bgr_median = cv2.medianBlur(bear_bgr, 5)
# bear_hsv_median = cv2.cvtColor(bear_bgr_median, cv2.COLOR_BGR2GRAY)
# _, thr = cv2.threshold(bear_hsv_median, 0, 255, cv2.THRESH_OTSU)  # подбирает автоматически
# # thr_adpt = cv2.adaptiveThreshold(bear_hsv_median, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 121, 25)
#
#
# cv2.imshow('picture1',bear_bgr[:,:,0])
# cv2.imshow('pic', thr)
# cv2.imwrite('test2.png',thr)
# # cv2.imshow('picture2', thr  )
# # cv2.waitKey(0)
# ## закрасить с помощью closexz


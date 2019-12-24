import rplidar
import numpy as np
import cv2
import math

# lidar = rplidar.RPLidar('/dev/cu.SLAB_USBtoUART')

# info = lidar.get_info()
# print(info)
# lidar.clear_input()

# health = lidar.get_health()
# print(health)

angles = np.zeros(360)
distances = np.zeros(360)

start_point = (200, 200)
image = np.zeros((400, 400, 3), np.uint8)

# while True:

# for i, angle in enumerate(lidar.iter_measurments()):
#     angles[int(angle[2])] = angle[2]
#     distances[int(angle[2])] = angle[3]
#     if i > 2000:
#         break

distances = np.loadtxt('lidar.txt')

for i in range(distances.size):
    dist = distances[i] / 1000 if distances[i] != 0 else 1

    end_x = math.asin(math.radians(angles[0])) / (dist)
    end_y = math.acos(math.radians(angles[0])) / (dist)

    end_point = [int(end_x), int(end_y)]
    print(end_point)
    image = cv2.line(image, start_point, tuple(end_point), (0, 255, 0), 5)
    cv2.imshow('test window', image)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

cv2.destroyAllWindows()

#
# lidar.stop()
# lidar.stop_motor()
# lidar.disconnect()

cv2.imshow('test window', image)
cv2.waitKey()

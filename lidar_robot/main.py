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

start_point = (1000, 1000)
image = np.zeros((2000, 2000, 3), np.uint8)

# while True:

# for i, angle in enumerate(lidar.iter_measurments()):
#     angles[int(angle[2])] = angle[2]
#     distances[int(angle[2])] = angle[3]
#     if i > 2000:
#         break
angles = np.array([i for i in range(360)])
distances = np.loadtxt('lidar.txt')

for i in range(distances.size):
    dist = distances[i] if distances[i] != 0 else 1

    end_x = math.sin(math.radians(angles[i])) * (dist)
    end_y = math.cos(math.radians(angles[i])) * (dist)

    end_point = [int(end_x), int(end_y)]
    print(angles[i], end_point)
    image = cv2.line(image, start_point, tuple(end_point), (0, 255, 0), 5)
    cv2.imshow('test window', image)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break



#
# lidar.stop()
# lidar.stop_motor()
# lidar.disconnect()

cv2.imshow('test window', image)
cv2.waitKey()
cv2.destroyAllWindows()

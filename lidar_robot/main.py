import rplidar
import numpy as np
import cv2

lidar = rplidar.RPLidar('COM6')

info = lidar.get_info()
print(info)
lidar.clear_input()

health = lidar.get_health()
print(health)

distance = np.zeros(360)

for i, angle in enumerate(lidar.iter_measurments()):
    distance[int(angle[2])] = angle[3]
    if i > 3000:
        break

np.savetxt('lidar.txt', distance)

cv2.imshow('test window', distance)
cv2.waitKey()
cv2.destroyAllWindows()


print(' '.join(str(i) for i in distance))

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
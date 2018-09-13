# pip install simple draw

import simple_draw as sd
start_point = sd.get_point(300, 10)
my_angle = 90
my_length = 200

vector = sd.get_vector(
    start_point = start_point, angle=my_angle, length=my_length, width=6)
vector.draw()

start_point_2 = vector.end_point
my_angle_2 = my_angle - 20
my_length_2 = my_length * .7

vector_2 = sd.get_vector(
    start_point = start_point_2, angle=my_angle_2, length=my_length_2, width=6)
vector_2.draw()

start_point_3 = vector.end_point
my_angle_3 = my_angle + 20
my_length_3 = my_length * .7

vector_3 = sd.get_vector(
    start_point = start_point_3, angle=my_angle_3, length=my_length_3, width=6)
vector_3.draw()

sd.pause()

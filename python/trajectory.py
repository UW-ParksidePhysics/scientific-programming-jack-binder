from math import pi, tan, cos

standard_gravity = 9.80665  # m/s/s
initial_velocity = 15.  # km/h
launch_angle = 60  # °
horizontal_range = 0.5  # m
initial_height = 1.0  # m

# print(f'v0    = {initial_velocity:.1f} km/h')
# print(f'theta = {launch_angle:.0f} °')
# print(f'x     = {horizontal_range:.1f} m')
# print(f'y0    = {initial_height:.1f} m')

# Convert initial velocity to m/s
initial_velocity = initial_velocity * 3600 / 1000
# Convert angle to radians
launch_angle = launch_angle * pi / 180


def calculate_height(horizontal_displacement, angle, starting_velocity, starting_height
                     , gravitational_acceleration=9.80665):
    """
    Calculates the height of a projectile path given initial conditions
    :param horizontal_displacement: Difference in horizontal position from start to end (in m)
    :param angle: float
        Launch angle (in rad)
    :param starting_velocity: float
        Launch velocity (in m/s)
    :param starting_height: float
        Launch height (in m)
    :param gravitational_acceleration:  float, optimal
        Acceleration due to gravity (in m/s^2)
    :return:
        height, float
        Maximum height of the projectile path
    """
    height = horizontal_displacement * tan(angle) \
             - 1 / (2 * starting_velocity ** 2) * gravitational_acceleration * horizontal_displacement ** 2 / (
                     (cos(angle)) ** 2) \
             + starting_height
    return height


gravitational_accelerations = [3.7, 8.9, 9.8]
for g in gravitational_accelerations:
    projectile_height = calculate_height(horizontal_range, launch_angle, initial_velocity, initial_height,
                                         gravitational_acceleration=g)
    # print(f'y(g={g:.1f} m/s^2)     = {projectile_height:.3f} m')

# from sys import argv
#
# for index, argument in enumerate(argv):
#     print(f'i, arg = {index}, {argument}')
#
#
# if len(argv) > 1:
# gravitational_acceleration = float(argv[1])
# gravitational_acceleration = float(input('Input acceleration due to gravity in m/s^2:'))

gravitational_accelerations = []
acceleration_data = open('gravitational_accelerations', 'r')
for line in acceleration_data:
    gravitational_accelerations.append(float(line))

print(gravitational_accelerations)

# initial_velocity = 1.0  # m/s
# time = 1.0  # sec
# final_velocity = initial_velocity + gravitational_acceleration * time
# print(f'v(t={time} s, g={gravitational_acceleration}) = {final_velocity:.2f} m/s')


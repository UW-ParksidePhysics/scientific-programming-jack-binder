from initial_conditions import set_initial_conditions
from Unit_Conversions import convert_units
from trajectory import calculate_height

Initial_Conditions = set_initial_conditions()
launch_angle = Initial_Conditions[2]
launch_angle = convert_units(launch_angle, 'degree', 'radian')

initial_velocity = Initial_Conditions[1]
initial_velocity = convert_units(initial_velocity, 'km.h', 'm/s')

projectile_height = calculate_height(Initial_Conditions[3],
                                     launch_angle,
                                     initial_velocity,
                                     Initial_Conditions[4])

print(f'y     = {projectile_height:.3f} m')
def convert_units(value, units_in, units_out):
    if units_in == 'degree' and units_out == 'radian':
        from math import pi
        converted_value = value * pi / 100
    elif units_in == 'km/h' and units_out == 'm/s':
        converted_value = 3600*value / 1000
    else:
        print(f'{units_in} to {units_out} unknown')
    return converted_value

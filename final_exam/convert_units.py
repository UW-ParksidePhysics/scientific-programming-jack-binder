def convert_units(value, units, desired_units=0):
    from scipy.constants import value as spvalue
    from scipy.constants import angstrom, giga
    if units == "cubic bohr/atom":
        value_in_desired_units = value * spvalue("Bohr radius")**3 / angstrom**3
    elif units == "rydberg/atom":
        value_in_desired_units = value * spvalue("Rydberg constant times hc in eV")
    elif units == "rydberg/cubic bohr":
        value_in_desired_units = value * spvalue("Rydberg constant times hc in J") / spvalue("Bohr radius")**3 / giga
    else:
        value_in_desired_units = value
    return value_in_desired_units


if __name__ == '__main__':
    print(convert_units(1, "cubic bohr/atom"))
    print(convert_units(1, "rydberg/atom"))
    print(convert_units(1, "rydberg/cubic bohr"))

# Name: Izzie Vazquez
# Assignment Name: 06 Prove Assignment: Troubleshooting Functions
# Assignment Description:
# Write the second half of the Python program to help an engineer design a water distribution system
# that you began in the previous lesson’s prove milestone. Also, write more test functions that will
# automatically verify that your program functions work correctly.

from pytest import approx
import pytest

rho = 998.2 # Density of water (kg/m³)

def water_column_height(tower_height, tank_height):
    """
    Calculates and returns the height of the water column (h) in meters.
    Formula: h = t + (3w / 4)
    """
    h = tower_height + (3 * tank_height / 4)
    return h

def pressure_gain_from_water_height(height):
    """
    Calculates and returns the pressure (P) from water height in kPa.
    Formula: P = (p * g * h) / 1000
    """
    g = 9.80665 # Acceleration due to gravity (m/s²)
    P = (rho * g * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates and returns the pressure loss (P) due to pipe friction in kPa.
    Formula: P = - (f * L * p * v²) / (2000 * d)
    """
    P = - (friction_factor * pipe_length * rho * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculates and returns the pressure loss (P) caused by pipe fittings.
    Formula: P = -0.04 * p * v² * n / 2000
    """
    P = -0.04 * rho * fluid_velocity**2 * quantity_fittings / 2000
    return P


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates and returns the Reynolds number (unitless).
    Formula: R = p * d * v / μ
    """
    mu = 0.0010016 # Dynamic viscosity (Pa·s)
    R = (rho * hydraulic_diameter * fluid_velocity) / mu
    return R


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates and returns the pressure loss (in kPa) caused by reduction in pipe diameter.
    Formulas:
        k = 0.1 + (50 / R) * ((D/d)^4 - 1)
        P = -k * p * v² / 2000
    """
    if fluid_velocity == 0:
        return 0
    k = (0.1 + (50 /reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    P = - (k * rho * (fluid_velocity ** 2)) / 2000
    return P

def kpa_to_psi(pressure_kpa):
    """
    Converts kilopascals (kPa) to pounds per square inch (psi).
    """
    psi = pressure_kpa / 6.89475729
    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
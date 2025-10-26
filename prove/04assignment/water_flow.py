# Name: Izzie Vazquez
# Assignment Name: 05 Prove Milestone: Testing and Fixing Functions
# Assignment Description:
# Write a Python program that could help an engineer design a water distribution system. During this prove
# milestone, you will write three program functions and three test functions as described in the Steps section below.

import pytest
from pytest import approx

def water_column_height(tower_height, tank_height):
    """
    Calculates and returns the height of the water column in meters.
    Formula: h = t + (3w / 4)
    """
    h = tower_height + (3 * tank_height / 4)
    return h


def pressure_gain_from_water_height(height):
    """
    Calculates and returns the pressure from water height in kPa.
    Formula: P = (p * g * h) / 1000
    """
    rho = 998.2 # Density of water (kg/m³)
    g = 9.80665 # Acceleration due to gravity (m/s²)
    P = (rho * g * height) / 1000
    return P


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates and returns the pressure loss due to pipe friction in kPa.
    Formula: P = - (f * L * p * v²) / (2000 * d)
    """
    rho = 998.2  # Density of water (kg/m³)
    P = - (friction_factor * pipe_length * rho * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return P
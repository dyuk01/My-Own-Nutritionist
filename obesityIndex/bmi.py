import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    Calculate BMI using weight and height.
    
    :param weight_kg: Weight in kilograms.
    :param height_cm: Height in centimeters.
"""

def bmi(weight_kg, height_cm):
    res = weight_kg / (height_cm)^2
    return res
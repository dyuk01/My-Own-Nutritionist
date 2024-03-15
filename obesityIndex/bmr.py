import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    Calculate daily calorie intake using the Mifflin-St Jeor Equation.
    
    :param weight_kg: Weight in kilograms.
    :param height_cm: Height in centimeters.
    :param age: Age in years.
    :param gender: Gender ('male' or 'female').
    :param activity_level: Activity level ranging from 1.2 (sedentary) to 2.5 (very active).
    :return: Estimated daily calorie intake.
"""

def calculate_daily_calories(weight_kg, height_cm, age, gender, activity_level):
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    return bmr * activity_level
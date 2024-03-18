import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    Calculate bmr and daily calorie intake using the Mifflin-St Jeor Equation.
    
    :param weight_kg: Weight in kilograms.
    :param height_cm: Height in centimeters.
    :param age: Age in years.
    :param gender: Gender ('male' or 'female').
    :param activity_level: Activity level ranging from 1.2 (sedentary) to 2.5 (very active).
    :return: Estimated daily calorie intake.
"""

def bmr(weight_kg, height_cm, age, gender):
    if gender == 'male':
        res = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == 'female':
        res = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else :
        print("Invalid Input\n")
        return
    return res

def calories_intake(bmr, activity_level):
    res = bmr * activity_level
    return res
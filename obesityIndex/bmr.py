import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_daily_calories(weight_kg, height_cm, age, gender, activity_level):
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    return bmr * activity_level
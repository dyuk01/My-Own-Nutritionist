import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class NutritionApp:
    """
    Initialization

    :param weight_kg: Weight in kilograms.
    :param height_cm: Height in centimeters.
    :param age: Age in years.
    :param gender: Gender ('male' or 'female').
    :param activity_level: Activity level ranging from 1.2 (sedentary) to 2.5 (very active).
    :return: Estimated daily calorie intake.
    """
    def __init__(self, weight, height, age, gender, activity_level):
        self.weight = weight  # in kilograms
        self.height = height  # in centimeters
        self.age = age
        self.gender = gender
        self.activity_level = activity_level

    #Calculate bmr and daily calorie intake using the Mifflin-St Jeor Equation
    def bmr(self):
        if self.gender == 'male':
            res = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5
        elif self.gender == 'female':
            res = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age - 161
        else :
            print("Invalid Input\n")
            return
        return res
    
    # Total Daily Energy Expenditure (TDEE) calculation
    def calories_intake(self):
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        tdee = self.calculate_bmr() * activity_factors.get(self.activity_level, 1.2)
        return tdee
    

    def bmr(weight_kg, height_cm, age, gender):
        if gender == 'male':
            res = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        elif gender == 'female':
            res = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        else :
            print("Invalid Input\n")
            return
        return res

    def calculate_tdee(self):
        # Total Daily Energy Expenditure (TDEE) calculation
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        tdee = self.calculate_bmr() * activity_factors.get(self.activity_level, 1.2)
        return tdee

    def suggest_meal_plan(self):
        # Placeholder for meal plan suggestions
        # Implement logic based on TDEE and dietary preferences
        pass

    def find_nearby_food_options(self):
        # Placeholder for integrating location-based food suggestions
        # Implement logic to use location data for finding food options
        pass

# Example usage
user_app = NutritionApp(weight=70, height=175, age=25, gender='male', activity_level='moderate')
print(f"Your daily calorie needs: {user_app.calculate_tdee()} kcal")

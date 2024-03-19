import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

class NutritionApp:
    """
    :param weight_kg: Weight in kilograms.
    :param height_cm: Height in centimeters.
    :param age: Age in years.
    :param gender: Gender ('male' or 'female').
    :param activity_level: Activity level ranging from 1.2 (sedentary) to 2.5 (very active).
    :return: Estimated daily calorie intake.
    """

    #Initialization
    def __init__(self, weight, height, age, gender, activity_level):
        self.weight = weight  # in kilograms
        self.height = height  # in centimeters
        self.age = age
        self.gender = gender
        self.activity_level = activity_level

    #Calculate bmr and daily calorie intake using the Mifflin-St Jeor Equation
    def bmr(weight_kg, height_cm, age, gender):
        if gender == 'male':
            res = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        elif gender == 'female':
            res = 10 * weight_kg + 6.25 *height_cm - 5 * age - 161
        else :
            print("Invalid Input\n")
            return
        return res
    
    # Total Daily Energy Expenditure (TDEE) calculation
    def calories_intake(weight_kg, height_cm, age, gender, activity_level):
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        bmr = bmr(weight_kg, height_cm, age, gender)
        tdee = bmr * activity_factors.get(activity_level, 1.2)
        return tdee
    
    def suggest_meal_plan(self):
        # Placeholder for meal plan suggestions
        # Implement logic based on TDEE and dietary preferences
        pass

    def find_nearby_food_options(self):
        # Placeholder for integrating location-based food suggestions
        # Implement logic to use location data for finding food options
        pass

class NutritionAppUI(QWidget):
    #Initialization
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nutrition App')
        self.setWindowIcon(QIcon('path/to/your/logo.png'))  # Set your logo path here

        # Create layout
        vbox = QVBoxLayout()

        # Logo
        logo = QLabel(self)
        pixmap = QPixmap('path/to/your/logo.png')  # Set your logo path here
        logo.setPixmap(pixmap)
        vbox.addWidget(logo)

        # Weight input
        hbox_weight = QHBoxLayout()
        label_weight = QLabel('Weight (kg):', self)
        self.input_weight = QLineEdit(self)
        hbox_weight.addWidget(label_weight)
        hbox_weight.addWidget(self.input_weight)
        vbox.addLayout(hbox_weight)

        # Height input
        hbox_height = QHBoxLayout()
        label_height = QLabel('Height (cm):', self)
        self.input_height = QLineEdit(self)
        hbox_height.addWidget(label_height)
        hbox_height.addWidget(self.input_height)
        vbox.addLayout(hbox_height)

        # Age input
        hbox_age = QHBoxLayout()
        label_age = QLabel('Age:', self)
        self.input_age = QLineEdit(self)
        hbox_age.addWidget(label_age)
        hbox_age.addWidget(self.input_age)
        vbox.addLayout(hbox_age)

        # Gender input
        hbox_gender = QHBoxLayout()
        label_gender = QLabel('Gender:', self)
        self.input_gender = QLineEdit(self)
        hbox_gender.addWidget(label_gender)
        hbox_gender.addWidget(self.input_gender)
        vbox.addLayout(hbox_gender)

        # Activity level input
        hbox_activity = QHBoxLayout()
        label_activity = QLabel('Activity Level:', self)
        self.input_activity = QLineEdit(self)
        hbox_activity.addWidget(label_activity)
        hbox_activity.addWidget(self.input_activity)
        vbox.addLayout(hbox_activity)

        # Calculate button
        btn_calculate = QPushButton('Calculate TDEE', self)
        btn_calculate.clicked.connect(self.showDialog)
        vbox.addWidget(btn_calculate)

        self.setLayout(vbox)
        self.show()

    def showDialog(self):
        weight = float(self.input_weight.text())
        height = float(self.input_height.text())
        age = int(self.input_age.text())
        gender = self.input_gender.text()
        activity_level = self.input_activity.text()

        user_app = NutritionApp(weight, height, age, gender, activity_level)
        tdee = user_app.calories_intake()

        QMessageBox.information(self, 'Result', f'Your daily calorie needs: {tdee} kcal', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NutritionAppUI()
    sys.exit(app.exec_())
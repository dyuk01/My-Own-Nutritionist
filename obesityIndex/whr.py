import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    Calculate Waist to Hip ratio.
    
    :param waist_circ_cm: Waist circumference in cm.
    :param hip_circ_cm: Hip circumference in cm.
"""

def calculate_daily_calories(waist_circ_cm, hip_circ_cm):
    whr = waist_circ_cm / hip_circ_cm
    return whr
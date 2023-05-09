
import pandas as pd
import numpy as np
import numbers
import ast

def transform_currencies(amount,currency):
    if (not np.isnan(amount) and currency!='Free'):
        if currency=='EUR':
            return int(amount)
        else:
            return int(amount*currencies[currency][0])
    else:
        return amount

def fix_city(city):
    if type(city)==type("s"):
        city = city.replace("\\","").replace("x92","")\
            .replace("xc3xa1","a").replace("xc3xa4","a")\
            .replace("xc3x89","E").replace("xc3xa9","e")\
            .replace("xc3x8d","I").replace("xc3x9f","b")\
            .replace("xc3xa8","e").replace("xc3xb","u")\
            .replace("xc3xa3","a").replace("xc3xad","i")\
            .replace("xc3xa6","ae").replace("xc3xac","i")\
            .replace("xc3x85","A").replace("xc3x96","O")\
            .replace("xc3x85","A").replace("xc2xb4","")\
            .replace("xc3xa7","c").replace("xc3x81","A")\
            .replace("xc3xa5","a").replace("xc3xa2","a")
        return ast.literal_eval(city)[0]
    return np.nan


def convert_duration(duration):
    if isinstance(duration, numbers.Number):
        return duration
    elif 'months' in duration:
        return int(duration.split(' ')[0])
    elif 'days' in duration:
        return int(int(duration.split(' ')[0]) / 30)
    else:
        return np.nan
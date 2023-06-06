# Any functionalities that I am probably writing in a common way, which will be used in entire application --> basically say that as a utils.py

'''
- Let's say I want to read a dataset from a database, I can probably create my client like mongodb client over here.
- If I want to probably save my model into the cloud, I can write the code over here
'''

import os
import sys

import numpy as np 
import pandas as pd
import dill
# import pickle

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

"""
Topic: Numpy
Date: 22/04/2024
Author: Hugo
"""

import numpy as np


def ShowInformation():
    print(f'Numpy Version: {np.__version__}')
    print('\nConfig Settings:')
    print(np.show_config())

def ContainsAZero(array: np.array):
    return not np.all(array)


if __name__ == '__main__':
    ShowInformation()

    myFirstArray = np.array([1,2,3,4])
    print(f'Array: {myFirstArray}')
    print(f'Contains A Zero: {ContainsAZero(myFirstArray)}')

    mySecondArray = np.array([0, 1, 2, 3])
    print(f'Array: {mySecondArray}')
    print(f'Contains A Zero: {ContainsAZero(mySecondArray)}')
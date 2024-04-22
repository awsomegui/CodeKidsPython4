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


if __name__ == '__main__':
    ShowInformation()

    myFirstArray = np.array([1,2,3,4])
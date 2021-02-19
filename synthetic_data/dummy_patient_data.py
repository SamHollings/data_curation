"""Author - Sam Hollings
This file makes dummy patient data in two styles - short-wide (more like HES, Civil Registration Deaths, etc.) and long-thin (more like GDPPR and others)
These are intended to be used for development and testing ONLY, and are not real reflections of patients, or any existing datasets.
"""
import pandas as pd
import numpy as np
import random

def random_list(elements, rows,p=None):
    return np.random.choice(elements, size=rows,p=p)#[element for x in range(0, rows)]


def column_random_person_id(rows=10000):
    """generate a column of person ID"""
    df = pd.DataFrame(index=range(0,rows))

    df['person_id'] = random_list(range(1000, 9999),rows)

    column_random_person_id_series = df['person_id']

    return column_random_person_id_series


def long_thin_data(rows=10000):
    """Make a long thin dataset"""
    df = pd.DataFrame(index=range(0,rows))
    df['person_id'] = column_random_person_id(rows=rows)
    df['gender'] = random_list(range(1,3),rows)
    df['date_birth'] = random_list(["{0}-01-01".format(1950+x) for x in range(0,71)],rows)
    df['diag'] = random_list(["diag_code_{0}".format(x) for x in range(0,21)],rows)
    df['date_date'] = random_list(["{0}-{1:02d}-01".format(2000 + x, y) for x in range(0, 21) for y in range(1,13)], rows)
    return df
"""Author - Sam Hollings
This file makes dummy patient data in two styles - short-wide (more like HES, Civil Registration Deaths, etc.) and long-thin (more like GDPPR and others)
These are intended to be used for development and testing ONLY, and are not real reflections of patients, or any existing datasets.
"""
import pandas as pd
import numpy as np


def random_list(elements, rows,p=None):
    """Generate a column of data sampling randomly from the provided list of elements, with probaility defined in the
    list p, for each element (if left as none, then equal chance for each element"""
    return np.random.choice(elements, size=rows,p=p)#[element for x in range(0, rows)]


def column_random_person_id(rows=10000):
    """generate a column of person ID"""
    df = pd.DataFrame(index=range(0,rows))

    df['person_id'] = random_list(range(10000000, 99999999),rows)

    column_random_person_id_series = df['person_id']

    return column_random_person_id_series


def short_wide_data(rows=10000, arrival_col_name='arrival', discharge_col_name='discharge', diag_col_name_dict = dict(diag = 'diag', proc='proc')):
    """Make a long thin dataset"""
    df = pd.DataFrame(index=range(0,rows))
    df['person_id'] = column_random_person_id(rows=rows)
    df['gender'] = random_list(range(1,3),rows)
    df['date_birth'] = random_list(pd.date_range('1970-01-01','2020-01-01', freq='MS'),rows)
    df[f'{arrival_col_name}_date'] = random_list(pd.date_range('2000-01-01','2020-01-01', freq='MS'), rows)
    if discharge_col_name is not None:
        df[f'{discharge_col_name}_date'] = df['arrival_date'].apply(lambda x: np.random.choice(pd.date_range(x,'2020-01-01', freq='MS')))
    for diag_col_name, diag_code_name in diag_col_name_dict.items():
        df[f'{diag_col_name}_01'] = random_list([f"{diag_code_name}_code_{x}" for x in range(0, 21)], rows)
        df[f'{diag_col_name}_02'] = random_list([None]*60+[f"{diag_code_name}_code_{x}" for x in range(0, 21)], rows)
        df[f'{diag_col_name}_03'] = random_list([None]*180+[f"{diag_code_name}_code_{x}" for x in range(0, 21)], rows)
    return df


def short_wide_hospital_data(rows=10000):
    """Make a fake Hosptial dataset"""
    df = short_wide_data(rows=rows)
    return df


def short_wide_death_data(rows=10000):
    """Make a fake deaths dataset"""
    df = short_wide_data(rows=rows, arrival_col_name='death', discharge_col_name=None, diag_col_name_dict=dict(cause='diag'))
    return df


def long_thin_gp_data(rows=10000):
    """make a fake GP dataset - this is long and thin, unlike deaths and hospital"""
    df = short_wide_data(rows=rows, arrival_col_name='event', discharge_col_name=None, diag_col_name_dict=dict(diag='diag'))
    df_long_thin = df.melt(id_vars=['person_id','gender','date_birth','event_date'],
                           value_vars=['diag_01','diag_02','diag_03'],
                           value_name='diag_code',
                           var_name='diag_position')
    return df_long_thin
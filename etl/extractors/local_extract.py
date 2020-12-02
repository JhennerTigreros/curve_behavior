import pandas as pd

def load():
    df_employe = pd.read_excel('./extractors/data/employe.xlsx', sheet_name = 'Tnal mensual')
    df_inflation = pd.read_excel('./extractors/data/inflation.xlsx')

    return df_employe, df_inflation
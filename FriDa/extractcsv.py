import pandas as pd
import pathlib

def extractcsv():
    path = pathlib.Path(__file__).parent.resolve()

    ds = pd.read_csv(str(path)+'/alumno.csv', sep='|')
    ds = ds.sort_values('data_verifica', ascending=False)

    headings = ds.columns 
    data = ds.values.tolist()
    return [headings, data]

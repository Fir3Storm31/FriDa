import pandas as pd
import pathlib

def extractcsv():
    path = pathlib.Path(__file__).parent.resolve()

    ds = pd.read_csv(str(path)+'/alumno.csv', sep='|')

    headings = ds.columns 
    data = ds.values.tolist()
    return [headings, data]

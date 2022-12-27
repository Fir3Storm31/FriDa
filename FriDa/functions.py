import pandas as pd
import json

def addRowToCsv(row):
    try:
        ds = pd.read_csv('alumno.csv', sep='|')
    except:
        with open('alumno.csv', 'w') as f:
            f.write('anno_scolastico,periodo_valutativo,data_verifica,tipo_verifica,materia,docente,voto,descrizione\n')
            ds = pd.read_csv('alumno.csv', sep='|')

    ds = pd.read_csv('alumno.csv', sep='|')
    ds = pd.concat([ds, pd.DataFrame.from_records([
        {'anno_scolastico': row[0], 'periodo_valutativo': row[1], 
        'data_verifica': row[2], 'tipo_verifica': row[3], 
        'materia': row[4], 'docente': row[5], 'voto': row[6], 'descrizione': row[7]}])])
    ds.to_csv('alumno.csv', sep='|', index=False)

def changeSettings(changes):
    with open('Settings/aesthetics.json') as f:
        aesthetics = json.load(f)
        for change in changes:
            aesthetics[change[0]] = change[1]
    with open('Settings/aesthetics.json', 'w') as f:
        json.dump(aesthetics, f)
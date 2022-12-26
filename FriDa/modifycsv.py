import pandas as pd
import datetime
import tornado

try:
    ds = pd.read_csv('alumno.csv', sep='|')
except:
    with open('alumno.csv', 'w') as f:
        f.write('anno_scolastico,periodo_valutativo,data_verifica,tipo_verifica,materia,docente,voto,descrizione\n')
        ds = pd.read_csv('alumno.csv', sep='|')

def addRow(anno_scolastico, periodo_valutativo, data_verifica, tipo_verifica, materia, docente, voto, descrizione):
    ds = pd.read_csv('alumno.csv', sep='|')
    ds = pd.concat([ds, pd.DataFrame.from_records([
        {'anno_scolastico': anno_scolastico, 'periodo_valutativo': periodo_valutativo, 
        'data_verifica': data_verifica, 'tipo_verifica': tipo_verifica, 
        'materia': materia, 'docente': docente, 'voto': voto, 'descrizione': descrizione}])])
    ds.to_csv('alumno.csv', sep='|', index=False)
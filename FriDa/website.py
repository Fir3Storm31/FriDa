import json
from flask import Flask, request, render_template

from extractcsv import extractcsv
from functions import addRowToCsv, changeSettings

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', headings=extractcsv()[0], data=extractcsv()[1])

@app.route('/voti', methods=['POST', 'GET'])
def voti():
    if request.method == "POST":
        if (int(request.form['data_verifica'][5:7]) > 0) & (int(request.form['data_verifica'][5:7]) < 7):
            anno_scolastico = int(request.form['data_verifica'][0:4]) - 1
            periodo_valutativo = 'pentamestre'
        else:
            anno_scolastico = int(request.form['data_verifica'][0:4])
            periodo_valutativo = 'trimestre'
        addRowToCsv(row = [
            anno_scolastico,
            periodo_valutativo,
            request.form['data_verifica'],
            request.form['tipo_verifica'],
            request.form['materia'],
            request.form['docente'],
            request.form['voto'],
            request.form['descrizione']
        ])
    return render_template('voti.html', headings=extractcsv()[0], data=extractcsv()[1])

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == "POST":
        changeSettings(changes = [
            ['theme', request.form['theme']],
            ['barplot_color', request.form['barplot_color']],
            ['barplot_grid',  eval(request.form['barplot_grid'])],
            ['scatterplot_grid', eval(request.form['scatterplot_grid'])],
            ['lineplot_linewidth', int(request.form['lineplot_linewidth'])],
            ['lineplot_grid', eval(request.form['lineplot_linewidth'])]
        ])
    f = open('Settings/aesthetics.json')
    aesthetics = json.load(f)
    return render_template('settings.html', settings=aesthetics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


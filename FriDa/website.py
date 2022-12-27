import panel as pn
import holoviews as hv
from flask import Flask, request, render_template

from fridash import golden
from extractcsv import extractcsv
from modifycsv import addRow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', headings=extractcsv()[0], data=extractcsv()[1])

@app.route('/submit', methods=['POST'])
def submit():
    anno_scolastico = request.form['anno_scolastico']
    periodo_valutativo = request.form['periodo_valutativo']
    data_verifica = request.form['data_verifica']
    tipo_verifica = request.form['tipo_verifica']
    materia = request.form['materia']
    docente = request.form['docente']
    voto = request.form['voto']
    descrizione = request.form['descrizione']
    addRow(anno_scolastico, periodo_valutativo, data_verifica, tipo_verifica, materia, docente, voto, descrizione)
    return render_template('index.html', headings=extractcsv()[0], data=extractcsv()[1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


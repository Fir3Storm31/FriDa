import hvplot.pandas
import panel as pn
import pandas as pd
import panel.widgets as pnw
import pathlib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import json
from bokeh.models import DatetimeTickFormatter

#css = '''
#.bk.panel-widget-box {
#  background: #4b4b4b;
#  border-radius: 5px;
#  border: 1px grey solid;
#}
#'''

pn.extension()#raw_css=[css])

f = open('Settings/aesthetics.json')
aesthetics = json.load(f)

path = pathlib.Path(__file__).parent.resolve()

pn.extension(sizing_mode='stretch_width')

#data = pd.read_csv(str(path)+'/frisidata.csv')
data = pd.read_csv(str(path)+'/alumno.csv', sep='|')

data['data_verifica'] = pd.to_datetime(data['data_verifica'])
data['mese_giorno'] = data['data_verifica'].dt.strftime('%m-%d')
data['voto'] = pd.to_numeric(data['voto'], errors='coerce')
#data["mese_giorno"] = pd.to_datetime(data["mese_giorno"])

materia = pnw.Select(
    name='Materia', value="Materia", options=list(data['materia'].unique())
)
anno_scolastico = pnw.Select(
    name='Anno Scolastico', value="Anno Scolastico", options=list(data['anno_scolastico'].unique())
)

idf = data.interactive()
idf2 = data.interactive()
idf3 = data.interactive()

df = idf[
    ( idf['materia'] ==  materia ) & 
    ( idf['anno_scolastico'] ==  anno_scolastico )
    ].sort_values('data_verifica')

df2 = idf2[
    ( idf2['materia'] ==  materia )
    ].sort_values('mese_giorno')

df3 = idf3[
    ( idf3['anno_scolastico'] ==  anno_scolastico )
    ].sort_values('data_verifica')

plot = df.hvplot.bar(x='data_verifica', y='voto', 
                      title='Voti materia', hover_alpha= 0.5,
                      line_width=3, hover_line_width=5,   
                      line_join='bevel', line_cap='round', 
                      color      = aesthetics["barplot_color"],
                      grid       = aesthetics["barplot_grid"],
                      hover_cols = aesthetics["barplot_hover"],
                      xformatter=DatetimeTickFormatter(
                        hours=["%Y-%m"], days=["%Y-%m-%d"], 
                        months=["%Y-%m"], years=["%m-%d"]))


plot2 = df2.hvplot.scatter(x='mese_giorno', y='voto', color='anno_scolastico',
                      title='Voti materia per a.s.',
                      line_width=9, hover_line_width=14,
                      line_join='bevel', line_cap='round',
                      cmap = aesthetics["scatterplot_colors"],
                      grid = aesthetics["scatterplot_grid"],)

all_subjects = df3.hvplot.line(x='data_verifica', y='voto', 
                      title='Materie a confronto', by='materia', 
                      hover_line_width=9, hover_alpha=0.5, 
                      line_join='bevel', line_cap='round', 
                      color      = aesthetics["lineplot_colors"],
                      grid       = aesthetics["lineplot_grid"],
                      line_width = aesthetics["lineplot_linewidth"],
                      hover_cols = aesthetics["lineplot_hover"],
                      xformatter=DatetimeTickFormatter(
                        hours=["%Y-%m"], days=["%Y-%m-%d"], 
                        months=["%Y-%m"], years=["%m-%d"]))

golden = pn.template.GoldenTemplate(title='FriDa', theme=aesthetics["theme"])
golden.sidebar.append(
    pn.Column(
        pn.pane.Markdown("## Controlli dashboard"),
        materia, 
        anno_scolastico)
)
golden.main.append(
    pn.Column(
        plot.panel(),
        plot2.panel()
    )
)
golden.main.append(
    pn.Column(
        all_subjects.panel()
        )
)

f.close()

app = FastAPI()
templates = Jinja2Templates(directory="examples/apps/fastApi/templates")

@app.get("/")
async def main(request: Request):
    script = server_document("http://localhost:5006/app")
    return templates.TemplateResponse("base.html", {"request": request, "script": script})

if __name__ == "__main__":
    pn.serve({'/dashboard': golden}, port=5000)
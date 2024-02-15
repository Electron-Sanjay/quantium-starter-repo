from dash import Dash, html,dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv("D:/Forage/Quantium/sw/quantium-starter-repo/final.csv")

data = data.sort_values(by= "date", ascending= True)


fig = px.line(data,x= "date",y= "Total Sales in $")

app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsel'),

    html.Div(children='''
        Below graph shows the sales of the Pink Morsel.
    '''),

    dcc.Graph(
        id='line-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

"""From the dash we can say that the sales are increased even 
after the price of the Pink Morsel increase"""
import pandas as pd
import nltk
import functions
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Figure, Layout, Bar
from plotly.graph_objs import *

app = dash.Dash()


text_data = pd.read_csv('data.csv')

nonzero = text_data[(text_data['Compound'] != 0)]
trace = go.Scatter(
    x=nonzero.Date,
    y=nonzero['Compound'],
    name = "Compound Sentiment",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

data3 = [trace]

layout3 = dict(
    title='Compound Polarity over Time',
    titlefont = dict(
        size=20,
        color = 'rgb(203, 203, 203)'
    ),
    font = dict(family='Courier New, monospace', size = 10, color = '#cbcbcb'),
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=3,
                     label='3m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=12,
                     label='12m',
                     step='month',
                     stepmode='backward'),
                dict(count=24,
                     label='2y',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ]),
            font = dict(size = 11, color = '#000000')
        ),
        rangeslider=dict(),
        type='date'
    ),
    paper_bgcolor = 'rgba(44, 58, 71, 1)',
    plot_bgcolor = 'rgba(44, 58, 71, 1)',
    height = 560,
    width = 800
)

fig3 = dict(data=data3, layout=layout3)


values = [3893, 3661, 2810, 2609, 2127, 2016, 1569, 1123, 1101, 1100]
phases = ['#tcot', '#politics', '#pjnet', '#maga', '#news', '#trump', '#ccot', '#merkelmussbleiben', '#trumpforpresident', '#wakeupamerica']


colors = ['rgb(32,155,160)', 'rgb(253,93,124)', 'rgb(28,119,139)', 'rgb(182,231,235)', 'rgb(35,154,160)', 'rgb(45,32,193)', 'rgb(123,167,33)', 'rgb(34,55,78)', 'rgb(109,33,165)', 'rgb(76,89,145)']

n_phase = len(phases)
plot_width = 400

# height of a section and difference between sections 
section_h = 100
section_d = 10

# multiplication factor to calculate the width of other sections
unit_width = plot_width / max(values)

# width of each funnel section relative to the plot width
phase_w = [int(value * unit_width) for value in values]

# plot height based on the number of sections and the gap in between them
height = section_h * n_phase + section_d * (n_phase - 1)


# list containing all the plot shapes
shapes = []

# list containing the Y-axis location for each section's name and value text
label_y = []

for i in range(n_phase):
        if (i == n_phase-1):
                points = [phase_w[i] / 2, height, phase_w[i] / 2, height - section_h]
        else:
                points = [phase_w[i] / 2, height, phase_w[i+1] / 2, height - section_h]

        path = 'M {0} {1} L {2} {3} L -{2} {3} L -{0} {1} Z'.format(*points)

        shape = {
                'type': 'path',
                'path': path,
                'fillcolor': colors[i],
                'line': {
                    'width': 1,
                    'color': colors[i]
                }
        }
        shapes.append(shape)
        
        # Y-axis location for this section's details (text)
        label_y.append(height - (section_h) / 2)

        height = height - (section_h + section_d)

# For phase names
label_trace = go.Scatter(
    x=[-350]*n_phase,
    y=label_y,
    mode='text',
    text=phases,
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)
 
# For phase values
value_trace = go.Scatter(
    x=[350]*n_phase,
    y=label_y,
    mode='text',
    text=values,
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)

data = [label_trace, value_trace]
 
layout = go.Layout(
    title="<b>Top Ten Hashtags Used by Russian Bots</b>",
    titlefont=dict(
        size=20,
        color='rgb(203,203,203)'
    ),
    shapes=shapes,
    height=560,
    width=800,
    showlegend=False,
    paper_bgcolor='rgba(44,58,71,1)',
    plot_bgcolor='rgba(44,58,71,1)',
    xaxis=dict(
        showticklabels=False,
        zeroline=False,
    ),
    yaxis=dict(
        showticklabels=False,
        zeroline=False
    ),
    margin=go.Margin(
        l=50,
        r=50,
        b=50,
        t=100,
        pad=4
    )
)

fig = dict(data=data, layout=layout)    



trace1 = go.Bar(
    y=['@realdonaldtrump'],
    x=[4325],
    orientation = 'h',
    marker = dict(
        color = 'rgba(32,155,160, 0.6)',
        line = dict(
            color = 'rgba(253,93,124, 1.0)',
            width = 2)
    )
)
trace2 = go.Bar(
    y=['@midnight'],
    x=[2414],
    orientation = 'h',
    marker = dict(
        color = 'rgba(28,119,139, 0.6)',
        line = dict(
            color = 'rgba(182,231,235, 1.0)',
            width = 2)
    )
)

trace3 = go.Bar(
    y=['@blicqer'],
    x=[2181],
    orientation = 'h',
    marker = dict(
        color = 'rgba(35,154,160, 0.6)',
        line = dict(
            color = 'rgba(45,32,193, 1.0)',
            width = 2)
    )
)

trace4 = go.Bar(
    y = ['@hillaryclinton'],
    x=[2080],
    orientation = 'h',
    marker = dict(
        color = 'rgba(123,167,33, 0.6)',
        line = dict(
            color = 'rgba(34,55,78, 1.0)',
            width = 2)
    )
)

trace5 = go.Bar(
    y=['@conservatexian'],
    x=[1105],
    orientation = 'h',
    marker = dict(
        color = 'rgba(109,33,165, 0.6)',
        line = dict(
            color = 'rgba(76,89,145, 1.0)',
            width = 2)
    )
)


data2 = [trace5, trace4, trace3, trace2, trace1]
layout2 = go.Layout(
    title="<b>Top Five Mentions by Russian Bots</b>",
    titlefont=dict(
        size=20,
        color='rgb(203,203,203)'
    ),
    font=dict(family='Courier New, monospace', size=10, color='#cbcbcb'),
    barmode='stack',
    height=560,
    width=800,
    showlegend=False,
    paper_bgcolor='rgba(44,58,71,1)',
    plot_bgcolor='rgba(44,58,71,1)',
    margin=go.Margin(
        l=150,
        r=50,
        b=100,
        t=100,
        pad=4
    )
)

fig2 = dict(data=data2, layout=layout2)


labels = ['Positive', 'Negative', 'Neutral']
values = [61049, 61209, 77741]

trace8 = go.Pie(labels=labels, values=values)
data4 = [trace8]

layout4 = go.Layout(
    title="<b>Overall Sentiment Analysis<b>",
    titlefont=dict(
        size=20,
        color='rgb(255, 255, 255)'
    ),
    font=dict(family='Courier New, monospace', size=10, color='#FFFFFF'),
    height = 560, 
    width = 800,
    paper_bgcolor='rgba(44,58,71,1)'
)

fig4 = dict(data = data4, layout = layout4)

app.layout = html.Div([
    html.Div(
        [
         html.H2("Russia Lago: Safeguarding Voters from State Sponsored Content\nAuthors: Clara Na, Siddharth Nanda, Dhyey Parikh, Dale Wilson")
            ],
        className='banner',
        style={'color': '#FFFFFF','text-align': 'center', 'margin-bottom': '30px'}
        ),
 
    
    html.Div([
        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
        
        dcc.Graph(
            id = 'graph4',
            figure=fig4
         )], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'baseline'}),
    
    html.Div([
        dcc.Graph(
            id='graph1',
            figure=fig
        ),

        dcc.Graph(
            id ='graph2',
            figure=fig2
        )], style= {'width': '49%', 'display': 'inline-block'}), 
],  style={'backgroundColor': '#000000', 'margin': '0 auto'})


if __name__ == '__main__':
    app.run_server(debug=True)
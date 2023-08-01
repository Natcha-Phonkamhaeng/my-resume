import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback
import plotly.graph_objects as go
import pandas as pd


dash.register_page(__name__, path='/', icon="bi bi-person-circle", order=1)

def skill():
	fig = go.Figure(data=go.Scatterpolar(
		r=[4, 4, 5, 3, 3, 5],
		theta=['Finance and Account','Coding Language','Web App Dashboard', 'English Language', 'Data Science Model', 'MS Excel'],
		fill='toself'
	))

	fig.update_layout(polar=dict(bgcolor='rgb(30,33,48)'),showlegend=False, 
		paper_bgcolor='rgba(0,0,0,0)',
		margin=dict(l=45, r=45, t=45, b=45),
		font={'color':'dodgerblue'})
	return fig

layout = dbc.Container([
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardImg(src='assets/pic.jpg')
				])
			], width=5, xs=10, sm=5, md=5, lg=6, xl=5),
		dbc.Col([
			html.H2(['Resume']),
			html.P(['15 years in finance / 3 years in coding / masters degree in Data Science (studying)'], className='icon-color'),
			html.Br(),
			html.P(['15 years experience in financing field of Ocean Freight and Logistics Business. 3 years of coding specialized in\
				dashboard, data cleaning ETL and data insight with the language of Python, JavaScript, CSS, HTML. \
				Now looking for a job as a data analyst.'], 
				style={'justify':'center', 'color': 'grey'}),
			html.Hr(),
			html.H4(children=[html.I(className='bi bi-speedometer2 me-2 icon-color'), 'Skills']),
			dcc.Graph(figure=skill()),
			html.Hr(),
			html.H4(['Contact']),
			html.P(['Email: Natcha.Phonkamhaeng@gmail.com'], style={'color': 'grey'}),
			html.P(['Phone No: 081-557-5214'], style={'color': 'grey'})
			], width=7)
		], justify='center')
	])

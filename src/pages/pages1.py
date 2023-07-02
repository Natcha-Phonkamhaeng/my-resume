import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_ag_grid as dag

dash.register_page(__name__, path='/', icon="bi bi-person-circle", order=1)


layout = dbc.Container([
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardImg(src='assets/pic.jpg')
				])
			], width=5, xs=10, sm=5, md=5, lg=6, xl=5),
		dbc.Col([
			html.H2(['Resume']),
			html.P(['15 years in finance / 3 years in coding / masters degree in Data Science (studying)'], style={'color': 'dodgerblue'}),
			html.Br(),
			html.P(['15 years experience in financing feild of Ocean Freight and Logistics Business. 3 years of coding specialized in'\
				' dashboard, data cleaning and data insight with the language of Python.'], 
				style={'justify':'center', 'color': 'grey'}),
			html.Br(),
			html.Hr(),
			], width=7)
		], justify='center')
	])


















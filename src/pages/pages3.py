import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback


dash.register_page(__name__, path='/service', icon="bi bi-buildings-fill", order=3)

layout = dbc.Container([
	dbc.Row([
		dbc.Col([
			html.H2(['My service'])
			])
		], style={'margin-left': '2rem'}),
	html.Br(),
	dbc.Row([
		dbc.Col([
			html.H4(html.I(className='bi bi-rocket-takeoff icon-color')),
			html.H4(['Mitsui O.S.K Lines (Thailand) Co.,Ltd.'], style={'color': 'dodgerblue'}),
			html.P(['Year: 2008-2018'], style={'color': 'grey'}),
			html.P(['Position: Chief'], style={'color': 'grey'}),
			html.P(['Department: Finance and Accounting'], style={'color': 'grey'}),
			html.P(['Job Responsibilities:'], style={'color': 'grey'}),
			html.Li(['AR collection for outstanding customers'], style={'color': 'grey'}),
			html.Li(['Issue tax invoice/receipt'], style={'color': 'grey'}),
			html.Li(['Reconcile AR freight againt daily report'], style={'color': 'grey'}),
			]), 
		dbc.Col([
			html.H4(html.I(className='bi bi-airplane-fill icon-color')),
			html.H4(['Ocean Network Express (Thailand) PTE.'], style={'color': 'dodgerblue'}),
			html.P(['Year: 2018-present'], style={'color': 'grey'}),
			html.P(['Position: Supervisor'], style={'color': 'grey'}),
			html.P(['Department: Finance and Accounting'], style={'color': 'grey'}),
			html.P(['Job Responsibilities:'], style={'color': 'grey'}),
			html.Li(['Record AR freight in GL'], style={'color': 'grey'}),
			html.Li(['Checking and reconcile bank statement'], style={'color': 'grey'}),
			html.Li(['Reconcile AR freight againt daily report'], style={'color': 'grey'}),
			html.Li(['Reconcile withholding tax from Revenue Dept with GL'], style={'color': 'grey'}),
			html.Li(['e-tax invoice/e-receipt project'], style={'color': 'grey'}),
			html.Li(['Create tracking withholding tax from customers with GSheets'], style={'color': 'grey'}),
			html.Li(['Develope dashboard productivity Finance Dept for managements'], style={'color': 'grey'}),
			html.Li(['Develope program for converting file to e-receipt portal'], style={'color': 'grey'}),

			])
		], style={'margin-left': '2rem'})
	])
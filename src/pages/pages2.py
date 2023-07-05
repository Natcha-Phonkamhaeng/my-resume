import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback

dash.register_page(__name__, path='/project', icon="bi bi-briefcase-fill", order=2)

layout = dbc.Container([
	dbc.Row([
		dbc.Col([
			html.H2(['Project']),
			html.Br(),
			html.H4(children=[html.I(className='bi bi-github me-2 icon-color'), 'Github Repo']),
			html.A(children=[html.P(['https://github.com/Natcha-Phonkamhaeng'])], 
					href='https://github.com/Natcha-Phonkamhaeng',
					target='_blank'
					)
			], width=12, xs=10, sm=5, md=5, lg=6, xl=5)
		], style={'margin-left': '2rem'}),
	html.Br(),
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardImg(src='assets/nobel_pic.png', top=True),
				dbc.CardBody([
					html.H4('Nobel Prize', className='card-title'),
					html.P('Dashboard for the winners of nobel prize since 1901-2022', className='card-text', style={'color':'grey'}),
					dbc.Button(
						html.A(children=[html.P(['Click'])], 
							href='https://nobel-viz.onrender.com/',
							target='_blank'
							)
						)
					])
				])
			], width=4, xs=8, sm=8, md=4, lg=4, xl=4),
		dbc.Col([
			
			],width=4, xs=8, sm=8, md=4, lg=4, xl=4),
		dbc.Col([
			
			], width=4, xs=8, sm=8, md=4, lg=4, xl=4)
		], style={'margin-left': '2rem'})
	])








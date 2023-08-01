import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback

dash.register_page(__name__, path='/project', icon="bi bi-briefcase-fill", order=2)

layout = dbc.Container([
	html.H2(['Project'], style={'margin-left': '42px'}),
	html.P(['Note: viewing the projects might take time to open because I"m hosting the WepApp with free tier plan on Render.com'],
		style={'margin-left': '42px', 'margin-bottom': '30px'}),
	dbc.Row([
		dbc.Col([
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
					html.P('Interactive data visualization dashboard for the nobel prize since 1901-2022.\
						Written in Python', className='card-text', style={'color':'grey'}),
					dbc.Col([
						dbc.Button(
							html.A(children=[html.P(['View'])], 
							href='https://nobel-viz.onrender.com/',
							target='_blank'
							), className='project-left-button'
						),
						dbc.Button(
							html.A(children=[html.P(['Code'])], 
							href='https://github.com/Natcha-Phonkamhaeng/nobel-viz',
							target='_blank'
							), className='project-right-button'
						)
						])
					])
				])
			], width=4, xs=8, sm=8, md=4, lg=4, xl=4),
		dbc.Col([
			
			],width=4, xs=8, sm=8, md=4, lg=4, xl=4),
		dbc.Col([
			
			], width=4, xs=8, sm=8, md=4, lg=4, xl=4)
		], style={'margin-left': '2rem'})
	])








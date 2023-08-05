import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc, callback

dash.register_page(__name__, path='/education', icon="bi bi-mortarboard", order=4)

layout = dbc.Container([
	html.H2(["Education Background"], className='education-header'),
	html.Br(),
	dbc.Row([
			html.H4(['Bachelor\'s Degree'], className='icon-color'),
			html.Li(['Chulalongkorn University (2004-2008)']),
			html.Li(['Faculty: Economics with GPA 2.92']),
			html.Br(),
			html.Br(),
			html.H4(['Master\'s Degree'], className='icon-color'),
			html.Li(['Chulalongkorn University (2022-Present)']),
			html.Li(['Faculty: Accounting and Finance']),
			html.Li(['Field of Study: Statistics and Data Science'])
		], style={'margin-left': '2rem'})
	])


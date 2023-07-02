import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Output, Input, dcc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP],
		 meta_tags=[{'name': 'viewport',
                    'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )

server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "5rem",
    "padding": "2% 1%",
    "background-color": 'rgb(10,10,10)',
    'color': 'dodgerblue',
    'text-align': 'center',
    # 'font-size': '50px',
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": '1rem',
    # "margin-right": '5rem',
    #'padding': '2rem'
    #'margin-right': '10%',
    "margin-top": "2%"
}

sidebar = html.Div([
    html.Div(['NP'], style={'height': '1px', 'font-size':'20px', 'font-weight': 'bold'}),
    html.Br(),
    html.Br(),
    html.Div([
    	dbc.Nav([
        dbc.NavLink([
            html.Div(
                [
                    html.I(className=page["icon"])
              
                ], className='navbar-nav ms-0'),
            ],
            href=page['path']
            )
            for page in dash.page_registry.values()
        ],
        vertical=True),
    	])
    
    ])


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            sidebar
            ],
            style=SIDEBAR_STYLE),
        dbc.Col([
            dash.page_container
            ],
            style=CONTENT_STYLE, width={'size':12})
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
















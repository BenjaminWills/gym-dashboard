import dash_bootstrap_components as dbc
from dash import Dash, html, page_container, page_registry

app = Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.MINTY])

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Statistics", header=True),
                *[dbc.DropdownMenuItem(f"{page['name']}", href=page["relative_path"])
                for page in page_registry.values()]
            ],
            nav=True,
            in_navbar=True,
            label="Workout statistics",
        ),
    ],
    brand="Bens gym dashboard",
    brand_href="http://0.0.0.0:8080/",
    color="primary",
    dark=True,
)



app.layout = html.Div([navbar,
	page_container
    ])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=8080)
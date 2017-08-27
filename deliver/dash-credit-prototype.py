import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})





app.layout = html.Div([

	html.Div([
		html.Table([

			html.Tr([

				html.Th('Monthly income'),
				html.Th('Debt Ratio'),

				]),

			html.Tr([

				html.Td(dcc.Input(id='monthly-income-id', value=20800, type="number")),
				html.Td(dcc.Input(id='debt-ratio-id', value=0.5, type="number")),
								
				]),

			html.Tr([

				html.Th('Monthly income'),
				html.Th('Debt Ratio'),

				]),

			html.Tr([

				html.Td(dcc.Input(id='monthly-income-id', value=20800, type="number")),
				html.Td(dcc.Input(id='debt-ratio-id', value=0.5, type="number")),
								
				]),

			html.Tr([

				html.Th('Monthly income'),
				html.Th('Debt Ratio'),

				]),

			html.Tr([

				html.Td(dcc.Input(id='monthly-income-id', value=20800, type="number")),
				html.Td(dcc.Input(id='debt-ratio-id', value=0.5, type="number")),
				
				]),

			html.Tr([

				html.Th('Monthly income'),
				html.Th('Debt Ratio'),

				]),

			html.Tr([

				html.Td(dcc.Input(id='monthly-income-id', value=20800, type="number")),
				html.Td(dcc.Input(id='debt-ratio-id', value=0.5, type="number")),
				
				]),

			html.Tr([

				html.Th('Monthly income'),
				html.Th('Debt Ratio'),

				]),

			html.Tr([

				html.Td(dcc.Input(id='monthly-income-id', value=20800, type="number")),
				html.Td(dcc.Input(id='debt-ratio-id', value=0.5, type="number")),
				
				]),







			])


			


		])


]) #End Main Div


if __name__ == '__main__':
    app.run_server()



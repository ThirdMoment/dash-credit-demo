import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.css.append_css({"external_url": "https://rawgit.com/ThirdMoment/dash-credit-demo/master/develop/styles.css"})



app.layout = html.Div([

	html.Div([

				html.H5('Input application details:',
                    className='three columns',)
		

		],

		className= 'row'

		), #End table title


	html.Div(

		[

		html.Table([

			html.Tr([
				html.Th('Age:'),
				html.Th('Number of dependents'),
				]),

			html.Tr([
				html.Td(dcc.Input(id='age-id', value=30, type="number")),
				html.Td(dcc.Input(id='dependents-id', value=0, type="number")),
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
				html.Th('Total # open lines & loans'),
				html.Th('Total # real estate lines & loans'),
				]),

			html.Tr([
				html.Td(dcc.Input(id='total-lines-id', value=5, type="number")),
				html.Td(dcc.Input(id='real-estate-id', value=2, type="number")),				
				]),

			html.Tr([
				html.Th('Total utilization: revolving unsecured'),
				html.Th('Total # past due notice: 30-59 days'),
				]),

			html.Tr([
				html.Td(dcc.Input(id='revolving-id', value=0.5, type="number")),
				html.Td(dcc.Input(id='thirty-sixty-id', value=1, type="number")),			
				]),

			html.Tr([
				html.Th('Total # past due notice: 60-89 days'),
				html.Th('Total # past due notice: > 90 days'),
				]),

			html.Tr([
				html.Td(dcc.Input(id='soxty-ninety-id', value=1, type="number")),
				html.Td(dcc.Input(id='greater-ninety-id', value=0, type="number")),
				]),
			
		],
		className= 'three columns'
		),

		html.Div(
			[
				dcc.Graph(id='count_graph')
            ],
			 className='six columns',
			 #style={'margin-top': '10'}
        ),
	],
	className= 'row'
), # End input table

	],

    className='ten columns'


) #End Main Div


if __name__ == '__main__':
    app.run_server()



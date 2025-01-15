import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from insights import aggregate_insights

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("DynamoDB Analytics Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(id='user-activity-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60000,  # Refresh every 60 seconds
        n_intervals=0
    )
])

# Callback to dynamically update the graph
@app.callback(
    Output('user-activity-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    data = aggregate_insights()
    users = [d['user'] for d in data]
    counts = [d['count'] for d in data]

    figure = {
        'data': [
            {'x': users, 'y': counts, 'type': 'bar', 'name': 'User Activity'}
        ],
        'layout': {
            'title': 'User Activity Analytics',
            'xaxis': {'title': 'User ID'},
            'yaxis': {'title': 'Total Interactions'},
            'plot_bgcolor': '#f9f9f9',
            'paper_bgcolor': '#f9f9f9',
        }
    }
    return figure

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

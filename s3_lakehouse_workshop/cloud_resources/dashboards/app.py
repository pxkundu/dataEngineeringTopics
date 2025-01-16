import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from insights import aggregate_insights_by_event_type
from insights import aggregate_insights

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("DynamoDB Analytics Dashboard", style={'textAlign': 'center'}),
    
    # User Activity Bar Chart
    html.Div([
        html.H3("User Activity (Total Interactions)"),
        dcc.Graph(id='user-activity-graph'),
    ]),

    # Interaction Type per User
    html.Div([
        html.H3("Interaction Types Per User"),
        dcc.Graph(id='interaction-type-graph'),
    ]),

    # Auto-refresh
    dcc.Interval(
        id='interval-component',
        interval=60000,  # Refresh every 60 seconds
        n_intervals=0
    )
])

# Callback to dynamically update the User Activity graph
@app.callback(
    Output('user-activity-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_user_activity_graph(n_intervals):
    data = aggregate_insights()  # Fetch aggregated data
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

# Callback to dynamically update the Interaction Type graph
@app.callback(
    Output('interaction-type-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_interaction_type_graph(n_intervals):
    # Example data structure: [{'user': 'user_1', 'event_type': 'view', 'count': 10}, ...]
    data = aggregate_insights_by_event_type()
    
    users = list(set(d['user'] for d in data))
    event_types = list(set(d['event_type'] for d in data))

    # Create traces for each event type
    traces = []
    for event_type in event_types:
        counts = [
            d['count'] if d['event_type'] == event_type else 0
            for d in data if d['user'] in users
        ]
        traces.append({'x': users, 'y': counts, 'type': 'bar', 'name': event_type})

    figure = {
        'data': traces,
        'layout': {
            'title': 'Interaction Types Per User',
            'xaxis': {'title': 'User ID'},
            'yaxis': {'title': 'Interaction Count'},
            'barmode': 'stack',
            'plot_bgcolor': '#f9f9f9',
            'paper_bgcolor': '#f9f9f9',
        }
    }
    return figure

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

import dash  # version 1.13.1
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([
    html.H1('Sam Analytics'),
    html.Iframe(id='map', srcDoc=open('https://raw.githubusercontent.com/NandhiniRiya/Nisha-app-3/main/Rani_Parties%20(1).html', 'r').read(), width='100%', height='600'),
    html.Button(id='map-submit-button', n_clicks=0, children='Submit')
])
@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button', 'n_clicks')])
def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open('https://raw.githubusercontent.com/NandhiniRiya/Nisha-app-3/main/Rani_Parties%20(1).html', 'r').read()
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

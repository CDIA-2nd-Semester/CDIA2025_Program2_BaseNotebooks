from flask import Flask, render_template, jsonify
import json
import plotly.express as px
import pandas as pd
import os
import plotly


path_base=os.path.join(os.getcwd(), 'Unit_4', 'Week_2', 'tutorial', 'plotly_connection')

json_file_path = os.path.join(path_base, 'graph_1.json')

app = Flask(__name__)

@app.route('/')

def index():
    # # Load the data
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    
    # # Create a new column for Dolarization
    # df['Dolarization'] = df['year'].apply(lambda x: 'Dolarization' if x >= 2000 else 'Non-Dolarization')
    
    # # Create the plot
    # fig = px.scatter(df, x="year", y="gdpPercap", size="pop", color='Dolarization', log_x=False, size_max=30)
    # fig.update_layout(title="GDP per Capita in Ecuador Over Time", yaxis_title="GDP per Capita", xaxis_title="Year")
    # fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    
    
    with open(json_file_path, "r") as f:
        graph_json = f.read()
    
    
    return render_template('index.html', graphJSON=graph_json)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
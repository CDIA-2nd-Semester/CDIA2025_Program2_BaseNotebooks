from flask import Flask, render_template, jsonify
import os
import json
import plotly.express as px
import pandas as pd


path_base=os.path.join(os.getcwd(), 'Unit_4', 'Week_2', 'tutorial', 'plotly_connection')


# graph_json = json.load(open('graph.json', 'r'))



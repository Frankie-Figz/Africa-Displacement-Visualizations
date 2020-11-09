# import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pd
import json
from flask_cors import CORS

# create engine and connection to postgres
from sqlalchemy import create_engine

db_name = "africa_disaster_displacements"
engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/{db_name}')
connection = engine.connect()
connection

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    cards_json = get_data()
    cards_json_2 = get_data_2()
    cards_json_3 = get_data_3()
    return render_template("index.html", cards_to_js = cards_json, cards_to_js_2 = cards_json_2, cards_to_js_3 = cards_json_3)

@app.route("/api/data")
def get_data():
    # import SQL table as pandas dataframe
    cards_df = pd.read_sql('select "Hazard_Type", SUM("New_Displacements") as "Count_Displacement" from africa_disaster_displacements group by "Hazard_Type"', connection)
    # convert pandas dataframe to json
    cards_json = json.dumps(cards_df.to_dict('records'))
    
    return cards_json

@app.route("/api/data_2")
def get_data_2():
    # import SQL table as pandas dataframe
    cards_df_2 = pd.read_sql('select sum("New_Displacements") as displacements, "Year", "Country" from africa_disaster_displacements group by "Country", "Year"', connection)
    # convert pandas dataframe to json
    cards_json_2 = json.dumps(cards_df_2.to_dict('records'))
    
    return cards_json_2

@app.route("/api/data_3")
def get_data_3():
    # import SQL table as pandas dataframe
    cards_df_3 = pd.read_sql('select sum("New_Displacements") as total_displacements, "Country" from africa_disaster_displacements group by "Country"', connection)
    # convert pandas dataframe to json
    cards_json_3 = json.dumps(cards_df_3.to_dict('records'))
    
    return cards_json_3


if __name__ == "__main__":
    app.run(debug = True)
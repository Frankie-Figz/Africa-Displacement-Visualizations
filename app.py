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
    return render_template("index.html", cards_to_js = cards_json)

@app.route("/api/data")
def get_data():
    # import SQL table as pandas dataframe
    cards_df = pd.read_sql('select "Hazard_Type", SUM("New_Displacements") as "Count_Displacement" from africa_disaster_displacements group by "Hazard_Type"', connection)
    # convert pandas dataframe to json
    cards_json = json.dumps(cards_df.to_dict('records'))
    
    return cards_json

if __name__ == "__main__":
    app.run(debug = True)
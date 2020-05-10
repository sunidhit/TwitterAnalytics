from flask import Flask,render_template

import pandas as pd
import json


app = Flask(__name__)

@app.route("/")
def index():
    #df = pd.read_csv('/Users/sunidhibrajesh/PycharmProjects/TwitterAnalytics/Files/Global_Mobility_Report.csv')
    ob = {'Date':['2009-03-31','2009-03-30'],'High':[18.79,17.76]}
    df = pd.DataFrame(data=ob)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

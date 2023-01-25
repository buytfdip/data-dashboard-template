from fastapi import FastAPI, Response
from jinja2 import Environment, FileSystemLoader
import json
import plotly
import plotly.graph_objects as go

app = FastAPI()

@app.get("/")
def index():
    # Create the graph using Plotly
    fig = go.Figure(data=[go.Bar(y=[1, 2, 3])])

    # Convert the graph to a JSON object
    fig_json = json.dumps(fig.to_dict(), cls=plotly.utils.PlotlyJSONEncoder)

    # Load the filler data from the JSON file
    with open('filler_data.json') as f:
        filler_data = json.load(f)

    # Create the Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Render the template
    template = env.get_template("template.html")
    output = template.render(fig_json=fig_json, filler_data=filler_data)

    return Response(content=output, media_type="text/html")
    
    from fastapi import FastAPI, HTTPException
# from tastyworks_api import Tastyworks

# app = FastAPI()

# @app.get("/account-balance")
# async def account_balance():
#     try:
#         # Initialize Tastyworks object with email and password
#         tastyworks = Tastyworks("email", "password")
#         # Get account balance
#         account = tastyworks.account()
#         return {"balance": account.balance}
#     except HTTPException as e:
#         raise HTTPException(status_code=e.status_code, detail=e.detail)
##
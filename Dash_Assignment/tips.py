"""
Create a Dash application that predicts the tip amount based on user input.
Tasks
1. Train a simple Linear Regression model using:
○ total_bill
○ size
2. Create a Dash dashboard with:
○ Input box for total bill
○ Input box for number of people
○ Button to predict tip
3. Display the predicted tip on the dashboard
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from dash import Dash, html, dcc, Input, Output, State


# Train the model
tips = sns.load_dataset("tips")
X = tips[["total_bill", "size"]]
y = tips["tip"]
model = LinearRegression()
model.fit(X, y)


# Dash app
app = Dash(__name__)
app.layout = html.Div(
    [
        html.H1("Tip Predictor Dashboard"),
        html.Label("Total Bill ($):"),
        dcc.Input(id="total-bill", type="number", value=20, min=0, step=0.1),
        html.Br(),
        html.Br(),
        html.Label("Number of people:"),
        dcc.Input(id="size", type="number", value=2, min=1, step=1),
        html.Br(),
        html.Br(),
        html.Button("Predict Tip", id="predict-btn", n_clicks=0),
        html.Br(),
        html.Br(),
        html.Div(
            id="tip-output",
            style={
                "fontSize": 24,
                "color": "red",
                "border": "2px solid black",
                "padding": "10px",
                "width": "300px",
                "marginTop": "20px",
                "borderRadius": "8px",
                "backgroundColor": "#f9f9f9",
                "textAlign": "center",
            },
        ),
    ]
)


@app.callback(
    Output("tip-output", "children"),
    Input("predict-btn", "n_clicks"),
    State("total-bill", "value"),
    State("size", "value"),
)

# predict tip
def predict_tip(n_clicks, total_bill, size):
    if n_clicks > 0:
        prediction = model.predict([[total_bill, size]])[0]
        return f"Predicted Tip: ${prediction:.2f}"

    return ""


if __name__ == "__main__":
    app.run(debug=True)

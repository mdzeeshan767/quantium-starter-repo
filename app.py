import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample dataset (replace with your own CSV if needed)
data = {
    "date": pd.date_range(start="2024-01-01", periods=10),
    "sales": [120, 150, 170, 160, 180, 210, 190, 220, 240, 260],
    "region": ["north", "south", "east", "west", "north",
               "south", "east", "west", "north", "south"]
}
df = pd.DataFrame(data)

# Initialise app
app = dash.Dash(__name__)
app.title = "Pink Morsels Sales Visualiser"

# Layout
app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsels Sales Dashboard", className="title"),

        html.Div(
            className="controls",
            children=[
                html.Label("Select Region", className="label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="radio-group",
                ),
            ],
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        markers=True,
        title="Pink Morsels Sales Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        title_font_size=20,
        legend_title="Region",
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)

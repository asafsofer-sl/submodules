import plotly.graph_objects as go
import random

# generate some random sample datai
def print_plotly():
    points = 100
    x = [random.uniform(0, 10) for _ in range(points)]
    y = [random.uniform(0, 10) for _ in range(points)]
    category = [random.choice(["A", "B", "C"]) for _ in range(points)]

    color_map = {"A": "#1f77b4", "B": "#ff7f0e", "C": "#2ca02c"}
    colors = [color_map[group] for group in category]

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                mode="markers",
                marker={"color": colors, "size": 8, "opacity": 0.8},
                text=[f"Group {group}" for group in category],
                hovertemplate="%{text}<br>X: %{x:.2f}<br>Y: %{y:.2f}<extra></extra>",
            )
        ]
    )
    fig.update_layout(
        title="Random scatter (no NumPy/Pandas)",
        xaxis_title="X value",
        yaxis_title="Y value",
    )
    fig.show()


from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from PIL import Image

import geometry_tools

model_name_top1 = "/Users/danhle/SHREC2023/visualize_tool/dash-obj-in-3dmesh/data/obj/0a77cd2a91dfff53.obj" #.obj & .mtl files in data/obj
model_name_top5 = "/Users/danhle/SHREC2023/visualize_tool/dash-obj-in-3dmesh/data/obj/test.obj"
img_path = "/Users/danhle/SHREC2023/visualize_tool/dash-obj-in-3dmesh/data/obj/0d138c88827df428.jpg"

axis_template = {
    "showbackground": False,
    "visible" : False
}

plot_layout = {
    "title": "",
    "margin": {"t": 0, "b": 0, "l": 0, "r": 0},
    "font": {"size": 12, "color": "white"},
    "showlegend": False,
    'uirevision':'same_all_the_time', #this keeps camera position etc the same when data changes.
    "scene": {
        "xaxis": axis_template,
        "yaxis": axis_template,
        "zaxis": axis_template,
        "aspectmode" : "data",
        "camera": {"eye": {"x": 1.25, "y": 1.25, "z": 1.25}},
        "annotations": [],
    },
}

def layout():
 return html.Div([
    html.Img(src=Image.open(img_path)),
    html.Div([html.H1("Top1"),
    dcc.Graph(
          id="graph2",
          figure={
              "data": geometry_tools.import_geometry_filename([model_name_top1]),
              "layout": plot_layout,
          },
          config={"scrollZoom": True}, # activates wheel thingy on mouse to zoom and wotnot
      )])
    ,
    html.Div([html.H1("Top5"),
    dcc.Graph(
          id="graph",
          figure={
              "data": geometry_tools.import_geometry_filename([model_name_top5]),
              "layout": plot_layout,
          },
          config={"scrollZoom": True}, # activates wheel thingy on mouse to zoom and wotnot
      )])
    ])
      
app = Dash()
app.layout = layout

if __name__ == "__main__":
    app.run_server()
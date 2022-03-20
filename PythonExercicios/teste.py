from ipywidgets import widgets
from IPython.display import display

out = widgets.Output(layout={"color": "red", 'border': '1px solid blue', 'font-size': '200%'})

display(out)
with out:
    print(f"Alô mundo. Formatando número: {3.210002:0.02f}")

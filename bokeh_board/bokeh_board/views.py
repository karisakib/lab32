from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, FactorRange
import matplotlib.pyplot as plt

def index(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    fig = plt.figure(
        title="simple example", 
        x_axis_label='x', 
        y_axis_label='y'
    )

    fig.line(x, y, legend_label='s', line_width=2)

    script, div = components(fig)

    return render('index.html', {'script':script, 'div':div})

def handler404(request, exception):
       return render(request, '404.html')

def handler500(request):
       return render(request, '500.html')

def handler403(request, exception):
       return render(request, '403.html')

def handler400(request, exception):
       return render(request, '400.html')
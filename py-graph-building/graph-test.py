import os
from graphviz import Digraph

sink = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), os.pardir, 'latex', 'images'))

dot = Digraph('structs', comment='The Round Table')

dot.attr('node', shape='box')

dot.edge_attr.update(arrowhead='none')

dot.node('A', 'Sampling Algorithms for Sensor Data')
dot.node('B', 'Sampling Algorithms')
dot.node('C', 'Filtering Algorithms')

dot.node('D', 'Adaptive Sampling')
dot.node('E', 'Compressive Sampling')

dot.node('F', 'Model Based Schemes')
dot.node('G', 'Adaptive Filtering')

dot.edges(['AB', 'AC'])  # top edges
dot.edges(['BD', 'BE'])  # sampling edges
dot.edges(['CF', 'CG'])  # sampling edges

full_path = os.path.join(sink, 'taxonomy')

dot.render(full_path)
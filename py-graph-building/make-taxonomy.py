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

dot.node('H', 'Backcasting, Jain et al., \n USAC, EASA')
dot.node('I', 'CDG, EDCA, STCDG')
dot.node('J', 'BBQ, Ken, \n ASAP, Jiang et al.')
dot.node('K', 'Meng et al., Solis et al., \n Conch, CME')

dot.edges(['AB', 'AC'])  # top edges
dot.edges(['BD', 'BE'])  # sampling edges
dot.edges(['CF', 'CG'])  # filtering edges

dot.edges(['DH'])  # test edges
dot.edges(['EI'])  # test edges
dot.edges(['FJ'])  # test edges
dot.edges(['GK'])  # test edges

full_path = os.path.join(sink, 'taxonomy')

dot.render(full_path)

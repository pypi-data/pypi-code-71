"""
The :mod:`tsia.network_graphs` module includes methods that deals with the
network graph obtained from the Markov transition fields of a signal.
"""

from .ng import *

__all__ = [
    'get_network_graph', 
    'compute_network_graph_statistics',
    'get_modularity_encoding'
]
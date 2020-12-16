import itertools
from collections import defaultdict
from typing import Dict

from ether.core import Node, Capacity
from ether.util import parse_size_string

counters = defaultdict(lambda: itertools.count(0, 1))


def create_vm_node(name=None) -> Node:
    name = name if name is not None else 'cloudvm_%d' % next(counters['cloudvm'])

    return create_node(name=name,
                       cpus=4, arch='x86', mem='8167784Ki',
                       labels={
                           'ether.edgerun.io/type': 'vm',
                           'ether.edgerun.io/model': 'vm'
                       })


def create_server_node(name=None) -> Node:
    name = name if name is not None else 'server_%d' % next(counters['server'])

    return create_node(name=name,
                       cpus=88, arch='x86', mem='188G',
                       labels={
                           'ether.edgerun.io/type': 'server',
                           'ether.edgerun.io/model': 'server'
                       })


def create_rpi3_node(name=None) -> Node:
    name = name if name is not None else 'rpi3_%d' % next(counters['rpi3'])

    return create_node(name=name,
                       cpus=4, arch='arm32', mem='999036Ki',
                       labels={
                           'ether.edgerun.io/type': 'sbc',
                           'ether.edgerun.io/model': 'rpi3b+'
                       })


def create_nuc_node(name=None) -> Node:
    name = name if name is not None else 'nuc_%d' % next(counters['nuc'])

    return create_node(name=name,
                       cpus=4, arch='x86', mem='16Gi',
                       labels={
                           'ether.edgerun.io/type': 'sffc',
                           'ether.edgerun.io/model': 'nuci5'
                       })


def create_tx2_node(name=None) -> Node:
    name = name if name is not None else 'tx2_%d' % next(counters['tx2'])

    return create_node(name=name,
                       cpus=4, arch='aarch64', mem='8047252Ki',
                       labels={
                           'ether.edgerun.io/type': 'embai',
                           'ether.edgerun.io/model': 'nvidia_jetson_tx2',
                           'ether.edgerun.io/capabilities/cuda': '10',
                           'ether.edgerun.io/capabilities/gpu': 'pascal',
                       })


def create_node(name: str, cpus: int, mem: str, arch: str, labels: Dict[str, str]) -> Node:
    capacity = Capacity(cpu_millis=cpus * 1000, memory=parse_size_string(mem))
    return Node(name, capacity=capacity, arch=arch, labels=labels)


rpi3 = create_rpi3_node
nuc = create_nuc_node
tx2 = create_tx2_node
server = create_server_node

# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/103_models.MLP.ipynb (unless otherwise specified).

__all__ = ['MLP']

# Cell
from ..imports import *
from .layers import *

# Cell
class MLP(Module):
    def __init__(self, c_in, c_out, seq_len, layers=[500,500,500], ps=[0.1, 0.2, 0.2], act_cls=nn.ReLU(inplace=True),
                 use_bn=False, bn_final=False, lin_first=False, fc_dropout=0.5, y_range=None):
        layers, ps = L(layers), L(ps)
        if len(ps) <= 1: ps = ps * len(layers)
        assert len(layers) == len(ps), '#layers and #ps must match'
        self.flatten = Reshape(-1)
        nf = [c_in * seq_len] + layers
        self.mlp = nn.ModuleList()
        for i in range(len(layers)): self.mlp.append(LinBnDrop(nf[i], nf[i+1], bn=use_bn, p=ps[i], act=act_cls, lin_first=lin_first))
        _head = [LinBnDrop(nf[-1], c_out, bn=bn_final, p=fc_dropout)]
        if y_range is not None: _head.append(SigmoidRange(*y_range))
        self.head = nn.Sequential(*_head)

    def forward(self, x):
        x = self.flatten(x)
        for mlp in self.mlp: x = mlp(x)
        return self.head(x)
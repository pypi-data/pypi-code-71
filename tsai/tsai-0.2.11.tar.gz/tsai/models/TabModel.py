# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/120_models.TabModel.ipynb (unless otherwise specified).

__all__ = ['TabModel']

# Cell
from ..imports import *
from .layers import *

# Cell
class TabModel(Module):
    "Basic model for tabular data."
    def __init__(self, emb_szs, n_cont, out_sz, layers, ps=None, embed_p=0., y_range=None, use_bn=True, bn_final=False, bn_cont=True,
                 act_cls=nn.ReLU(inplace=True)):
        ps = ifnone(ps, [0.]*len(layers))
        if not is_listy(ps): ps = [ps]*len(layers)
        self.embeds = nn.ModuleList([Embedding(ni, nf) for ni,nf in emb_szs])
        self.emb_drop = nn.Dropout(embed_p)
        self.bn_cont = nn.BatchNorm1d(n_cont) if bn_cont else None
        n_emb = sum(e.embedding_dim for e in self.embeds)
        self.n_emb,self.n_cont = n_emb,n_cont
        sizes = [n_emb + n_cont] + layers + [out_sz]
        actns = [act_cls for _ in range(len(sizes)-2)]
        _layers = [LinBnDrop(sizes[i], sizes[i+1], bn=use_bn and (i!=len(actns)-1 or bn_final), p=p, act=a)
                       for i,(p,a) in enumerate(zip(ps,actns))]
        self.layers = nn.Sequential(*_layers)
        _head = [nn.Linear(layers[-1], out_sz)]
        self.head_nf = layers[-1]
        if y_range is not None: _head.append(SigmoidRange(*y_range))
        self.head = nn.Sequential(*_head)

    def forward(self, x_cat, x_cont=None):
        if self.n_emb != 0:
            x = [e(x_cat[:,i]) for i,e in enumerate(self.embeds)]
            x = torch.cat(x, 1)
            x = self.emb_drop(x)
        if self.n_cont != 0:
            if self.bn_cont is not None: x_cont = self.bn_cont(x_cont)
            x = torch.cat([x, x_cont], 1) if self.n_emb != 0 else x_cont
        x = self.layers(x)
        return self.head(x)
# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/011_callback.semi_supervised.ipynb (unless otherwise specified).

__all__ = ['NoisyStudent']

# Cell
from ..imports import *
from ..utils import *
from ..data.preprocessing import *
from ..data.transforms import *
from ..models.layers import *
from fastai.callback.all import *

# Cell
import torch.multiprocessing
torch.multiprocessing.set_sharing_strategy('file_system')

# Cell
class NoisyStudent(Callback):
    """A callback to implement the Noisy Student approach. In the original paper this was used in combination with noise:
        - stochastic depth: .8
        - RandAugment: N=2, M=27
        - dropout: .5

    Steps:
        1. Build the dl you will use as a teacher
        2. Create dl2 with the pseudolabels (either soft or hard preds)
        3. Pass any required batch_tfms to the callback

    """

    def __init__(self, dl2:DataLoader, bs:Optional[int]=None, l2pl_ratio:int=1, batch_tfms:Optional[list]=None, do_setup:bool=True,
                 pseudolabel_sample_weight:float=1., verbose=False):
        r'''
        Args:
            dl2:                       dataloader with the pseudolabels
            bs:                        batch size of the new, combined dataloader. If None, it will pick the bs from the labeled dataloader.
            l2pl_ratio:                ratio between labels and pseudolabels in the combined batch
            batch_tfms:                transforms applied to the combined batch. If None, it will pick the batch_tfms from the labeled dataloader (if any)
            do_setup:                  perform a transform setup on the labeled dataset.
            pseudolabel_sample_weight: weight of each pseudolabel sample relative to the labeled one of the loss.
        '''

        self.dl2, self.bs, self.l2pl_ratio, self.batch_tfms, self.do_setup, self.verbose = dl2, bs, l2pl_ratio, batch_tfms, do_setup, verbose
        self.pl_sw = pseudolabel_sample_weight

    def before_fit(self):
        if self.batch_tfms is None: self.batch_tfms = self.dls.train.after_batch
        self.old_bt = self.dls.train.after_batch # Remove and store dl.train.batch_tfms
        self.old_bs = self.dls.train.bs
        self.dls.train.after_batch = noop

        if self.do_setup and self.batch_tfms:
            for bt in self.batch_tfms:
                bt.setup(self.dls.train)

        if self.bs is None: self.bs = self.dls.train.bs
        self.dl2.bs = min(len(self.dl2.dataset), int(self.bs / (1 + self.l2pl_ratio)))
        self.dls.train.bs = self.bs - self.dl2.bs
        pv(f'labels / pseudolabels per training batch              : {self.dls.train.bs} / {self.dl2.bs}', self.verbose)
        rel_weight = (self.dls.train.bs/self.dl2.bs) * (len(self.dl2.dataset)/len(self.dls.train.dataset))
        pv(f'relative labeled/ pseudolabel sample weight in dataset: {rel_weight:.1f}', self.verbose)
        self.dl2iter = iter(self.dl2)

        self.old_loss_func = self.learn.loss_func
        self.learn.loss_func = self.loss

    def before_batch(self):
        if self.training:
            X, y = self.x, self.y
            try: X2, y2 = next(self.dl2iter)
            except StopIteration:
                self.dl2iter = iter(self.dl2)
                X2, y2 = next(self.dl2iter)
            if y.ndim == 1 and y2.ndim == 2: y = torch.eye(self.learn.dls.c)[y].to(device) # ensure both

            X_comb, y_comb = concat(X, X2), concat(y, y2)

            if self.batch_tfms is not None:
                X_comb = compose_tfms(X_comb, self.batch_tfms, split_idx=0)
                y_comb = compose_tfms(y_comb, self.batch_tfms, split_idx=0)
            self.learn.xb = (X_comb,)
            self.learn.yb = (y_comb,)
            pv(f'\nX: {X.shape}  X2: {X2.shape}  X_comb: {X_comb.shape}', self.verbose)
            pv(f'y: {y.shape}  y2: {y2.shape}  y_comb: {y_comb.shape}', self.verbose)

    def loss(self, output, target):
        if target.ndim == 2: _, target = target.max(dim=1)
        if self.training and self.pl_sw != 1:
            loss = (1 - self.pl_sw) * self.old_loss_func(output[:self.dls.train.bs], target[:self.dls.train.bs])
            loss += self.pl_sw * self.old_loss_func(output[self.dls.train.bs:], target[self.dls.train.bs:])
            return loss
        else:
            return self.old_loss_func(output, target)

    def after_fit(self):
        self.dls.train.after_batch = self.old_bt
        self.learn.loss_func = self.old_loss_func
        self.dls.train.bs = self.old_bs
        self.dls.bs = self.old_bs
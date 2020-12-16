"""
This is a wrapper class for Deep CCA
We create an instance with a method and number of latent dimensions.

The class has a number of methods intended to align roughly with the linear Wrapper:

fit(): gives us train correlations and stores the variables needed for out of sample prediction as well as some
method-specific variables

predict_corr(): allows us to predict the out of sample correlation for supplied views

predict_view(): allows us to predict a reconstruction of missing views from the supplied views

transform_view(): allows us to transform given views to the latent variable space

recon_loss(): gets the reconstruction loss for out of sample data - if the model has an autoencoder piece
"""

import copy

import numpy as np
import torch
from sklearn.cross_decomposition import CCA
from torch.utils.data import DataLoader

import cca_datasets
import cca_zoo.plot_utils
from cca_zoo.configuration import Config


class DeepWrapper:

    def __init__(self, config: Config = Config):
        self.config = config
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def fit(self, *args, labels=None, val_split=0.2):
        if type(args[0]) is np.ndarray:
            dataset = cca_datasets.CCA_Dataset(*args, labels=labels)
            lengths = [len(dataset) - int(len(dataset) * val_split), int(len(dataset) * val_split)]
            train_dataset, val_dataset = torch.utils.data.random_split(dataset, lengths)
        elif type(args[0]) is torch.utils.data.dataset.Subset and len(args) == 2:
            train_dataset, val_dataset = args[0], args[1]
        elif type(args[0]) is torch.utils.data.Dataset or type(args[0]) is torch.utils.data.dataset.Subset:
            dataset = args[0]
            lengths = [len(dataset) - int(len(dataset) * val_split), int(len(dataset) * val_split)]
            train_dataset, val_dataset = torch.utils.data.random_split(dataset, lengths)
        else:
            pass

        if self.config.batch_size == 0:
            train_dataloader = DataLoader(train_dataset, batch_size=len(train_dataset), drop_last=True)
        else:
            train_dataloader = DataLoader(train_dataset, batch_size=self.config.batch_size, drop_last=True)
        val_dataloader = DataLoader(val_dataset, batch_size=len(val_dataset))

        self.config.input_sizes = [view.shape[-1] for view in dataset[0][0]]

        # First we get the model class.
        # These have a forward method which takes data inputs and outputs the variables needed to calculate their
        # respective loss. The models also have loss functions as methods but we can also customise the loss by calling
        # a_loss_function(model(data))
        self.model = self.config.method(self.config)
        num_params = sum(p.numel() for p in self.model.parameters())
        print('total parameters: ', num_params)
        best_model = copy.deepcopy(self.model.state_dict())
        self.model.double().to(self.device)
        min_val_loss = torch.tensor(np.inf)
        epochs_no_improve = 0
        early_stop = False
        all_train_loss = []
        all_val_loss = []

        for epoch in range(1, self.config.epoch_num + 1):
            if not early_stop:
                epoch_train_loss = self.train_epoch(train_dataloader)
                print('====> Epoch: {} Average train loss: {:.4f}'.format(
                    epoch, epoch_train_loss))
                epoch_val_loss = self.val_epoch(val_dataloader)
                print('====> Epoch: {} Average val loss: {:.4f}'.format(
                    epoch, epoch_val_loss))

                if epoch_val_loss < min_val_loss or epoch == 1:
                    min_val_loss = epoch_val_loss
                    best_model = copy.deepcopy(self.model.state_dict())
                    print('Min loss %0.2f' % min_val_loss)
                    epochs_no_improve = 0

                else:
                    epochs_no_improve += 1
                    # Check early stopping condition
                    if epochs_no_improve == self.config.patience and self.config.patience > 0:
                        print('Early stopping!')
                        early_stop = True
                        self.model.load_state_dict(best_model)

                all_train_loss.append(epoch_train_loss)
                all_val_loss.append(epoch_val_loss)
        cca_zoo.plot_utils.plot_training_loss(all_train_loss, all_val_loss)
        if not self.config.autoencoder:
            self.train_correlations = self.predict_corr(train_dataset, train=True)
        return self

    def train_epoch(self, train_dataloader: torch.utils.data.DataLoader):
        self.model.train()
        train_loss = 0
        for batch_idx, (data, label) in enumerate(train_dataloader):
            data = [d.to(self.device) for d in list(data)]
            loss = self.model.update_weights(*data)
            train_loss += loss.item()
        return train_loss / len(train_dataloader)

    def val_epoch(self, val_dataloader: torch.utils.data.DataLoader):
        self.model.eval()
        with torch.no_grad():
            total_val_loss = 0
            for batch_idx, (data, label) in enumerate(val_dataloader):
                data = [d.to(self.device) for d in list(data)]
                loss = self.model.loss(*data)
                total_val_loss += loss.item()
        return total_val_loss / len(val_dataloader)

    def predict_corr(self, *args, train=False):
        z_list = self.transform_view(*args, train=train)
        correlations = np.diag(
            np.corrcoef(z_list[0], z_list[1], rowvar=False)[:self.config.latent_dims, self.config.latent_dims:])
        return correlations

    def transform_view(self, *args, labels=None, train=False):
        if type(args[0]) is np.ndarray:
            test_dataset = cca_datasets.CCA_Dataset(*args, labels=labels)
        elif type(args[0]) is torch.utils.data.Dataset or type(args[0]) is torch.utils.data.dataset.Subset:
            test_dataset = args[0]
        else:
            pass
        test_dataloader = DataLoader(test_dataset, batch_size=len(test_dataset))
        with torch.no_grad():
            for batch_idx, (data, label) in enumerate(test_dataloader):
                data = [d.to(self.device) for d in list(data)]
                z = self.model(*data)
                if batch_idx == 0:
                    z_list = [z_i.detach().cpu().numpy() for i, z_i in enumerate(z)]
                else:
                    z_list = [np.append(z_list[i], z_i.detach().cpu().numpy(), axis=0) for
                              i, z_i in enumerate(z)]
        # For trace-norm objective models we need to apply a linear CCA to outputs
        if self.config.post_transform:
            if train:
                self.cca = CCA(n_components=self.config.latent_dims)
                z_list = self.cca.fit_transform(z_list[0], z_list[1])
            else:
                z_list = self.cca.transform(np.array(z_list[0]), np.array(z_list[1]))
        return z_list

    def predict_view(self, *args, labels=None):
        if type(args[0]) is np.ndarray:
            test_dataset = cca_datasets.CCA_Dataset(*args, labels=labels)
        elif type(args[0]) is torch.utils.data.Dataset or type(args[0]) is torch.utils.data.dataset.Subset:
            test_dataset = args[0]
        else:
            pass
        test_dataloader = DataLoader(test_dataset, batch_size=len(test_dataset))
        with torch.no_grad():
            for batch_idx, (data, label) in enumerate(test_dataloader):
                data = [d.to(self.device) for d in list(data)]
                x = self.model.recon(*data)
                if batch_idx == 0:
                    x_list = [x_i.detach().cpu().numpy() for i, x_i in enumerate(x)]
                else:
                    x_list = [np.append(x_list[i], x_i.detach().cpu().numpy(), axis=0) for
                              i, x_i in enumerate(x)]
        return x_list

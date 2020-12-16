#! /usr/bin/env python

# Copyright (C) 2018  Charlie Hoy <charlie.hoy@ligo.org>
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
import pesummary
from pesummary.gw.file.read import read as GWRead
from pesummary.gw.pepredicates import PEPredicates
from pesummary.gw.p_astro import PAstro
from pesummary.utils.utils import make_dir, logger
from pesummary.utils.exceptions import InputError
import argparse


__doc__ = """This executable is used to generate a txt file containing the
source classification probailities"""


def command_line():
    """Generate an Argument Parser object to control the command line options
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-w", "--webdir", dest="webdir",
                        help="make page and plots in DIR", metavar="DIR",
                        default=None)
    parser.add_argument("-s", "--samples", dest="samples",
                        help="Posterior samples hdf5 file", nargs='+',
                        default=None)
    parser.add_argument("--labels", dest="labels",
                        help="labels used to distinguish runs", nargs='+',
                        default=None)
    parser.add_argument("--prior", dest="prior",
                        choices=["population", "default", "both"],
                        default="both",
                        help=("Prior to use when calculating source "
                              "classification probabilities"))
    parser.add_argument("--plot", dest="plot",
                        help="name of the plot you wish to make",
                        default="bar", choices=["bar", "mass_1_mass_2"])
    return parser


def generate_probabilities(result_files, prior="both"):
    """Generate the classification probabilities

    Parameters
    ----------
    result_files: list
        list of result files
    prior: str
        prior you wish to reweight your samples too
    """
    classifications = []

    for num, i in enumerate(result_files):
        mydict = {}
        f = GWRead(i)
        if not isinstance(f, pesummary.gw.file.formats.pesummary.PESummary):
            f.generate_all_posterior_samples()
            mydict["default"], mydict["population"] = \
                PEPredicates.classifications(f.samples, f.parameters)
            em_bright = PAstro.classifications(f.samples_dict)
        else:
            label = f.labels[0]
            mydict["default"], mydict["population"] = \
                PEPredicates.classifications(f.samples[0], f.parameters[0])
            em_bright = PAstro.classifications(f.samples_dict[label])
        mydict["default"].update(em_bright[0])
        mydict["population"].update(em_bright[1])
        classifications.append(mydict)
    if prior == "both":
        return classifications
    return [{prior: i[prior]} for i in classifications]


def save_classifications(savedir, classifications, labels):
    """Read and return a list of parameters and samples stored in the result
    files

    Parameters
    ----------
    result_files: list
        list of result files
    classifications: dict
        dictionary of classification probabilities
    """
    import os
    import json

    base_path = os.path.join(savedir, "{}_{}_prior_pe_classification.json")
    for num, i in enumerate(classifications):
        for prior in i.keys():
            with open(base_path.format(labels[num], prior), "w") as f:
                json.dump(i[prior], f)


def make_plots(
    result_files, webdir=None, labels=None, prior=None, plot_type="bar",
    probs=None
):
    """Save the plots generated by PEPredicates

    Parameters
    ----------
    result_files: list
        list of result files
    webdir: str
        path to save the files
    labels: list
        lisy of strings to identify each result file
    prior: str
        Either 'default' or 'population'. If 'population' the samples are reweighted
        to a population prior
    plot_type: str
        The plot type that you wish to make
    probs: dict
        Dictionary of classification probabilities
    """
    if webdir is None:
        webdir = "./"

    for num, i in enumerate(result_files):
        if labels is None:
            label = num
        else:
            label = labels[num]
        f = GWRead(i)
        if not isinstance(f, pesummary.gw.file.formats.pesummary.PESummary):
            f.generate_all_posterior_samples()
        if plot_type == "bar":
            from pesummary.gw.plots.plot import _classification_plot

            if prior == "default" or prior == "both":
                fig = _classification_plot(probs[num]["default"])
                fig.savefig(
                    os.path.join(
                        webdir,
                        "{}_default_pepredicates_bar.png".format(label)
                    )
                )
            if prior == "population" or prior == "both":
                fig = _classification_plot(probs[num]["population"])
                fig.savefig(
                    os.path.join(
                        webdir,
                        "{}_population_pepredicates_bar.png".format(label)
                    )
                )
        elif plot_type == "mass_1_mass_2":
            if prior == "default" or prior == "both":
                fig = PEPredicates.plot(
                    f.samples, f.parameters, population_prior=False
                )
                fig.savefig(
                    os.path.join(
                        webdir, "{}_default_pepredicates.png".format(label)
                    )
                )
            if prior == "population" or prior == "both":
                fig = PEPredicates.plot(f.samples, f.parameters)
                fig.savefig(
                    os.path.join(
                        webdir, "{}_population_pepredicates.png".format(label)
                    )
                )


def main(args=None):
    """Top level interface for `summarypublication`
    """
    parser = command_line()
    opts = parser.parse_args(args=args)
    if opts.webdir:
        make_dir(opts.webdir)
    else:
        logger.warning(
            "No webdir given so plots will not be generated and "
            "classifications will be shown in stdout rather than saved to file"
        )
    classifications = generate_probabilities(opts.samples, prior=opts.prior)
    if opts.labels is None:
        opts.labels = []
        for i in opts.samples:
            f = GWRead(i)
            if hasattr(f, "labels"):
                opts.labels.append(f.labels[0])
            else:
                raise InputError("Please provide a label for each result file")
    if opts.webdir:
        save_classifications(opts.webdir, classifications, opts.labels)
    else:
        print(classifications)
        return
    if opts.plot == "bar":
        probs = classifications
    else:
        probs = None
    make_plots(
        opts.samples, webdir=opts.webdir, labels=opts.labels, prior=opts.prior,
        plot_type=opts.plot, probs=probs
    )


if __name__ == "__main__":
    main()

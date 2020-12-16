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

import numpy as np
from pesummary.utils.utils import check_filename


def _parameters_and_samples_from_structured_array(array):
    """Return the parameters and samples stored in a structured array

    Parameters
    ----------
    array: numpy.ndarray
        structured array containing the parameters and samples. Each column
        should correspond to the samples for a single distribution
    """
    parameters = list(array.dtype.names)
    array = np.atleast_1d(array)
    samples = array.view((float, len(array.dtype.names)))
    return parameters, samples


def genfromtxt(path, **kwargs):
    """Return the parameters and samples stored in a `txt` file

    Parameters
    ----------
    path: str
        path to the result file you wish to read in
    **kwargs: dict, optional
        all additional kwargs are passed to the `np.genfromtxt` function
    """
    data = np.genfromtxt(path, **kwargs)
    return _parameters_and_samples_from_structured_array(data)


def read_numpy(path, **kwargs):
    """Grab the parameters and samples in a .npy file

    Parameters
    ----------
    path: str
        path to the result file you wish to read in
    **kwargs: dict, optional
        all additional kwargs are passed to the `np.load` function
    """
    data = np.load(path, **kwargs)
    return _parameters_and_samples_from_structured_array(data)


def _write_numpy(
    parameters, samples, outdir="./", label=None, filename=None, overwrite=False,
    default_filename="pesummary_{}.npy", **kwargs
):
    """Write a set of samples to a csv file

    Parameters
    ----------
    parameters: list
        list of parameters
    samples: 2d list
        list of samples. Columns correspond to a given parameter
    outdir: str, optional
        directory to write the dat file
    label: str, optional
        The label of the analysis. This is used in the filename if a filename
        if not specified
    filename: str, optional
        The name of the file that you wish to write
    overwrite: Bool, optional
        If True, an existing file of the same name will be overwritten
    """
    from pesummary.utils.samples_dict import SamplesDict

    filename = check_filename(
        default_filename=default_filename, outdir=outdir, label=label,
        filename=filename, overwrite=overwrite
    )
    _array = SamplesDict(
        parameters, np.array(samples).T
    ).to_structured_array()
    np.save(filename, _array)


def write_numpy(
    parameters, samples, outdir="./", label=None, filename=None, overwrite=False,
    **kwargs
):
    """Write a set of samples to a npy file

    Parameters
    ----------
    parameters: nd list
        list of parameters
    samples: nd list
        list of samples. Columns correspond to a given parameter
    outdir: str, optional
        directory to write the csv file
    label: str, optional
        The label of the analysis. This is used in the filename if a filename
        if not specified
    filename: str, optional
        The name of the file that you wish to write
    overwrite: Bool, optional
        If True, an existing file of the same name will be overwritten
    """
    from pesummary.io.write import _multi_analysis_write

    _multi_analysis_write(
        _write_numpy, parameters, samples, outdir=outdir, label=label,
        filename=filename, overwrite=overwrite, file_format="numpy", **kwargs
    )

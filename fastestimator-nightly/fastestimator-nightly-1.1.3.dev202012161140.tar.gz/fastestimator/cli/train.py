# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional

from fastestimator import Estimator
from fastestimator.cli.cli_util import parse_cli_to_dictionary


def _get_estimator(args: Dict[str, Any], unknown: Optional[List[str]]) -> Estimator:
    """A helper method to invoke the get_estimator method from a file using provided command line arguments as input.

    Args:
        args: A dictionary containing location of the FE file under the 'entry_point' key, as well as an optional
            'hyperparameters_json' key if the user is storing their parameters in a file.
        unknown: The remainder of the command line arguments to be passed along to the get_estimator() method.

    Returns:
        The estimator generated by a file's get_estimator() function.
    """
    entry_point = args['entry_point']
    hyperparameters = {}
    if args['hyperparameters_json']:
        hyperparameters = os.path.abspath(args['hyperparameters_json'])
        with open(hyperparameters, 'r') as f:
            hyperparameters = json.load(f)
    hyperparameters.update(parse_cli_to_dictionary(unknown))
    module_name = os.path.splitext(os.path.basename(entry_point))[0]
    dir_name = os.path.abspath(os.path.dirname(entry_point))
    sys.path.insert(0, dir_name)
    spec_module = __import__(module_name, globals(), locals(), ["get_estimator"])
    return spec_module.get_estimator(**hyperparameters)


def train(args: Dict[str, Any], unknown: Optional[List[str]]) -> None:
    """Load an Estimator from a file and invoke its .fit() method.

    Args:
        args: A dictionary containing location of the FE file under the 'entry_point' key, as well as an optional
            'hyperparameters_json' key if the user is storing their parameters in a file.
        unknown: The remainder of the command line arguments to be passed along to the get_estimator() method.
    """
    estimator = _get_estimator(args, unknown)
    warmup_option = {"true": True, "false": False, "debug": "debug"}
    estimator.fit(warmup=warmup_option[args['warmup'].lower()], summary=args['summary'])


def test(args: Dict[str, Any], unknown: Optional[List[str]]) -> None:
    """Load an Estimator from a file and invoke its .test() method.

    Args:
        args: A dictionary containing location of the FE file under the 'entry_point' key, as well as an optional
            'hyperparameters_json' key if the user is storing their parameters in a file.
        unknown: The remainder of the command line arguments to be passed along to the get_estimator() method.
    """
    estimator = _get_estimator(args, unknown)
    estimator.test(summary=args['summary'])


def configure_train_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add a training parser to an existing argparser.

    Args:
        subparsers: The parser object to be appended to.
    """
    parser = subparsers.add_parser('train',
                                   description='Train a FastEstimator model',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                   allow_abbrev=False)
    # use an argument group for required flag arguments since otherwise they will show up as optional in the help
    parser.add_argument('entry_point', type=str, help='The path to the model python file')
    parser.add_argument('--hyperparameters',
                        dest='hyperparameters_json',
                        type=str,
                        help="The path to the hyperparameters JSON file")
    parser.add_argument('--warmup', type=str, help="Warmup setting, can be true, false or debug", default="true")
    parser.add_argument('--summary', type=str, help="Experiment name", default=None)
    parser.add_argument_group(
        'hyperparameter arguments',
        'Arguments to be passed through to the get_estimator() call. \
        Examples might look like --epochs <int>, --batch_size <int>, --optimizer <str>, etc...')
    parser.set_defaults(func=train)


def configure_test_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add a testing parser to an existing argparser.

    Args:
        subparsers: The parser object to be appended to.
    """
    parser = subparsers.add_parser('test',
                                   description='Test a FastEstimator model',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                   allow_abbrev=False)
    # use an argument group for required flag arguments since otherwise they will show up as optional in the help
    parser.add_argument('entry_point', type=str, help='The path to the model python file')
    parser.add_argument('--hyperparameters',
                        dest='hyperparameters_json',
                        type=str,
                        help="The path to the hyperparameters JSON file")
    parser.add_argument('--summary', type=str, help="Experiment name", default=None)
    parser.add_argument_group(
        'hyperparameter arguments',
        'Arguments to be passed through to the get_estimator() call. \
        Examples might look like --epochs <int>, --batch_size <int>, --optimizer <str>, etc...')
    parser.set_defaults(func=test)

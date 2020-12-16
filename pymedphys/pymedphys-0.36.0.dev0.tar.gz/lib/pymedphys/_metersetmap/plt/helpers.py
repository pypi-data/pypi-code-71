# Copyright (C) 2018 Simon Biggs

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pymedphys._imports import numpy as np


def pcolormesh_grid(x, y, grid_resolution=None):
    if grid_resolution is None:
        diffs = np.hstack([np.diff(x), np.diff(y)])
        assert np.all(np.abs(diffs - diffs[0]) < 10 ** -12)

        grid_resolution = diffs[0]

    new_x = np.concatenate([x - grid_resolution / 2, [x[-1] + grid_resolution / 2]])
    new_y = np.concatenate([y - grid_resolution / 2, [y[-1] + grid_resolution / 2]])

    return new_x, new_y

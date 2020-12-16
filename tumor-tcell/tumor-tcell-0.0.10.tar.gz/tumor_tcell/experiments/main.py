"""
========================
Tumor/T-cell Experiments
========================

Experiments can be triggered from the command line:

```
$ python tumor_tcell/experiments/main.py [experiment_name]
```
"""

import random

# vivarium-core imports
from vivarium.core.composition import (
    agent_environment_experiment,
    make_agent_ids,
    compose_experiment,
    GENERATORS_KEY,
    EXPERIMENT_OUT_DIR,
)
from vivarium.library.units import units, remove_units
from vivarium.core.control import Control

# plots
from vivarium.plots.agents_multigen import plot_agents_multigen
from vivarium_cell.plots.multibody_physics import plot_tags, plot_snapshots

# tumor-tcell imports
from tumor_tcell.composites.tumor_agent import TumorAgent
from tumor_tcell.composites.t_cell_agent import TCellAgent
from tumor_tcell.composites.tumor_microenvironment import TumorMicroEnvironment

# global parameters
TIMESTEP = 60
NBINS = [10, 10]
DEPTH = 10  # um
BOUNDS = [200 * units.um, 200 * units.um]

TUMOR_ID = 'tumor'
TCELL_ID = 'tcell'


def get_tcells(number=1):
    return {
    '{}_{}'.format(TCELL_ID, n): {
        #'location': [x, y],
        'type': 'tcell',
        'cell_state': 'PD1n',
        #'PD1': 0,
        #'TCR':50000,
        'velocity': 10.0 * units.um/units.min,
        'diameter': 5 * units.um,
    } for n in range(number)
}

def get_tumors(number=1):
    return {
        '{}_{}'.format(TUMOR_ID, n): {
            # 'location': [x, y],
            'type': 'tumor',
            'cell_state': 'PDL1n' if random.uniform(0, 1) < 0.5 else 'PDL1p',
            # 'PDL1': 50000,
            # 'MHCI': 50000,
            'diameter': 10 * units.um,
        } for n in range(number)
    }

def random_location(bounds):
    return [
        random.uniform(0, bounds[0]),
        random.uniform(0, bounds[1])]

# make defaults
N_TUMORS = 50
N_TCELLS = 3
DEFAULT_TUMORS = get_tumors(number=N_TUMORS)
DEFAULT_TCELLS = get_tcells(number=N_TCELLS)


# simulation # 1
def tumor_tcell_abm(
    bounds=BOUNDS,
    n_bins=NBINS,
    depth=DEPTH,
    field_molecules=['IFNg'],
    tumors=DEFAULT_TUMORS,
    tcells=DEFAULT_TCELLS,
    total_time=50000,
    time_step=TIMESTEP,
):

    ## configure the cells
    # t-cell configuration
    t_cell_hierarchy = {
        agent_id: {
            GENERATORS_KEY: {
                'type': TCellAgent,
                'config': {
                    'time_step': time_step,
                    'agent_id': agent_id,
                }
            }
        } for agent_id in tcells.keys()
    }

    # tumor configuration
    tumor_hierarchy = {
        agent_id: {
            GENERATORS_KEY: {
                'type': TumorAgent,
                'config': {
                    'time_step': time_step,
                    'agent_id': agent_id,
                }
            }
        } for agent_id in tumors.keys()
    }

    # declare the full hierarchy with the environments
    hierarchy = {
        # generate the tumor micro-environment at the top level
        GENERATORS_KEY: {
            'type': TumorMicroEnvironment,
            'config': {
                'neighbors_multibody': {
                    'time_step': time_step,
                    'bounds': bounds,
                    'jitter_force': 5e-4,
                },
                'diffusion_field': {
                    'time_step': time_step,
                    'molecules': field_molecules,
                    'bounds': bounds,
                    'n_bins': n_bins,
                    'depth': depth,
                }
            }
        },
        # cells are one level down, under the 'agents' key
        'agents': {**t_cell_hierarchy, **tumor_hierarchy}
    }

    # make environment instance to get an initial state
    environment = TumorMicroEnvironment(hierarchy[GENERATORS_KEY]['config'])
    initial_env = environment.initial_state({'uniform': 0.0})

    # initialize state
    initial_t_cells = {
        agent_id: {
            'boundary': {
                'location': state.get('location', random_location(bounds)),
                'diameter': state.get('diameter', 10 * units.um),
                'velocity': state.get('velocity', 0.0 * units.um/units.min),
            },
            'internal': {
                'cell_state': state.get('cell_state', None)
            },
            'neighbors': {
                'present': {
                    'PD1': state.get('PD1', None),
                    'TCR': state.get('TCR', 50000)
                }
            },
        } for agent_id, state in tcells.items()
    }
    initial_tumors = {
        agent_id: {
            'internal': {
                'cell_state': state.get('cell_state', None)
            },
            'boundary': {
                'location': state.get('location', random_location(bounds)),
                'diameter': state.get('diameter', 20 * units.um),
                'velocity': state.get('velocity', 0.0 * units.um/units.min),
            },
            'neighbors': {
                'present': {
                    'PDL1': state.get('PDL1', None),
                    'MHCI': state.get('MHCI', None)
                }
            },
        } for agent_id, state in tumors.items()
    }
    initial_state = {
        **initial_env,
        'agents': {
            **initial_t_cells, **initial_tumors}
    }

    # configure the simulation experiment
    experiment = compose_experiment(
        hierarchy=hierarchy,
        initial_state=initial_state)

    # run simulation
    experiment.update(total_time)
    data = experiment.emitter.get_data_deserialized()
    experiment.end()

    return data


def small_experiment():
    return tumor_tcell_abm(
        tumors=get_tumors(number=2),
        tcells=get_tcells(number=2),
        total_time=1000,
    )



def plots_suite(data, out_dir=None, bounds=BOUNDS):
    # separate out tcell and tumor data for multigen plots
    tcell_data = {}
    tumor_data = {}
    for time, time_data in data.items():
        all_agents_data = time_data['agents']
        tcell_data[time] = {
            'agents': {
                agent_id: agent_data
                for agent_id, agent_data in all_agents_data.items()
                if TCELL_ID in agent_id}}
        tumor_data[time] = {
            'agents': {
                agent_id: agent_data
                for agent_id, agent_data in all_agents_data.items()
                if TUMOR_ID in agent_id}}

    # make multigen plot for tcells and tumors
    plot_settings = {
        'skip_paths': [
            ('boundary', 'diameter'),
            ('boundary', 'location'),
        ]
    }
    fig1 = plot_agents_multigen(tcell_data, plot_settings, out_dir, TCELL_ID)
    fig2 = plot_agents_multigen(tumor_data, plot_settings, out_dir, TUMOR_ID)

    # snapshots plot
    # extract data
    env_config = {'bounds': remove_units(bounds)}
    agents = {time: time_data['agents'] for time, time_data in data.items()}
    fields = {time: time_data['fields'] for time, time_data in data.items()}
    plot_data = {
        'agents': remove_units(agents),
        'fields': fields,
        'config': env_config}
    plot_config = {
        'fields': [],
        'n_snapshots': 8,
        'agent_shape': 'circle',
        'out_dir': out_dir}
    fig3 = plot_snapshots(plot_data, plot_config)


    return fig1, fig2, fig3

# all of the experiments go here for easy access by control class
experiments_library = {
    '1': tumor_tcell_abm,
    '2': small_experiment,
}
plots_library = {
    '1': plots_suite,
}
workflow_library = {
    '1': {
        'name': 'tumor_tcell_experiment',
        'experiment': '1',
        'plots': ['1'],
    },
    '2': {
        'name': 'small_experiment',
        'experiment': '2',
        'plots': ['1'],
    },
}

if __name__ == '__main__':
    Control(
        experiments=experiments_library,
        plots=plots_library,
        workflows=workflow_library,
    )

from gradient_free_optimizers import (
    HillClimbingOptimizer,
    StochasticHillClimbingOptimizer,
    TabuOptimizer,
    RandomSearchOptimizer,
    RandomRestartHillClimbingOptimizer,
    RandomAnnealingOptimizer,
    SimulatedAnnealingOptimizer,
    ParallelTemperingOptimizer,
    ParticleSwarmOptimizer,
    EvolutionStrategyOptimizer,
    BayesianOptimizer,
    TreeStructuredParzenEstimators,
    DecisionTreeOptimizer,
    EnsembleOptimizer,
)

optimizers_singleOpt = (
    "Optimizer",
    [
        (HillClimbingOptimizer),
        (StochasticHillClimbingOptimizer),
        (TabuOptimizer),
        (RandomSearchOptimizer),
        (RandomRestartHillClimbingOptimizer),
        (RandomAnnealingOptimizer),
        (SimulatedAnnealingOptimizer),
    ],
)

optimizers_PopBased = (
    "Optimizer",
    [
        (ParallelTemperingOptimizer),
        (ParticleSwarmOptimizer),
        (EvolutionStrategyOptimizer),
    ],
)

optimizers_noSBOM = (
    "Optimizer",
    [
        (HillClimbingOptimizer),
        (StochasticHillClimbingOptimizer),
        (TabuOptimizer),
        (RandomSearchOptimizer),
        (RandomRestartHillClimbingOptimizer),
        (RandomAnnealingOptimizer),
        (SimulatedAnnealingOptimizer),
        (ParallelTemperingOptimizer),
        (ParticleSwarmOptimizer),
        (EvolutionStrategyOptimizer),
    ],
)

optimizers_SBOM = (
    "Optimizer",
    [
        (BayesianOptimizer),
        (TreeStructuredParzenEstimators),
        (DecisionTreeOptimizer),
        (EnsembleOptimizer),
    ],
)

optimizers_local = (
    "Optimizer",
    [
        (HillClimbingOptimizer),
        (StochasticHillClimbingOptimizer),
        (TabuOptimizer),
        (SimulatedAnnealingOptimizer),
        (ParallelTemperingOptimizer),
        (ParticleSwarmOptimizer),
        (EvolutionStrategyOptimizer),
    ],
)


optimizers = (
    "Optimizer",
    [
        (HillClimbingOptimizer),
        (StochasticHillClimbingOptimizer),
        (TabuOptimizer),
        (RandomSearchOptimizer),
        (RandomRestartHillClimbingOptimizer),
        (RandomAnnealingOptimizer),
        (SimulatedAnnealingOptimizer),
        (ParallelTemperingOptimizer),
        (ParticleSwarmOptimizer),
        (EvolutionStrategyOptimizer),
        (BayesianOptimizer),
        (TreeStructuredParzenEstimators),
        (DecisionTreeOptimizer),
        (EnsembleOptimizer),
    ],
)

from enum import Enum
from math import erf, sqrt
from typing import List, Tuple

from matplotlib.pylab import rand


class DistributionType(Enum):
    RANDOM = 1
    UNIFORM = 2
    NORMAL = 3

def getRandomDistribution() -> Tuple[float]:
    distribution: List[float] = []

    sum: float = 0
    for i in range(11):
        distribution.append(rand())
        sum += distribution[i]
    
    for i in range(11):
        distribution[i] /= sum
    
    return tuple(distribution)

def getUniformDistribution() -> Tuple[float]:
    distribution: List[float] = []
    for i in range(11):
        distribution.append(1 / 11)
    
    return tuple(distribution)

def getNormalDistribution() -> Tuple[float]:
    distribution: List[float] = []
    mean: float = rand()
    shape: float = rand() * 0.4

    def cdf(x: int) -> float:
        return (1 + erf((x - mean) / (shape * sqrt(2)))) / 2

    distribution.append(cdf(1 / 11))
    for i in range(9):
        distribution.append(cdf((i + 2) / 11) - cdf((i + 1) / 11))
    distribution.append(1 - cdf(1))
    
    return tuple(distribution)

def getDistribution(distributionMethod: DistributionType) -> Tuple[float]:
    match distributionMethod:
        case DistributionType.UNIFORM:
            return getUniformDistribution()
        case DistributionType.NORMAL:
            return getNormalDistribution()
        case _: # Random
            return getRandomDistribution()

def sampleDistribution(distribution: Tuple[float]) -> int:
    sample: float = rand()

    sum: float = 0
    for rating, mass in enumerate(distribution):
        sum += mass
        if sample <= sum:
            return rating
    
    return 10

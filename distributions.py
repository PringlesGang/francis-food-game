from enum import Enum
from typing import List, Tuple

from matplotlib.pylab import rand


class DistributionType(Enum):
    RANDOM = 1

def getRandomDistribution() -> Tuple[float]:
    distribution: List[float] = []

    sum: float = 0
    for i in range(11):
        distribution.append(rand())
        sum += distribution[i]
    
    for i in range(11):
        distribution[i] /= sum
    
    return tuple(distribution)

def getDistribution(distributionMethod: DistributionType) -> Tuple[float]:
    match distributionMethod:
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
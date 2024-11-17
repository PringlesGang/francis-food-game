from typing import List, Tuple
import pandas as pd

from distributions import DistributionType, getDistribution, sampleDistribution
from predictions import PredictionType, getPrediction


PredictionMethod: PredictionType = PredictionType.SAMPLE_MEAN
DistributionMethod: DistributionType = DistributionType.RANDOM

def readData() -> pd.DataFrame:
    return pd.read_csv("./data.csv")

def runTest(rounds: int, log: bool) -> int:
    distributionOpa: Tuple[float] = getDistribution(DistributionMethod)
    distributionOma: Tuple[float] = getDistribution(DistributionMethod)

    if log:
        print(f"Distribution opa: {distributionOpa}")
        print(f"Distribution oma: {distributionOma}")
        print()

    dataOpa: pd.DataFrame = pd.DataFrame()
    dataOma: pd.DataFrame = pd.DataFrame()

    score: int = 0
    for i in range(rounds):
        prediction: int = getPrediction(PredictionMethod, dataOpa, dataOma, False)

        opaRating: int = sampleDistribution(distributionOpa)
        omaRating: int = sampleDistribution(distributionOma)
        dataOpa[-1] = [opaRating]
        dataOma[-1] = [omaRating]
        rating: int = opaRating + omaRating

        score -= abs(prediction - rating)

        if log:
            print(f"{i}: \tPrediction={prediction} \tOpa={opaRating} \tOma={omaRating} \tTotal={rating} \tScore={score}")
    
    return score

def runManyTests(tests: int, rounds: int) -> None:
    results: List[int] = []

    sum: int = 0
    for i in range(tests):
        results.append(runTest(rounds, False))
        sum += results[i]
    
    print(results)
    print(f"Average score: {sum / tests} \tAverage difference: {sum / (tests * rounds)}")

def nextPrediction() -> None:
    data: pd.DataFrame = readData()
    opa: pd.DataFrame = data["opa"]
    oma: pd.DataFrame = data["oma"]

    prediction: int = getPrediction(opa, oma, True)

    print(f"Final prediction: {prediction}")

if __name__ == "__main__":
    # nextPrediction()
    runManyTests(100, 26)
from typing import List, Tuple
import pandas as pd

from distributions import DistributionType, getDistribution, sampleDistribution
from predictions import PredictionType, getPrediction


PredictionMethod: PredictionType = PredictionType.SAMPLE_MEAN
DistributionMethod: DistributionType = DistributionType.NORMAL

def readData() -> pd.DataFrame:
    return pd.read_csv("./data.csv")

def runTest(rounds: int, log: bool) -> float:
    distributionOpa: Tuple[float] = getDistribution(DistributionMethod)
    distributionOma: Tuple[float] = getDistribution(DistributionMethod)

    if log:
        print(f"Distribution opa: {distributionOpa}")
        print(f"Distribution oma: {distributionOma}")
        print()

    dataOpa: pd.DataFrame = pd.DataFrame()
    dataOma: pd.DataFrame = pd.DataFrame()

    score: float = 0
    for i in range(rounds):
        prediction: float = getPrediction(PredictionMethod, dataOpa, dataOma, False)

        opaRating: int = sampleDistribution(distributionOpa)
        omaRating: int = sampleDistribution(distributionOma)
        dataOpa[-1] = [opaRating]
        dataOma[-1] = [omaRating]
        rating: int = opaRating + omaRating

        score -= abs(prediction - rating)

        if log:
            print(f"{i}: \tPrediction={prediction} \tOpa={opaRating} \tOma={omaRating} \tTotal={rating} \tScore={score}")
    
    if log:
        print(f"Total score: {score} \tAverage difference: {score / rounds}")
    return score

def runManyTests(tests: int, rounds: int) -> None:
    results: List[float] = []

    sum: float = 0
    for i in range(tests):
        results.append(runTest(rounds, False))
        sum += results[i]
    
    print(results)
    print(f"Average score: {sum / tests} \tAverage difference: {sum / (tests * rounds)}")

def nextPrediction() -> None:
    data: pd.DataFrame = readData()
    opa: pd.DataFrame = pd.DataFrame(data["opa"])
    oma: pd.DataFrame = pd.DataFrame(data["oma"])

    prediction: float = getPrediction(PredictionMethod, opa, oma, True)

    print(f"Final prediction: {prediction}")

if __name__ == "__main__":
    nextPrediction()
    # runTest(17, True)
    # runManyTests(100, 17)

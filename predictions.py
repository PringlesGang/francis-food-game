from enum import Enum

import pandas as pd


class PredictionType(Enum):
    SAMPLE_MEAN = 1
    UNIFORM_MEAN = 2

def getSamplePrediction(data: pd.DataFrame) -> float:
    if (data.size == 0):
        return 8
    
    return data.mean().iloc[0]

def getUniformMean() -> float:
    return 10

def getSinglePrediction(predictionMethod: PredictionType, data: pd.DataFrame) -> float:
    match predictionMethod:
        case PredictionType.SAMPLE_MEAN:
            return getSamplePrediction(data)
        case _: # Uniform mean
            return getUniformMean()

def getPrediction(predictionMethod: PredictionType, opa: pd.DataFrame, oma: pd.DataFrame, log: bool) -> int:
    opaPrediction: float = getSinglePrediction(predictionMethod, opa)
    omaPrediction: float = getSinglePrediction(predictionMethod, oma)

    if log:
        print(f"Opa prediction: {opaPrediction}")
        print(f"Oma prediction: {omaPrediction}")

    aggregate: float = getSinglePrediction(predictionMethod, opa) + getSinglePrediction(predictionMethod, oma)
    return int(round(aggregate))

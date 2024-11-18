from enum import Enum

import pandas as pd


class PredictionType(Enum):
    SAMPLE_MEAN = 1
    UNIFORM_MEAN = 2
    SAMPLE_MEDIAN = 3
    SAMPLE_MODE = 4

def getSampleMean(data: pd.DataFrame) -> float:
    if (data.size == 0):
        return 8
    
    return pd.to_numeric(data.mean()).iloc[0]

def getSampleMedian(data: pd.DataFrame) -> float:
    if (data.size == 0):
        return 8
    
    return pd.to_numeric(data.median()).iloc[0]

def getSampleMode(data: pd.DataFrame) -> float:
    if (data.size == 0):
        return 8
    
    return pd.to_numeric(data.mean()).iloc[0]

def getUniformMean() -> float:
    return 10

def getSinglePrediction(predictionMethod: PredictionType, data: pd.DataFrame) -> float:
    match predictionMethod:
        case PredictionType.SAMPLE_MEAN:
            return getSampleMean(data)
        case PredictionType.SAMPLE_MEDIAN:
            return getSampleMedian(data)
        case PredictionType.SAMPLE_MODE:
            return getSampleMode(data)
        case _: # Uniform mean
            return getUniformMean()

def getPrediction(predictionMethod: PredictionType, opa: pd.DataFrame, oma: pd.DataFrame, log: bool) -> float:
    opaPrediction: float = getSinglePrediction(predictionMethod, opa)
    omaPrediction: float = getSinglePrediction(predictionMethod, oma)

    if log:
        print(f"Opa prediction: {opaPrediction}")
        print(f"Oma prediction: {omaPrediction}")

    aggregate: float = getSinglePrediction(predictionMethod, opa) + getSinglePrediction(predictionMethod, oma)
    return aggregate

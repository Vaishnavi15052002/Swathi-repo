def recommend(mode):
    if mode == "model_fail":
        raise ValueError("ModelCrashed")
    if mode == "no_data":
        raise LookupError("NoTrainingData")
    if mode == "slow":
        raise TimeoutError("RecommendTimeout")

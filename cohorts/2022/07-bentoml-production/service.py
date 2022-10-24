import numpy as np
from pydantic import BaseModel

import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray


class UserProfile(BaseModel):
    name:str 
    age: int 
    country: str 
    rating: float 

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("user_profile_classifier", runners=[model_runner])

@svc.api(input=NumpyNdarray(shape=(-1, 4), enforce_shape=True), output = NumpyNdarray())
async def classify(user_profile):
    prediction = await model_runner.predict.async_run(user_profile)
    print(prediction)
    result = prediction[0]
    return result


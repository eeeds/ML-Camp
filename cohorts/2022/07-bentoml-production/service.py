import numpy as np
from pydantic import BaseModel

import bentoml
from bentoml.io import JSON


class UserProfile(BaseModel):
    name:str 
    age: int 
    country: str 
    rating: float 


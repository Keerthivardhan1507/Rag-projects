import os
from backend.config_loader import load_config
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import Literal,List,Any,Dict

class ConfigLoader:
    def __init__(self):
        pass
    
    def __getitem__(self, key):
        pass
    
class ModelLoader(BaseModel):
    def __init__(self):
        pass
    
    def model_post_init():
        pass
    
    class Config:
        
        def load_llm(self):
            pass
            



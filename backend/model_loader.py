import os
from backend.config_loader import load_config
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Literal,List,Any,Dict,Optional

class ConfigLoader:
    def __init__(self):
        print("loadinf Config")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]
    
class ModelLoader(BaseModel):
    model_provider :Literal["groq"] = "groq"
    config :Optional[ConfigLoader] = Field(default=None,exclude=True)
    
    def model_post_init(self,__context:Any)->None:
        self.config = ConfigLoader()    
    class Config:
        arbitrary_types_allowed = True
        
    def load_llm(self):
        """Load the llm model
        """
        print(f"loading model")
        print(f"Loading llm model {self.model_provider}")
        
        if self.model_provider == "groq":
            print("loading groq model")
            groq_api_key = os.environ["GROQ_API_KEY"]
            model_name = self.config["llm"]["groq"]
            llm = ChatGroq(model=model_name,api_key=groq_api_key)
        return llm
            



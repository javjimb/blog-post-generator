from pydantic import BaseModel
from typing import List

class Query(BaseModel):
    query: str

class BlogPost(BaseModel):
    title: str
    content: str
    
class BlogPostGenerationRequest(BaseModel):
    topic: str
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.95

  
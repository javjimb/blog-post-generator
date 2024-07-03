from fastapi import APIRouter, HTTPException
from transformers import GPT2Tokenizer, GPT2Model
from typing import List
from app.schemas import Query, BlogPost
from models.pinecone.pinecone_setup import index
from app.utils.search import find_relevant_content

# Initialize the router
router = APIRouter()

# Load GPT-2 model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2Model.from_pretrained(model_name)

# Set padding token
tokenizer.pad_token = tokenizer.eos_token

@router.post("/search", response_model=List[BlogPost])
def search_blog_posts(query: Query):
    search_results, error = find_relevant_content(query.query)
    
    if error:
        raise HTTPException(status_code=500, detail=error)

    return search_results


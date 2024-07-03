from transformers import GPT2Tokenizer, GPT2Model
from typing import List, Tuple
from app.schemas import BlogPost
from models.pinecone.pinecone_setup import index

# Load GPT-2 model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2Model.from_pretrained(model_name)

# Set padding token
tokenizer.pad_token = tokenizer.eos_token

def find_relevant_content(query: str, top_k: int = 6) -> Tuple[List[BlogPost], str]:
    try:
        # Generate embeddings for the query
        inputs = tokenizer(query, return_tensors='pt', truncation=True, padding=True, max_length=512)
        outputs = model(**inputs)
   
        query_embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy().tolist()
        
        # Perform a similarity search in Pinecone
        search_results = index.query(vector=query_embedding, top_k=top_k, include_values=True, include_metadata=True)

        if not search_results['matches']:
            return [], "No matching blog posts found"
        
        # Retrieve the matching blog posts
        results = []
        for match in search_results['matches']:
            if 'metadata' in match:
                metadata = match['metadata']
                results.append(BlogPost(title=metadata['title'], content=metadata['content']))
            else:
                return [], "Metadata not found in Pinecone response"

        return results, ""
    except Exception as e:
        return [], str(e)
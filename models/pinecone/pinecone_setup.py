# models/pinecone/pinecone_setup.py
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables from .env file
load_dotenv()

# Access the API key
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Create a Pinecone instance
pinecone = Pinecone(api_key=pinecone_api_key)

# Create a new index if it does not exist
index_name = 'denia-dog-travel'
if index_name not in pinecone.list_indexes().names():
    pinecone.create_index(
        name=index_name,
        dimension=768,  # common size for GPT-2, BERT, etc.
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1',
        )
    )

# Connect to the index
index = pinecone.Index(index_name)

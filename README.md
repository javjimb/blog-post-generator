# Blog Post Generator

## Project Description

The Blog Post Generator is an AI-powered tool for generating SEO-friendly blog posts. It uses machine learning models to create engaging and search-optimized content based on provided topics or keywords.

## Project Goals

- **Innovative Content Creation:** Develop a system to generate SEO-friendly blog posts to boost website traffic.
- **Advanced Retrieval System:** Implement a retrieval system to fetch relevant content based on keywords using the Pinecone vector database.
- **Generative Model:** Use a GPT model to generate high-quality articles based on the retrieved content.
- **Documentation:** Maintain detailed documentation of the progress using Jupyter Notebooks.

## Tech Stack

- **Backend:** FastAPI for the server-side logic and API endpoints.
- **Vector Database:** Pinecone for storing and querying text embeddings.
- **NLP Models:** GPT for content generation.
- **Data Collection:** BeautifulSoup and Requests for web scraping.
- **Utilities:** Pandas for data handling, and Jupyter Notebooks for documenting progress.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Pinecone API Key
- OpenAI API Key

### Installation Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/blog-post-generator.git
   cd blog-post-generator
   ```
2. **Create a virtual environment and activated it:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the required dependencies:**
   ```sh
    pip install -r requirements.txt
    ```
4. **Set up environment variables:**
   Create a .env file in the root directory and add your API keys:
   ```sh
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```
5. **Run the FastAPI server:**
   ```sh
   uvicorn main:app --reload
   ```

## Project Work and Documentation

### Backend API Development

- **FastAPI Endpoints:**
  - `/generate_blog`: Generates a blog post based on a user-provided topic or keyword.
  - `/search`: Searches for relevant content based on a query.

- **Pinecone Integration:**
  - Used for storing and querying text embeddings to retrieve relevant content.

- **GPT Model Integration:**
  - Utilizes the OpenAI GPT-3.5 model to generate coherent and engaging blog posts.

### Data Collection

- **Web Scraping:**
  - Used BeautifulSoup and Requests to collect relevant content from various sources.
  - Stored and processed the data using Pandas.

### Embeddings and Search

- **Text Embeddings:**
  - Generated text embeddings using GPT-2.
  - Stored embeddings in Pinecone for efficient retrieval.

- **Search Functionality:**
  - Implemented search functionality to find and retrieve relevant content based on user queries.

### Jupyter Notebooks

- [Documented](notebooks/Automated_Blog_Post_Generator.ipynb) the progress of the project, including data collection, embedding generation, and search implementation.
- Provided detailed explanations and code examples to help understand the workflow and implementation details.

## Future Work

- **Frontend Development:**
  - A user-friendly web interface using Vue.js for inputting topics and viewing generated content (planned in a separate repository).

- **SEO Optimization:**
  - Integrate tools like SEMrush or Ahrefs APIs to analyze and optimize the generated content for SEO (planned in a separate repository).

## Author

- **Javier Jiménez Blasco** - [javjimb](https://github.com/javjimb)
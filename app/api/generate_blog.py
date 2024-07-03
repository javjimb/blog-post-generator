import os
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from openai import OpenAI
from app.schemas import BlogPost, BlogPostGenerationRequest
from app.utils.search import find_relevant_content
from app.utils.keywords import extract_keywords

load_dotenv()
client = OpenAI()

router = APIRouter()

@router.post("/generate_blog", response_model=BlogPost)
def generate_blog_post(request: BlogPostGenerationRequest):
    # Search for relevant content 
    retrieved_posts, error = find_relevant_content(request.topic)
    if error:
        raise HTTPException(status_code=500, detail=error)

    retrieved_content = " ".join([post.content for post in retrieved_posts])

    keywords = extract_keywords(retrieved_content)
    keyword_str = ", ".join(keywords)

    messages = [
      {"role": "system", "content": "You are a helpful assistant that generates SEO-friendly blog posts. The blog post should have a clear introduction, body, and conclusion. It should be engaging, informative, and written in a professional tone. Include headings and subheadings for better readability. Use bullet points, lists, and examples where appropriate."},
      {"role": "user", "content": retrieved_content},
      {"role": "system", "content": f"Focus on the following keywords: {keyword_str}. Ensure the content is optimized for search engines by using the keywords naturally within the text. Include meta descriptions and alt text for any images."},
      {"role": "system", "content": "Write in a friendly and conversational tone, but maintain professionalism. Use anecdotes or personal experiences if relevant to make the content more relatable."},
      {"role": "system", "content": "The blog post should also include a call-to-action at the end, encouraging readers to engage with the content, leave comments, or visit a related page."}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            n=1
        )

        generated_text = response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return BlogPost(title=request.topic, content=generated_text)
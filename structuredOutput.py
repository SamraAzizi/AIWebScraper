import asyncio
from typing import List
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig, Controller

# Path to Chrome
chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# Browser configuration
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=chrome_path
    )
)

# Define Instagram post structure (simplified)
class Post(BaseModel):
    post_title: str
    post_url: str

class Posts(BaseModel):
    posts: List[Post]

# Controller
controller = Controller(output_model=Posts)

# LLM setup
llm = ChatOllama(model="llama2", num_ctx=4096)



import asyncio
from typing import List
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig, Controller

# Step 1: Chrome path for your system (adjust if needed)
chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# Step 2: Configure the browser
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=chrome_path
    )
)

# Step 3: Define your Pydantic output format
class Post(BaseModel):
    post_title: str
    post_url: str
    num_comments: int
    hours_since_post: int



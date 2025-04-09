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


# Task - structured instruction
task = (
    "Go to Tech With Tim's Instagram page. "
    "Extract the 3 most recent posts. "
    "For each post, return the caption text as 'post_title' and the post URL as 'post_url'. "
    "Respond in JSON format matching this structure:\n"
    "{ 'posts': [ { 'post_title': str, 'post_url': str }, ... ] }"
)

# Main async logic
async def main():
    agent = Agent(task=task, llm=llm, browser=browser, controller=controller)
    
    history = await agent.run()
    result = history.final_result()
    
    if result:
        parsed: Posts = Posts.model_validate_json(result)

        for post in parsed.posts:
            print('\n--------------------------------')
            print(f'Title: {post.post_title}')
            print(f'URL:   {post.post_url}')
    else:
        print('No result')

    input("\n✅ Press Enter to close the browser...")
    await browser.close()

# Entry point
if __name__ == '__main__':
    asyncio.run(main())
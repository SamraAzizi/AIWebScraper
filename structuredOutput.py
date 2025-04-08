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

class Posts(BaseModel):
    posts: List[Post]

# Step 4: Controller to parse output into the defined schema
controller = Controller(output_model=Posts)

# Step 5: Ollama LLM setup (you can change model as needed)
llm = ChatOllama(model="llama2", num_ctx=4096)

# Step 6: Your custom task for the agent
task = "Search Google for the top 5 AI tools launched in 2024, open each tool's website, and summarize their main features. Return structured JSON with title, URL, estimated comment count, and estimated hours since launch."

# Step 7: Main function to run the task and parse output
async def main():
    agent = Agent(task=task, llm=llm, browser=browser, controller=controller)
    
    history = await agent.run()
    result = history.final_result()
    
    if result:
        parsed: Posts = Posts.model_validate_json(result)

        for post in parsed.posts:
            print('\n--------------------------------')
            print(f'Title:            {post.post_title}')
            print(f'URL:              {post.post_url}')
            print(f'Comments:         {post.num_comments}')
            print(f'Hours since post: {post.hours_since_post}')
    else:
        print('No result')

    input("\n✅ Press Enter to close the browser...")
    await browser.close()

# Step 8: Entry point
if __name__ == '__main__':
    asyncio.run(main())

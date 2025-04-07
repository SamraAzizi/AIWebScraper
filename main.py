import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig

# Change this path to match your system:

# For macOS:
# chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# For Windows:
chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# For Linux:
# chrome_path = '/usr/bin/google-chrome'

# Configure the browser instance
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=chrome_path
    )
)

# Initialize the Ollama model
llm = ChatOllama(model="llama2", num_ctx=4096)

# Task for the agent to perform
task = "Search Google for the top 5 AI tools launched in 2024, open each tool's website, and summarize their main features."

# Create the agent
agent = Agent(
    task=task,
    llm=llm,
    browser=browser
)

# Async runner
async def main():
    await agent.run()
    input("✅ Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

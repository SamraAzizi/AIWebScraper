import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

async def main():
    agent = Agent(
        task="Visit example.com/articles, click on the 'Load More' button until all articles are loaded, then extract the titles of all articles.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

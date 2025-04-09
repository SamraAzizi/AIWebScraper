import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

async def main():
    agent = Agent(
        task="Visit example.com, navigate to the 'Products' page, click on the first product, and extract its name and price.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

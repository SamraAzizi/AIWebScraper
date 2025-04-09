import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

async def main():
    agent = Agent(
        task="Go to example.com/contact, fill out the contact form with name 'John Doe', email 'john@example.com', and message 'Hello, this is a test.', then submit the form.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())

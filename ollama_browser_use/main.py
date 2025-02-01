"""Main."""
import asyncio

from browser_use import Agent, Browser, BrowserConfig
from langchain_ollama import ChatOllama


async def main():
    """Run agent."""
    # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
    browser = Browser(
        config=BrowserConfig(
            headless=False,
            # Windows chrome path
            chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            # WSL chrome path
            # chrome_instance_path="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe",
        )
    )

    # Initialize the model
    llm = ChatOllama(model="qwen2.5:latest", num_ctx=8000)

    print("Welcome to Ollama Browser Use!")
    print("Ensure that you have closed all Chrome windows before starting a task.")
    task = input("Enter a task: ")
    print("\n")

    # Create agent with the model
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        use_vision=True,
    )

    # Run the agent and print the result
    result = await agent.run()
    print(result)
    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())

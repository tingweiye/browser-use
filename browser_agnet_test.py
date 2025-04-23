import sys
import os

# sys.path.append(os.path.abspath("./browser-use"))
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

config = BrowserConfig(
    headless=False,
    disable_security=False
)

browser = Browser(config=config)


from browser_use import Controller, ActionResult
# Initialize the controller
# controller = Controller()

# @controller.action('Ask user for information')
# def ask_human(question: str) -> str:
#     answer = input(f'\n{question}\nInput: ')
#     return ActionResult(extracted_content=answer)

# browser = Browser(
#     config=BrowserConfig(
#         # Specify the path to your Chrome executable
#         # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
#         browser_binary_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
#         # For Linux, typically: '/usr/bin/google-chrome'
#     )
# )

# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
#     handlers=[
#         logging.FileHandler("logs/browser_use.log"),
#         logging.StreamHandler()
#     ]
# )



llm=ChatOpenAI(
    # model="deepseek/deepseek-r1-zero:free",
    model="deepseek-chat",
    # model="deepseek-reasoner",
    
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_ENDPOINT"),
)
# print(os.getenv("OPENAI_API_KEY"))
# print(os.getenv("OPENAI_ENDPOINT"))
'''
agent = Agent(
        task="去淘宝买一个小收纳箱",
        llm=llm,
)
agent.run()
'''

async def main():
    agent = Agent(
        task="去淘宝买一个小收纳箱",
        llm=llm,
        # browser=browser,
    )
    await agent.run()
    await browser.close()

asyncio.run(main())
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
config=BrowserConfig(
    # Specify the path to your Chrome executable
    # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
    browser_binary_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    # disable_security=False
    # For Linux, typically: '/usr/bin/google-chrome'
)

browser = Browser(
    config=config
)

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


async def main():
    agent = Agent(
        # task="在当前的淘宝页面搜索框输入‘星巴克馥芮白’并点击搜索按钮，不要搜索其他url",
        # task="你在选品购买界面，选择美式，数量尽可能少的规格并点击购买，不要加入购物车",
        task="下单一份KFC香辣鸡腿堡两件套并支付，记得先选取商品规格(香辣鸡腿堡两件套+中可)（没有该类似套餐则直接结束流程）再点击下单",
        # task="在淘宝下单一份KFC香辣鸡腿堡两件套并支付，要求价格尽可能低。在具体商品下单界面时，记得先选取商品规格(香辣鸡腿堡两件套+中可)（如果有的话）再点击下单",
        # task="点击第二个“查看更多”按键，之后点击跳出的第三个商品",
        # task="在淘宝下单一份霸王茶姬伯牙绝弦并支付，要求价格尽可能低。在具体商品下单界面时，记得先选取商品规格（如果有的话）再点击下单。到支付宝界面你就可以结束",
        # task="在淘宝下单一份麦辣鸡腿堡四件套并支付，要求价格尽可能低。在具体商品下单界面时，记得先选取商品规格(麦辣鸡腿堡的四件套)（如果有的话）再点击下单。到支付宝界面你就可以结束",
        # task="在淘宝下单一份麦辣鸡腿堡四件套并支付，要求选择搜索后的第一个商品/店铺。在具体商品下单界面时，记得先选取商品规格(麦辣鸡腿堡的四件套)（如果有的话）再点击下单。到支付宝界面你就可以结束",
        llm=llm,
        browser=browser,
        generate_gif=True
    )
    await agent.run()
    await browser.close()

asyncio.run(main())
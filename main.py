import sys
import os

# sys.path.append(os.path.abspath("./browser-use"))
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig
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
    new_context_config=BrowserContextConfig(
        cookies_file="D:\\workplace\\browser_use_test\\browser-use\\cookies\\www.taobao.com_cookies.json"
    )
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
# task="在当前的淘宝页面搜索框输入‘星巴克馥芮白’并点击搜索按钮，不要搜索其他url",
# task="你在选品购买界面，选择美式，数量尽可能少的规格并点击购买，不要加入购物车",
# task="在旺旺客服，选择第一个聊天记录，提取其中卡券兑换的里链接并导航到该链接，选择城市'杭州'，门店'杭州滨江保利天汇餐厅'，如果需要选择商品规格则选择'香辣鸡腿堡两件套+中可'，最后找到兑换按钮但不要点击，结束流程",
# task="在页面购买一份香辣鸡腿堡两件套，先选取商品规格(香辣鸡腿堡+中可)，如果有多个选项则需要多次选择，如果没有该类似套餐则直接结束流程，完成规格选择后再点击下单并支付",
# task="不要擅自导航到任何页面，除了卡密页面，在第一个页面点击旺旺聊天/旺旺在线，查看最新（第一个店铺）的最新聊天内容，提取其中的卡密（http或者https链接）并打开页面，在页面中兑换卡券，选择城市'杭州'，门店'杭州滨江保利天汇餐厅'，如果需要选择商品规格则选择'香辣鸡腿堡两件套+中可'，最后找到兑换按钮但不要点击，结束流程",
# task = "兑换卡券，选择城市'杭州'，门店'杭州滨江保利天汇餐厅'，如果需要选择商品规格则选择'香辣鸡腿堡两件套+中可'，最后找到兑换按钮但不要点击，结束流程"
task = \
"""
你需要做到：
1. 在淘宝商品的购买界面，根据列表【大杯，馥芮白/金烘馥芮白】选择合适的sku。
你的选择需要结合列表中的信息和页面中存在的信息，判断页面元素语义是否相似，而不是直接判断列表整体是否存在。如果页面中有多个选项则需要多次选择，如果没有多个选择则选择最合适的sku，如果没有该类似套餐则直接结束流程。
2. 完成规格选择后再点击下单并支付。如果新页面中显示“对不起，系统繁忙”类似的文字内容，则直接终止流程，输出“触发反爬机制，流程终止”。
3. 在支付完成界面进入旺旺在线/旺旺聊天，输出最新店家聊天的最新聊天内容，提取其中的卡密（http或者https链接）并输出。
"""
# task = \
# """
# 你需要做到：
# 1. 在淘宝商品的购买界面，根据列表【5块黄金鸡块】选择合适的sku。
# 你的选择需要结合列表中的信息和页面中存在的信息，判断页面元素语义是否相似，而不是直接判断列表整体是否存在。如果页面中有多个选项则需要多次选择，如果没有多个选择则选择最合适的sku，如果没有该类似套餐则直接结束流程。
# 2. 完成规格选择后再点击下单并支付。如果新页面中显示“对不起，系统繁忙”类似的文字内容，则直接终止流程，输出“触发反爬机制，流程终止”。
# 3. 在支付完成界面进入旺旺在线/旺旺聊天，输出最新店家聊天的最新聊天内容，提取其中的卡密（http或者https链接）并输出。
# """
# task = \
# """
# 点击购买下单或相同意思的按钮（不要点击加入购物车）
# """
# task = \
# """
# 你需要做到：
# 1. 在初始界面输入x_name用户名和x_password密码登入账号，选择保持登录（有的话）。
# 2. 跳转到'https://item.taobao.com/item.htm?abbucket=3&detail_redpacket_pop=true&id=842380312954'的购买界面。
# 2. 在淘宝商品的购买界面，根据列表【大杯，馥芮白/金烘馥芮白】选择合适的sku。
# 你的选择需要结合列表中的信息和页面中存在的信息，判断页面元素语义是否相似，而不是直接判断列表整体是否存在。如果页面中有多个选项则需要多次选择，如果没有多个选择则选择最合适的sku，如果没有该类似套餐则直接结束流程。
# 3. 完成规格选择后再点击下单并支付。如果新页面中显示“对不起，系统繁忙”类似的文字内容，则直接终止流程，输出“触发反爬机制，流程终止”。
# 4. 在支付完成界面进入旺旺在线/旺旺聊天，输出最新店家聊天的最新聊天内容，提取其中的卡密（http或者https链接）并输出。
# """

sensitive_data = {'x_name': '18258381393', 'x_password': 'hnytw8300'}

initial_actions = [
	# {'go_to_url': {'url': 'https://item.taobao.com/item.htm?abbucket=3&detail_redpacket_pop=true&id=876759558073&ltk2=17471205334116hcpzddo91lvcrzd6xxeed&ns=1&priceTId=undefined&query=%E6%98%9F%E5%B7%B4%E5%85%8B%E6%98%9F%E5%86%B0%E4%B9%90&skuId=5945671974730&spm=a21n57.1.hoverItem.5&utparam=%7B%22aplus_abtest%22%3A%2296098c529f490d99e537408099877ca4%22%7D&xxc=taobaoSearch'}},
	{'go_to_url': {'url': 'https://item.taobao.com/item.htm?abbucket=3&detail_redpacket_pop=true&id=842380312954&ltk2=174712137353826fvschzfsruhwvd173ic&ns=1&priceTId=undefined&query=%E6%98%9F%E5%B7%B4%E5%85%8B%E6%98%9F%E5%86%B0%E4%B9%90&skuId=5795655434860&spm=a21n57.1.hoverItem.7&utparam=%7B%22aplus_abtest%22%3A%229d9831db5dcae2980a1be0cbc91b8df4%22%7D&xxc=taobaoSearch'}},
	# {'go_to_url': {'url': 'https://detail.tmall.com/item.htm?abbucket=3&detail_redpacket_pop=true&id=823896547258&ltk2=1747138330040ulg3u51ocermrt26rpty3&ns=1&priceTId=213e045f17471383276446343e1f75&query=%E9%9C%B8%E7%8E%8B%E8%8C%B6%E5%A7%AC&skuId=5710032495209&spm=a21n57.1.hoverItem.5&utparam=%7B%22aplus_abtest%22%3A%22e04ed188ec996c73b858f220aebf37e3%22%7D&xxc=taobaoSearch'}},
	# {'go_to_url': {'url': 'https://item.taobao.com/item.htm?abbucket=3&detail_redpacket_pop=true&id=855771605095'}},
	{'scroll_down': {'amount': 100}},
]

async def main():
    agent = Agent(
        task=task,
        initial_actions=initial_actions,
        llm=llm,
        browser=browser,
        sensitive_data=sensitive_data,
        generate_gif=True
    )
    await agent.run()
    await browser.close()

asyncio.run(main())
import random
import requests
import httpx
import asyncio
import os
import openai
import re
from bs4 import BeautifulSoup
from datetime import date
from xml.etree import ElementTree
import nonebot
from nonebot import on_command, on_regex, logger
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from nonebot.params import RegexGroup
from nonebot.plugin import PluginMetadata
from .utils.decorator import auto_withdraw
from .utils.config import get_message_id
__plugin_meta__ = PluginMetadata(
    name="随机图片",
    description="从各随机图片接口获取一张图片",
    usage=(
        "来点猫片\n"
        "来点二次元图\n"
    ),
    extra={
        'type':    '娱乐',
        'range':   ['private', 'group', 'guild'],
        "author":  "惜月 <277073121@qq.com>",
        "version": "1.0.0",
    },
)

ecy_img = on_regex(r'^来点(二次元|二刺螈|银发|兽耳|星空|竖屏|横屏|富婆|萝莉|涩图|涩涩|色色|来点|福瑞)图?$', priority=13, block=True)
ecy_img.__paimon_help__ = {
    "usage":     "来点<类型>图",
    "introduce": "懂得都懂，类型有原神|二次元|二刺螈|银发|兽耳|星空|竖屏|横屏",
    "priority": 13
}
ys_img = on_command('原神壁纸', aliases={'来点原神图', '来点原神壁纸'}, priority=13, block=True)
bing_img = on_command('来点必应壁纸', aliases={'来点必应图', '来点必应壁纸', '来点必应'}, priority=13, block=True)
beautiful_img = on_command('来点随机图', aliases={'来点随机图'}, priority=13, block=True)
tuwei_word = on_command('来点情话', aliases={'来点情话','说点情话'}, priority=13, block=True)
coser_img = on_command('来点coser', aliases={'来点coser', '来点cos'}, priority=13, block=True)
paimon_knowledge = on_command('派蒙帮忙问问', aliases={'派蒙帮忙问问'}, priority=13, block=True)

# 读取.env.{ENVIRONMENT} 文件中的配置
config = nonebot.get_driver().config

#二次元图片
@ecy_img.handle()
@auto_withdraw(15)
async def ecy_img_handler(bot: Bot, event: MessageEvent, regexGroup=RegexGroup()):
    urls = [
        'https://www.dmoe.cc/random.php',
        #'https://api.iw233.cn/api.php?sort=random',
    ]
    img_type = regexGroup[0]
    if img_type in ['二次元', '二刺螈']:
        url = random.choice(urls)
        #print(url)
    elif img_type in ['富婆', '萝莉', '涩图', '涩涩', '色色', '福瑞']:
        backWords = [
            "呜呜呜，派蒙已经很努力了，但是没有找到你要的图片，可能是要找的网站不给派蒙图片，果面呐噻~下次一定一定会更努力的 (´；ω；`)",
            "歪，警察蜀黍嘛，派蒙这里有个变态要找富婆萝莉涩图！",
            "喂喂喂，派蒙可不知道你在说什么，派蒙可是个纯洁的向导哦！(｡>﹏<｡)",
            "啊嘞？你在找什么？派蒙可没听说过这种东西哦~（。・＿・。）ﾉ",
            "哼！派蒙不会帮你找这些奇怪的东西的！找其他的图吧~ ╭(๑¯д¯๑)╮",
            "派蒙怎么会知道这些东西呢！不过派蒙还是会努力的，只是这次可能没有办法帮到你啦 (｡•́︿•̀｡)",
            "想知道的更多嘛？嗯哼哼~快发送help获取吧~"
        ]
        await ecy_img.finish(random.choice(backWords))
    elif img_type in ['来点']:
        await ecy_img.finish(f'果面呐噻，派蒙没有找到你要的"{img_type}"图呢~，有没有可能是打错了字？发送help查看一下派蒙的用法吧！')
    elif img_type in ['银发','兽耳','星空','竖屏','横屏']:
        await ecy_img.finish(f'果面呐噻，派蒙没有找到你要的"{img_type}"图呢~，你知道哪里有嘛？偷偷的告诉派蒙吧！')
    else:
        url = ''
    await ecy_img.send(MessageSegment.image(file=url))

#原神
@ys_img.handle()
@auto_withdraw(30)
async def ys_img_handler(event: MessageEvent):
    urls = [
        'https://api.dreamofice.cn/random-v0/img.php?game=ys',
        'https://api.r10086.com/img-api.php?zsy=原神',
        'https://api.r10086.com/img-api.php?type=原神横屏系列1',
        'https://api.r10086.com/img-api.php?type=原神竖屏系列1',
    ]
    await ys_img.finish(MessageSegment.image(file=random.choice(urls)))
#coser图片
# 定义一个锁，如果上次请求还未完成，就不再进行下一次请求
request_lock = asyncio.Lock()
@coser_img.handle()
@auto_withdraw(30)
async def coser_img_handler(event: MessageEvent):
    if request_lock.locked():
        await coser_img.finish("派蒙还在处理 (｡•́︿•̀｡)，不要心急哦~")
        return

    async with request_lock:
        urls = [
            'http://3650000.xyz/api/?type=img&mode=8',
        ]
        
        selected_url_index = random.randint(0, len(urls) - 1)
        selected_url = urls[selected_url_index]
        
        if selected_url_index == 0:
            async with httpx.AsyncClient() as client:
                response = await client.get(selected_url)
                
            if response.status_code == 200:
                # 解析响应的 HTML
                soup = BeautifulSoup(response.text, 'lxml')
                
                # 提取图片 URL
                img_tag = soup.find('img')
                image_url = img_tag['src']
            else:
                await coser_img.finish("呜呜呜，派蒙已经很努力了，但是没有找到你要的图片，可能是要找的网站不给派蒙图片，果面呐噻~下次一定一定会更努力的 (´；ω；`)")
        else:
            image_url = selected_url
        
        # 发送图片给用户
        await coser_img.finish(MessageSegment.image(file=image_url))
#随机图
@beautiful_img.handle()
@auto_withdraw(30)
async def beautiful_img_handler(event: MessageEvent):
    urls = [
        'https://api.vvhan.com/api/acgimg',
        'https://api.vvhan.com/api/mobil.girl',
        'https://api.vvhan.com/api/girl',
        'https://api.uomg.com/api/image.lofter?format=images'
    ]
    await beautiful_img.finish(MessageSegment.image(file=random.choice(urls)))
#情话
# 用于存储用户请求的字典
user_requests = {}
# 读取配置文件中的土味情话每日限制次数, 没有就默认为 10 次
tuwei_word_daily_limit = int(getattr(config, "tuwei_word_daily_limit", 10))
@tuwei_word.handle()
@auto_withdraw(30)
async def tuwei_word_handler(event: MessageEvent):
    global user_requests
    user_id = event.user_id
    today = date.today()
    # 检查用户是否已经请求过，如果没有或者请求不是今天的，则初始化计数
    if user_id not in user_requests or user_requests[user_id]['date'] != today:
        user_requests[user_id] = {'date': today, 'count': 0}
    # 如果用户今天的请求次数已经达到限制，不再处理请求
    if user_requests[user_id]['count'] >= tuwei_word_daily_limit:
        print(f"用户 {user_id} 今日已经收到了 {tuwei_word_daily_limit} 次情话.")
        return
    # 定义情话API的URL列表
    urls = [
        'https://api.uomg.com/api/rand.qinghua?format=text',
        #'https://api.vvhan.com/api/love'
    ]
    # 从URL列表中随机选择一个URL
    chosen_url = random.choice(urls)
    # 如果请求成功，发送情话给用户，并增加今日请求次数
    async with httpx.AsyncClient() as client:
        response = await client.get(chosen_url)
        
    if response.status_code == 200:
        user_requests[user_id]['count'] += 1
        # 添加换行符
        text = response.text + "\n\n"
        text += f"--你今天已经收到了派蒙 {user_requests[user_id]['count']} / {tuwei_word_daily_limit}次情话咯~"  # 显示今天已请求的次数
        await tuwei_word.finish(text)
    else:
        await tuwei_word.finish("呜呜，派蒙还没想到，不过，派蒙会一直陪着你的~")
# 必应每日壁纸
@bing_img.handle()
@auto_withdraw(30)
async def bing_img_handler(bot: Bot, event: MessageEvent):
    url = 'https://rss.paimons.cn/bing'

    response = requests.get(url)
    xml_content = response.content

    # 解析 XML
    root = ElementTree.fromstring(xml_content)

    # 查找所有的 <item> 标签
    items = root.findall('.//item')

    # 获取一个随机的 <item> 标签
    item = random.choice(items)
    title = item.find('title').text
    description = item.find('description').text

    # 使用 BeautifulSoup 来解析描述中的 HTML
    soup = BeautifulSoup(description, 'lxml')
    img = soup.find('img')

    if img is not None:
        img_src = img.get('src')
        img_alt = title

        # 发送图片
        await bing_img.finish(MessageSegment.text(img_alt) + MessageSegment.image(file=img_src))
    else:
        await bing_img.finish("呜呜呜，派蒙已经很努力了，但是没有找到你要的图片，可能是要找的网站不给派蒙图片，果面呐噻~下次一定一定会更努力的 (´；ω；`)")

#chatgpt
# 读取配置文件中的openai_api_key
openai.api_key = str(getattr(config, "openai_api_key", ""))
# 从配置文件中获取被禁止的用户ID
ban_use_userid_str = str(getattr(config, "ban_use_userid", "")).strip()

# 根据逗号分隔字符串，并去除每个元素的前后空格
ban_use_userid = [user_id.strip() for user_id in ban_use_userid_str.split(",")] if ban_use_userid_str else []

# 定义一个异步函数用于获取gpt-3.5-turbo模型回答问题的答案
async def fetch_answer(question: str) -> str:
    # 读取配置文件中的openai_api_proxy代理
    proxy = str(getattr(config, "openai_api_proxy", ""))
    # 设置局部代理来使用openai的API的访问
    if proxy:
        openai.proxy = {
            'http': proxy,
            'https': proxy
        }
    # 使用异步方式调用openai的API，在请求 API 的时候，Bot 不会被阻塞
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # role：角色，content：用户输入的内容
            {"role": "user", "content": f"{question}"}
        ],
        # 精度，介于0和2之间。较高的值（如0.8）会使输出更随机，而较低的值（如0.2）则会使其输出更加集中和精准
        temperature=0.3,
        # 生成的回复的最大令牌数
        max_tokens=2048,
        n=1
    ))
    answer = response.choices[0].message["content"].strip()
    usage_info = response.usage
    return answer, usage_info

@paimon_knowledge.handle()
async def paimon_knowledge_handler(bot: Bot, event: MessageEvent):
    # 获取用户输入的内容
    message_text = str(event.message).strip()
    question_pattern = re.compile(r"派蒙帮忙问问\s*\?*？*(.*)")
    match = question_pattern.match(message_text)
    # 获取用户id
    user_id = event.user_id
    # 检查用户是否在禁止列表中
    if str(user_id) in ban_use_userid:
        await paimon_knowledge.finish("你被禁止使用派蒙帮忙问问功能。")

    if match:
        question = match.group(1).strip()
        if not question:
            await paimon_knowledge.finish("你想让派蒙帮忙问问ChatGPT什么呢？")
        else:
            # 创建一个非阻塞任务，以便在等待 API 响应时继续执行其他任务
            fetch_answer_task = asyncio.create_task(fetch_answer(question))
            answer, usage_info = await fetch_answer_task
            # 记录usage信息
            logger.info(f"使用信息:\nPrompt tokens: {usage_info['prompt_tokens']}\nCompletion tokens: {usage_info['completion_tokens']}\nTotal tokens: {usage_info['total_tokens']}")

            await paimon_knowledge.finish(answer)
    else:
        await paimon_knowledge.finish("派蒙不知道哦！")
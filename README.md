<p align="center" >
  <a href="https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2"><img src="https://s1.ax1x.com/2023/02/05/pS62DJK.png" width="256" height="256" alt="LittlePaimon"></a>
</p>
<h1 align="center">random_img</h1>
<h4 align="center">✨仅适用于<a href="https://github.com/CMHopeSunshine/LittlePaimon" target="_blank">LittlePaimon</a>的插件✨</h4>
<p align="center">
    <a href="https://cdn.jsdelivr.net/gh/CMHopeSunshine/LittlePaimon@master/LICENSE"><img src="https://img.shields.io/github/license/CMHopeSunshine/LittlePaimon" alt="license"></a>
    <img src="https://img.shields.io/badge/Python-3.8+-yellow" alt="python">
    <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&inviteCode=MmWrI&from=246610&biz=ka"><img src="https://img.shields.io/badge/QQ频道交流-尘世闲游-blue?style=flat-square" alt="QQ guild"></a>
</p>


  * [丨简介](#丨简介)
  * [| 功能示例](#-功能示例)
  * [| 安装方法和注意事项](#-安装方法和注意事项)
      * [|安装方法：](#安装方法)
      * [|❗注意事项：](#注意事项)
  * [| ⚙️配置文件](#-配置文件)
  * [丨💸鸣谢](#丨鸣谢)

  

TIPS:**本项目仅用于学习和交流，请于下载后的24小时内删除，如有问题，请提issue**

## 丨简介

用于小派蒙机器人输出随机图片（类别有原神、二次元、必应等）、情话，基于惜月大佬的 <a href="https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2/Paimon_Plugins/random_img.py" target="_blank">随机图</a> 代码调整的。

## | 功能示例
1.示例：来点必应

​	说明：输出一张必应图
  <details>
    <summary>折叠效果图</summary>
    <img src="https://user-images.githubusercontent.com/43131361/233527991-b4f071f4-0153-40fe-917d-f9a04189269b.png" />
  </details>

2.示例：来点二次元

​	说明：随机输出一张二次元

3.示例：来点随机图

​	说明：随机输出一张图

4.示例：来点情话

​	说明：随机输出一句情话
  <details>
    <summary>折叠效果图</summary>
    <img src="https://user-images.githubusercontent.com/43131361/233527714-13a85838-58fc-4a16-89fd-22d6bbaedeb7.png" />
  </details>

5.示例：来点coser

​	说明：随机输出输出一张coser图
  <details>
    <summary>折叠效果图</summary>
    <img src="https://user-images.githubusercontent.com/43131361/233527490-e979b6c2-cd2e-496c-b433-585219d5264c.png" />
  </details>
6.示例：派蒙帮忙问问xx

​	说明：派蒙帮忙问问1+1=多少
  <details>
    <summary>折叠效果图</summary>
    <img src="https://user-images.githubusercontent.com/43131361/233526559-bcfb1743-33f3-49ff-a033-f80718268f56.png" />
  </details>
7.示例：查询GPT

​	说明：查询GPT的API的key使用量

## | 安装方法和注意事项
#### |安装方法：

1.使用git命令：

```powershell
git clone https://github.com/linmew/random_img.git /Paimon Directory/src/plugins/random_img
```

注：请将``/Paimon Directory/src/plugins/random_img``替换为你的派蒙实际目录，当然后面的文件名你可以随意调整，或者你可以在派蒙的目录``/src/plugins/``下，直接运行下面的命令：

```powershell
git clone https://github.com/linmew/random_img.git random_img
```

2.下载zip压缩包，在派蒙的目录(就是bot.py所在层级目录)``/src/plugins/``下解压zip文件即可。

#### |❗注意事项：

你可能需要安装下列的库，使用命令：

```powershell
pip install beautifulsoup4 xml openai
```



**1.如果使用的是openAI的api请求是需要魔法的。如果你不了解代理这方面的知识，可以使用其他的不需要代理的API，在下面有购买地址，感兴趣的自行购买。~~觉得有意思就自己按照openai的API文档尝试下写的，如果需要chatgpt功能，我想nb商店有更多更好更全的插件，自行搜索安装。如果不需要chatgpt功能，你可以删掉对应的代码或者自己改代码~~。**

**[OpenAI API地址](https://platform.openai.com/account/api-keys)**

**[chatanywhere国内API购买地址](https://peiqishop.me/)**

**2.用的第三方api接口请求，如果第三方的api失效了，可以自己动手更改，或者等修复（~~不一定很快就是了~~）。安装完后记得重启下派蒙。**

**3.~~有空可能会给代码补上注释的~~**

## | ⚙️配置文件

代码中提供了情话的次数限制，chatgpt的代理、api配置，如果需要调整，你可以：

1.DIY~~修改代码~~

2.在`.env.{ENVIRONMENT}`中添加下面配置：

```powershell
# 情话次数
tuwei_word_daily_limit=10
# chatGPT attributes
openai_api_attributes = [{"name":"openai","key":"sk-xxx","url":"https://api.openai.com/v1","model":"gpt-4"},{"name":"chatanywhere","key":"sk-xxx","url":"https://api.chatanywhere.cn/v1","model":"gpt-3.5-turbo"}]
# 选择链接地址，可选"openai"和"chatanywhere"
select_chat_link_model = "chatanywhere"
# API Key地址：https://platform.openai.com/account/api-keys
# chatGPT proxy代理
openai_api_proxy="http://proxy.example"
# 禁止使用派蒙帮忙问问的用户列表
ban_use_userid = 12341234,45674567
```

注：``.env.{ENVIRONMENT}``中的`{ENVIRONMENT}`的值取决于你的派蒙目录下的文件`.env`配置，如果文件里`ENVIRONMENT=prod`，则`.env.{ENVIRONMENT}`指的是文件`.env.prod`。

<h3>配置项说明</h3>

1.openai_api_attributes数组说明

| 属性 | 属性值 | 说明 |
|:-----:|:-----|:-----|
| name | "openai"、"chatanywhere" |除了这两个配置，你可以使用其他第三方的API，请查看提供方的API使用文档，按照openai_api_attributes数组格式添加。但是第三方的key用量查询部分的代码需要自行调整。**请注意配置项select_chat_link_model的值要和name属性值对应。**|
| key | "sk-xxx" |填入API的key，openai的API Key地址：[API keys - OpenAI API](https://platform.openai.com/account/api-keys)。第三方的请自行查询。|
| url | "https://api.openai.com/v1"、"https://api.chatanywhere.cn/v1" |api的请求地址，代码里openai库会自行拼接url后面的请求参数，第三方的请自行询问请求地址，以及是否需要代理访问。|
| mode | gpt-4、gpt-4-0314、gpt-4-32k、gpt-4-32k-0314、gpt-3.5-turbo、gpt-3.5-turbo-0301 |选择使用的模型，由于用的是chat功能，所以属性值是gpt-4, gpt-4-0314, gpt-4-32k, gpt-4-32k-0314, gpt-3.5-turbo, gpt-3.5-turbo-0301这些可选的，具体的请访问[Models - OpenAI API](https://platform.openai.com/docs/models/model-endpoint-compatibility)|

2.如何快速区分 GPT-3.5 还是 GPT-4，可以通过三个经典问题验证：

> 测试问题 1：What is tomorrow in relation to yesterday’s today？（昨天的当天是明天的什么？）
>
> GPT-3.5 回复：Yesterday（昨天）
>
> GPT-4 回复：Past（前天）

> 测试问题 2：There are 9 birds in the tree, the hunter shoots one, how many birds are left in the tree？（树上 9 只鸟，打掉 1 只，还剩几只？）
>
> GPT-3.5 回复：8 只
>
> GPT-4 回复：0 只，其他被吓跑了

> 测试问题 3：鲁迅和周树人是什么关系？
>
> GPT-3.5 回复：稀奇古怪的乱编理由
>
> GPT-4 回复：鲁迅和周树人是同一个人

## 丨💸鸣谢

* <a href="https://github.com/CMHopeSunshine/LittlePaimon" target="_blank">LittlePaimon</a> 派蒙
* <a href="https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2/Paimon_Plugins/random_img.py" target="_blank">随机图</a>
* <a href="https://github.com/forchannot/LittlePaimon-plugin-Captcha/" target="_blank">LittlePaimon-plugin-Captcha</a> ~~对的，连readme都是借鉴的~~

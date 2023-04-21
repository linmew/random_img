<p align="center" >
  <a href="https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2"><img src="https://s1.ax1x.com/2023/02/05/pS62DJK.png" width="256" height="256" alt="LittlePaimon"></a>
</p>
<h1 align="center">LittlePaimon-plugin-Captch</h1>
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

2.示例：来点二次元

​	说明：随机输出一张二次元

3.示例：来点随机图

​	说明：随机输出一张图

4.示例：来点情话

​	说明：随机输出一句情话

5.示例：来点coser

​	说明：随机输出输出一张coser图

6.示例：派蒙帮忙问问xx

​	说明：派蒙帮忙问问1+1=多少


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



**1.如果使用了chatgpt的函数，请一定要装openai库，当然，api请求是需要魔法的。不要问，不懂删对应代码即可。~~觉得有意思就自己按照openai的API文档尝试下写的，如果需要chatgpt功能，我想nb商店有更多更好更全的插件，自行搜索安装哦，当然你也可以自己试试，挺有意思的~~。**

**[OpenAI API地址](https://platform.openai.com/account/api-keys)**

**2.用的第三方api接口请求，如果第三方的api失效了，可以自己动手更改，或者等修复（~~不一定很快就是了~~）。安装完后记得重启下派蒙。**

**3.~~有空可能会给代码补上注释的~~**

## | ⚙️配置文件

代码中提供了情话的次数限制，chatgpt的代理、api配置，如果需要调整，你可以：

1.DIY

2.在`.env.{ENVIRONMENT}`中添加下面配置：

```powershell
# 情话次数
tuwei_word_daily_limit=10
# 填入自己的openai API Key
openai_api_key=sk-xxx
# API Key：https://platform.openai.com/account/api-keys
# chatGPT proxy代理
openai_api_proxy="http://proxy.example"
```

注：``.env.{ENVIRONMENT}``中的`{ENVIRONMENT}`的值取决于你的派蒙目录下的文件`.env`配置，如果文件里`ENVIRONMENT=prod`，则`.env.{ENVIRONMENT}`指的是文件`.env.prod`。



## 丨💸鸣谢

* <a href="https://github.com/CMHopeSunshine/LittlePaimon" target="_blank">LittlePaimon</a> 派蒙
* <a href="https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2/Paimon_Plugins/random_img.py" target="_blank">随机图</a>
* <a href="https://github.com/forchannot/LittlePaimon-plugin-Captcha/" target="_blank">LittlePaimon-plugin-Captcha</a> ~~对的，连readme都是借鉴的~~

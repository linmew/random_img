import nonebot
import json

# 读取.env.{ENVIRONMENT} 文件中的配置
openai_configs = nonebot.get_driver().config

class OpenAIConfig:
    def __init__(self):
        max_tokens_raw = getattr(openai_configs, "openai_max_tokens", None)
        try:
            self.max_tokens = int(max_tokens_raw)
        except (ValueError, TypeError):
            self.max_tokens = float('inf')

        self.proxy = str(getattr(openai_configs, "openai_api_proxy", ""))
        ban_use_userid_str = str(getattr(openai_configs, "ban_use_userid", "")).strip()
        self.ban_use_userid = [user_id.strip() for user_id in ban_use_userid_str.split(",")] if ban_use_userid_str else []

        # 获取选择的模型名称
        self.select_chat_link_model = getattr(openai_configs, "select_chat_link_model", "openai")

        try:
            # 获取配置的API属性列表
            self.openai_api_attribute = getattr(openai_configs, "openai_api_attributes", [])
            # 根据模型名称选择配置
            selected_config = {}
            if all(isinstance(config, dict) for config in self.openai_api_attribute):
                for config in self.openai_api_attribute:
                    if config["name"] == self.select_chat_link_model:
                        selected_config = config
                        break

            self.api_key = selected_config["key"]
            self.api_url = selected_config["url"]
            self.model = selected_config["model"]
        except KeyError as e:
            print(f"配置错误：缺少 {e}。请检查配置文件。")
            self.api_url = "https://api.openai.com/v1"
            self.model = "gpt-3.5-turbo"
        self.timeOut = 30 if self.select_chat_link_model != "openai" else None

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.api_key}"
        }
        self.proxies = {}
        if self.proxy and self.select_chat_link_model == "openai":
            self.proxies = {
                'http': self.proxy,
                'https': self.proxy
            }
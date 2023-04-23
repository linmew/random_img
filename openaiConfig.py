import nonebot
import re
# 读取.env.{ENVIRONMENT} 文件中的配置
config = nonebot.get_driver().config
class OpenAIConfig:
    def __init__(self):
        max_tokens_raw = getattr(config, "openai_max_tokens", None)
        try:
            self.max_tokens = int(max_tokens_raw)
        except (ValueError, TypeError):
            self.max_tokens = float('inf')
        self.openai_api_key_str = getattr(config, "openai_api_key", "")
        self.openai_api_key_list = self.openai_api_key_str.split(",") if self.openai_api_key_str else []
        self.model = str(getattr(config, "openai_chat_model", "gpt-3.5-turbo"))
        self.proxy = str(getattr(config, "openai_api_proxy", ""))
        self.select_chat_link_str = getattr(config, "select_chat_link", "")
        self.select_chat_link = re.findall(r'https?://\S+', self.select_chat_link_str) if self.select_chat_link_str else ['https://api.openai.com/v1/chat/completions', 'https://api.chatanywhere.cn/v1/chat/completions']
        select_chat_link_model_raw = getattr(config, "select_chat_link_model", 0)
        self.select_chat_link_model = int(select_chat_link_model_raw) if isinstance(select_chat_link_model_raw, int) else 0
        self.api_url = self.select_chat_link[self.select_chat_link_model]
        self.api_key = self.openai_api_key_list[self.select_chat_link_model]
        ban_use_userid_str = str(getattr(config, "ban_use_userid", "")).strip()
        self.ban_use_userid = [user_id.strip() for user_id in ban_use_userid_str.split(",")] if ban_use_userid_str else []
        if self.select_chat_link_model == 0:
            self.timeOut = None
        else:
            self.timeOut = 30
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.api_key}"
        }
        self.proxies = {}
        if self.proxy and self.select_chat_link_model == 0:
            self.proxies = {
                'http://': self.proxy,
                'https://': self.proxy
            }
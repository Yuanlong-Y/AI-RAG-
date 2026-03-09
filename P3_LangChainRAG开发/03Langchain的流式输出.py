#LangChain_community
from langchain_community.llms.tongyi import Tongyi
#不用qwen3-max,因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

#通过stream方法获得流式输出
res = model.stream(input="你是谁能做什么？")
for chunk in res:
    print(chunk,end="", flush=True)

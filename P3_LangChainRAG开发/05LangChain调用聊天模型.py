from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

#得到模型对象，qwen3-max就是聊天模型
model = ChatTongyi(model="qwen3-max")

#准备消息列表
messages = [
    SystemMessage(content="你是一个边塞词人"),
    HumanMessage(content="写一首宋词"),
    AIMessage(content="独立小桥等风满袖，去年此门依旧，夜灯为君留，归来否"),
    HumanMessage(content="按照你上一个回复的格式，再写一首宋词")
           ]

#调用stream流式输出
res = model.stream(input=messages)

#for循环迭代打印输出, 通过.content来获取到输出内容
for chunk in res:
    print(chunk.content, end="", flush=True)
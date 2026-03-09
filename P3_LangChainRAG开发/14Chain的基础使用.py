from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人。"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗")
    ]
)
history_data=[
    ("human","你来写一首唐诗"),
    ("ai","床前明月光，疑是地上霜。举头望明月，低头思故乡"),
    ("human","再来一首"),
    ("human","两个黄鹂鸣翠柳，一行白鹭上青天。窗含西岭千秋雪，门泊东吴万里船")
]
#组成链，要求每一个组件都是Runnable接口的子类
model = ChatTongyi(model = "qwen3-max")
chain = chat_prompt_template | model
#通过链去调用invoke或stream
res=chain.invoke({"history":history_data})
print(res.content)
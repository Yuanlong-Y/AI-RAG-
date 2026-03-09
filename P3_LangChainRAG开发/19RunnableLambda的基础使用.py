from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

#创建所需的解析器
str_parser = StrOutputParser()

model = ChatTongyi(model="qwen3-max")
#第一个提示词
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请个双音节名字，并封装到Json格式，返回给我"
)
#第二个提示词
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义。"
)
#函数的入参：AIMassage ->dict ({"name":"xxx"})
my_func = RunnableLambda(lambda ai_msg: {"name":ai_msg.content})
#构建链
chain = first_prompt | model | my_func|second_prompt|model|str_parser

for chunk in chain.stream({"lastname":"杨","gender":"女儿"}):
    print(chunk,end="",flush=True)
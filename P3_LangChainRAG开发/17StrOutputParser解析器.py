from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser = StrOutputParser()

model=ChatTongyi(model="qwen3-max")
prompt=PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名"
)

chain = prompt|model|parser|model
#invoke输出
# res = chain.invoke({"lastname":"杨","gender":"女儿"})
# print(res)

#stream流式输出
for chunk in chain.stream({"lastname":"杨","gender":"女儿"}):
    print(chunk.content,end="",flush=True)
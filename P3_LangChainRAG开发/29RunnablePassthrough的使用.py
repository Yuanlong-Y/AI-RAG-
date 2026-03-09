from langchain_core.documents import Document
from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import Runnable, RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的参考资料为主,简洁回答问题。参考资料：{context}。"),
        ("user","用户提问：{input}")
    ]
)
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))
#准备资料（向量库的数据）
#add_texts传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练","在减肥期间饮食很重要，药注意清淡少油控制卡路里","跑步就是很好的运动"])
input_text="怎么减肥？"

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

#langchain中向量存储对象，有一个方法：as_retriever,可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kwargs = {"k":2})

def format_func(docs: list[Document]):
    if not docs:
        return"无相关参考资料"

    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"

    return formatted_str

#chain
chain = (
    {"input": RunnablePassthrough(),"context":retriever | format_func} | prompt | print_prompt | model | StrOutputParser()
)
res = chain.invoke(input_text)
print(res)
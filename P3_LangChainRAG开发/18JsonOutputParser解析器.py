from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

#创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen3-max")
#第一个提示词
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请个双音节名字，并封装到Json格式，返回给我"
    "要求key是name，value就是起的名字，请严格遵循格式要求"
)
#第二个提示词
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义。"
)
#构建链
chain = first_prompt | model | json_parser|second_prompt|model|str_parser
res = chain.invoke({"lastname":"杨","gender":"儿子"})
print(res)
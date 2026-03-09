from langchain_core.prompts import  PromptTemplate
from langchain_community.llms.tongyi import Tongyi
#zero shot
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字，简单回答。"
)
model = Tongyi(model="qwen-max")
# #调用format方法注入信息即可
# prompt_text = prompt_template.format(lastname= "杨",gender="女儿")
#
# res = model.invoke(input=prompt_text)
# print(res)

chain = prompt_template | model

res = chain.invoke({"lastname":"杨","gender":"儿子"})
print(res)


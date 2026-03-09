from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(), "="*20)
    return full_prompt
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "你需要根据对话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请给出回答"
)
str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(), "="*20)
    return full_prompt

base_chain = prompt|print_prompt|model|str_parser

store = {}                #key就是session，value就是InMemoryChatMessageHistory类对象
 #实现通过会话ID获取InMemoryChatMessageHistory类对象的函数
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

#创建一个新的链，对原有链增强功能：自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,              #增强原有chain
    get_history,             #通过会话ID获取历时会话的函数
    input_messages_key= "input",   #表示用户输入在模板中的占位符
    history_messages_key="chat_history"         #表示历史会话在模板中的占位符
)

if __name__ == '__main__':
#如下固定格式，配置当前会话的ID
   session_config = {
       "configurable":{
           "session_id":"user_001"
       }
   }

   res = conversation_chain.invoke({"input":"小明有两只猫"},session_config)
   print("第一次执行：",res)
   res = conversation_chain.invoke({"input":"小红有两只狗"},session_config)
   print("第二次执行：",res)
   res = conversation_chain.invoke({"input":"总共有几只宠物"},session_config)
   print("第三次执行：",res)

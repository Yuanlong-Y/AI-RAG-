from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = Chroma(
    collection_name="test",              #为当前存储起个名字
    embedding_function=DashScopeEmbeddings(),       #嵌入模型
    persist_directory="./chroma_db"         #指定数据存放的文件夹
 )

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source",
)

documents = loader.load()

#id1,id2,id3....
#向量存储的新增、删除、检索
vector_store.add_documents(
    documents=documents,                                         #被添加的文档，类型：list[Document]
    ids = ["id"+str(i) for i in range(1,len(documents)+1)]    #给被添加的文档提供id
)

#删除 传入id
vector_store.delete(["id1"])
result = vector_store.similarity_search(
    "大模型"
)
print(result)
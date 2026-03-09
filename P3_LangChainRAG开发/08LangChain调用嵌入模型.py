
from langchain_community.embeddings import DashScopeEmbeddings

#创建模型对象，不传model默认用的是text-embeddings-v1
model = DashScopeEmbeddings()

#不用invoke，stream，用embed_query、embed_documents
print(model.embed_query("我喜欢你"))
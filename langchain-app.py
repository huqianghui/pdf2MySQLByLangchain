import os

from cognitiveSearch.azure_cognitive_search import retriever
# step 1) 通过自定义语义搜索retriever，从认知搜索中获取相应的文档内容
cognitiveSearchResult = retriever.get_relevant_documents("申购和赎回的数额限定")
content = cognitiveSearchResult['content']

from template.azure_open_AI_instance import chain
# step 2) 通过llm chatmode和few shot，生成相应的答案
jsonResult = chain.run(content)

# step 3) 通过codex生成相应的sql
from codex.json2sql import json2sql
sql = json2sql(jsonResult)

# step 4) 执行insert sql插入数据库
from mysqlPersistence.mysql_operation import insert_sql
insert_sql(sql)




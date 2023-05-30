# 从非结构化文档中，抽取关键数据转化为结构化数据，并存储到关系型数据中

1. 在调用这个程序之前，通过表单认知服务，实现pdf的切割与文字识别等
2. 把合适的大小快和位置关系，保存到认知服务中。

## step 1) 通过自定义语义搜索retriever，从认知搜索中获取相应的文档内容

1. langchain中定义了很多retriever，包括azure cognitive search。但是这个retriever不支持语义搜索API，所以这里客户化改了一下。
2. 在实际使用认知搜索过程中，发现如果不适用语义搜索，确实对应的scores和rank，与预期的不一致。所以还是使用语义搜索比较好。
3. 对于中文来说，需要额外配置一下分词器等。
4. 同时如果中文开启认知搜索，和一些其他的参数不匹配，需要删除掉。


## step 2) 通过llm chatmode和few shot，生成相应的答案

1. langchain的底层实现了一些常规处理，比如retry，和limitation。所以很方便也实用。
2. 在这个例子中，发现多个few-shot是相互冲突的，每次只有最后一个few-shot生效。
3. 目前改成用了few-shot3，来作为最终的案例。

## step 3) 通过codex生成相应的sql

1. 在azure openAI 的playgound中使用codex，让自然语言转成sql 与实际使用langchain中prompt词有些变化。需要把few-shot等不用以#开头。
2. 如果要生成多条记录，一定需要one-shot或者few-shot，不然的话，出不来。


## step 4) 执行insert sql插入数据库

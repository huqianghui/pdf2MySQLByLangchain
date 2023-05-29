import os

from langchain.retrievers import AzureCognitiveSearchRetriever
from cognitiveSearch.azure_cognitive_search import AzureCognitiveSearchSemanticRetriever
from langchain.chains import RetrievalQA
from langchain import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME"] = "gptkb-odk2jh5qispeo"
os.environ["AZURE_COGNITIVE_SEARCH_INDEX_NAME"] ="dataingestionindex"
os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"] = "yjiXaGvg0VjX3JLkr0MHxpx20X0w4a1M8LtQnQsQ1EAzSeB9SOUw"

#retriever = AzureCognitiveSearchSemanticRetriever(content_key="content")
# step 1) 通过自定义语义搜索retriever，从认知搜索中获取相应的文档内容
#result = retriever.get_relevant_documents("申购和赎回的数额限定")

# step 2) 通过llm chatmode和few shot，生成相应的答案
from langchain.chat_models import AzureChatOpenAI
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://openai-test-fc.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_KEY"] = "2cadf4ed0527418788a56ec5b496fa92"

chat = AzureChatOpenAI(
    deployment_name="gpt-35-turbo",
    model_name="gpt-35-turbo",
    temperature=0)

human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
from template.systemTemplate import system_message_prompt
from template.fewshot1 import few_shot_human1, few_shot_ai_template1
from template.fewshot2 import few_shot_human2, few_shot_ai_template2
from template.fewshot3 import few_shot_human3, few_shot_ai_template3
from template.fewshot4 import few_shot_human4, few_shot_ai_template4

chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt, 
    few_shot_human1, few_shot_ai_template1,
    few_shot_human2,few_shot_ai_template2, 
    few_shot_human3,few_shot_ai_template3,
    few_shot_human4,few_shot_ai_template4, 
    human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)
# get a chat completion from the formatted messages
textData = '''
（四）申购和赎回的数额限定
1、申购金额的限制
投资者单个基金账户办理基金申购业务的（含定期定额投资），首次申购的 最低金额为单笔1元，追加申购的最低金额为单笔1元。通过基金管理人直销柜 台办理基金申购业务的，首次申购的最低金额为单笔100,000元，追加申购的最 低金额为单笔10,000元；已在直销机构有认购或申购过本基金管理人管理的任 一基金（包括本基金）记录的投资人不受首次申购最低金额的限制。本基金直 销机构单笔申购最低金额可由基金管理人酌情调整。其他销售机构接受申购申 请的最低金额和业务规则以其他销售机构的规定为准，但不得低于基金管理人 规定的最低限额。投资者将当期分配的基金收益再投资时，不受最低申购金额 的限制。
2、赎回份额的限制
赎回的最低份额为1份基金份额。
3、最低保留余额的限制
每个工作日投资人在单个交易账户保留的本基金份额余额少于1份时，若当
日该账户同时有基金份额减少类业务（如赎回、转换出等）被确认，则基金管 理人有权将投资人在该账户保留的本基金份额一次性全部赎回。
4、当接受申购申请对存量基金份额持有人利益构成潜在重大不利影响时， 基金管理人应当采取设定单一投资者申购金额上限或基金单日净申购比例上限、 拒绝大额申购、暂停基金申购等措施，切实保护存量基金份额持有人的合法权 益。基金管理人基于投资运作与风险控制的需要，可采取上述措施对基金规模 予以控制。具体见基金管理人相关公告。
5、基金管理人可根据市场情况，在法律法规允许的情况下，调整申购的金
32 华泰保兴长三角金融债一年定期开放债券型证券投资基金招募说明书
额和赎回的份额以及最低基金份额保留余额的数量限制，基金管理人必须在调 整实施前依照《信息披露办法》的有关规定在规定媒介上刊登公告。
6、基金管理人可以规定单个投资人累计持有的基金份额上限或者单日或单 笔申购金额上限，具体规定请参见相关公告。
7、基金管理人可以规定基金份额持有人持有本基金的最高限额和本基金的 总规模限额和单日净申购比例上限，但最迟应在新的限额实施前依照《信息披 露办法》的有关规定在规定媒介上公告。
'''

jsonResult = chain.run(textData)

print(jsonResult)




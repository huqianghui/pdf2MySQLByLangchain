import os
from cognitiveSearch.azureCognitiveSearchSemanticRetriever import AzureCognitiveSearchSemanticRetriever

os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME"] = "gptkb-odk2jh5qispeo"
os.environ["AZURE_COGNITIVE_SEARCH_INDEX_NAME"] ="dataingestionindex"
os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"] = "XXXXX"

retriever = AzureCognitiveSearchSemanticRetriever(content_key="content")

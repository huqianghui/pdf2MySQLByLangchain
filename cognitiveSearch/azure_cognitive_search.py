import os
from cognitiveSearch.azureCognitiveSearchSemanticRetriever import AzureCognitiveSearchSemanticRetriever

os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME"] = "gptkb-odk2jh5qispeo"
os.environ["AZURE_COGNITIVE_SEARCH_INDEX_NAME"] ="dataingestionindex"
os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"] = "yjiXaGvg0VjX3JLkr0MHxpx20X0w4a1M8LtQnQsQ1EAzSeB9SOUw"

retriever = AzureCognitiveSearchSemanticRetriever(content_key="content")

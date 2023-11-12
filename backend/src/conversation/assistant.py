import logging
from typing import List

from openai import OpenAI
import json

from src import db as models
from src.config import settings
from src.deps import get_db
from src.schemas.search import DocumentSearchResult
from src.services import embeddings
from src.services.search import get_document_search_results

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.1
SEED = "You are a trustworthy assistant for summarizing real time insights to help drive business decisions for a global leader in stainless steel manufacturing."

# function description for fetching additional information
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "fetch_documents",
            "description": "Fetch additional documents for summarizing",
            "parameters": {
                "type": "object",
                "properties": {
                    # "keywords": {
                    #     "type": "array",
                    #     "description": "list of keywords for searching the information",
                    #     "items": {
                    #         "type": "string",
                    #     }
                    # },
                    # "queries": {
                    #     "type": "array",
                    #     "description": "list queries in the form of sentences for searching the information",
                    #     "items": {
                    #         "type": "string",
                    #     }
                    # },
                    # "source": {
                    #     "type": "string",
                    #     "enum": ["news", "patents", "journals", "social media", "internet"],
                    #     "description": "the main type of source for the information"
                    # }
                    "query": {
                        "type": "string",
                        "description": "query for searching additional documents",
                    },
                },
                # "required": ["keywords", "queries", "source"]
                "required": ["query"]
            }
        },
    }
]


client = OpenAI(api_key=settings.OPENAI_KEY)


class Assistant:
    def __init__(self, messages: List = None, verbose: bool = False):
        self._messages = messages if messages else [
            {"role": "system", "content": SEED}
        ]
        self._documents = []
        self._verbose = verbose

    def get_messages(self) -> List:
        return self._messages

    def get_documents(self) -> List[DocumentSearchResult]:
        return self._documents

    def start(self, query: str, documents: List[DocumentSearchResult]) -> List:
        """
        Start conversation with initial prompt for summarizing and the data
        """

        prompt = f"Summarize answer in two paragraphs to the following question from the documents provided below: {query}"
        self._write(prompt)

        self._documents.extend(documents)

        for document in documents:
            prompt = f"""
            Title: {document.link_title}
            Metadata: {document.meta}
            Text:
            {document.full_text}
            """
            self._write(prompt)

        return self._submit()

    def run(self, query: str) -> List:
        """
        Make additional prompts in the conversation
        """
        self._write(query)
        return self._submit()

    def _write(self, message: str, role: str = "user"):
        self._messages.append({"role": role, "content": message})

    def _submit(self) -> List:
        response = client.chat.completions.create(
            model=MODEL,
            messages=self._messages,
            temperature=TEMPERATURE,
            tools=TOOLS
        )
        message = response.choices[0].message

        self._messages.append(message)  # TODO: fix type

        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name  # only one function
                function_args = json.loads(tool_call.function.arguments)  # TODO: json may be incorrect -> handle errors

                function_response = self._handle_fetch(
                    # keywords=function_args.get("keywords"),
                    # queries=function_args.get("queries"),
                    # source=function_args.get("source"),
                    query=function_args.get("query"),
                )

                self._messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )

            return self._submit()  # process tool calls recursively

        return self._messages

    def _handle_fetch(self, query: str) -> str:
        if self._verbose:
            print(query)

        logging.debug(f"assistant additional fetch: {query}")

        db = next(get_db())
        results = embeddings.search(query=query, limit=5)
        documents = get_document_search_results(db, results)

        self._documents.extend(documents)

        response = ""
        for document in documents:
            content = f"""
            Title: {document.link_title}
            Metadata: {document.meta}
            Text:
            {document.full_text}

            """
            response += content

        return response


# assistant store
assistants = {}


def get_assistant(id_: str) -> Assistant:
    if id_ in assistants:
        return assistants[id_]

    assistant = Assistant()
    assistants[id_] = assistant

    return assistant


def test():
    question = "What recent news state about possible energy price developments over the next three months?"
    texts = [
        "Energy prices dropped considerably at the onset of the pandemic in 2020, as the global demand for energy declined due to lockdown measures and reduced economic activity. For example, the Brent crude oil price dropped by 75% between February and April 20201.",
        "Energy prices recovered gradually in the second half of 2020 and the first half of 2021, as the demand for energy picked up with the easing of restrictions and the rollout of vaccines. However, the recovery was uneven across different energy sources, with gas prices reaching pre-pandemic levels in September 2020 and oil prices doing so in February 20211.",
        "Energy prices surged in the second half of 2021 and the first half of 2022, reaching record-high levels for some energy sources, such as natural gas and electricity. This surge was driven by a combination of factors, including supply shortages, low inventories, high demand, weather conditions, and geopolitical uncertainties. For instance, European gas prices increased by 145% since July 2021, while oil prices increased by 46% over the same period1.",
        "Energy prices are expected to remain high for longer, as the supply-demand imbalance persists and the geopolitical risks escalate. The World Bank projects that energy prices will increase by 50% on average in 2022, with coal prices, natural gas prices, and crude oil prices increasing by 81%, 74%, and 42%, respectively2. The International Energy Agency forecasts that energy prices will remain elevated until at least 20243.",
    ]

    def print_messages(messages: List):
        for message in messages:
            params = message if type(message) is dict else message.__dict__  # message can be dict or ChatCompletionMessage
            print(params["role"], ":", params["content"])

    assistant = Assistant(verbose=True)
    print_messages(assistant.start(question, texts))

    while True:
        query = input("> ")
        print_messages(assistant.run(query))


if __name__ == '__main__':
    test()

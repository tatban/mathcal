from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI
from typing import Union


llm = ChatOpenAI(
    model_name="qwen2.5:0.5b",
    api_key="ollama",
    base_url="http://ollama:11434/v1",
    temperature=0.0,
)

math_chain = LLMMathChain.from_llm(llm, verbose=False)


def eval_text_question(question: str) -> Union[float, None]:
    res = math_chain.invoke(question).get("answer", None)
    if res and isinstance(res, str):
        res = res.replace("Answer:", "").strip()
        return float(res)
    else:
        return None


if __name__ == "__main__":
    print(eval_text_question("2 times 3.5"))

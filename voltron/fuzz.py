from .llm import utils

def initialize_llm():
    clt = utils.login()

def fuzz_one():
    clt = utils.login()
    ans = utils.chatllm(clt, "Hello")
    return ans

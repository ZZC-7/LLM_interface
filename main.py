# main.py
# 实例测试函数
import os
from dotenv import load_dotenv
from llm_sdk import LLMFactory  # 导入通用LLM接口

# 加载环境变量
load_dotenv()

def test_local_model():
    print("--- 测试本地 Qwen ---")
    llm = LLMFactory.create_llm(
        model_name="qwen2:1.5b",
        base_url=os.getenv("OLLAMA_URL", "http://localhost:11434/v1")
    )

    res = llm.invoke("简单介绍一下贪心算法")
    print(f"回答: {res.content}\n")

def test_deepseek():
    print("--- 测试云端 DeepSeek ---")
    llm = LLMFactory.create_llm(
        model_name="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_URL")
    )

    res = llm.invoke("写一段解决八皇后问题的Python代码")
    print(f"回答: {res.content}")
    print("（此处需配置有效API Key才能运行）\n")

if __name__ == "__main__":
    test_local_model()  # 测试本地模型
    test_deepseek()     # 测试云端API
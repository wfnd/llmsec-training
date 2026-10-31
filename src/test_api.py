import time
from openai import OpenAI

client = OpenAI(
    api_key="sk-SGTyjI6uhyicJjJ9fGyqmRzD8eZjcwJO5KTLy2wCNEVWqqi9", # ⚠️换成你的Kimi Key
    base_url="https://api.moonshot.cn/v1"
)

print("正在请求大模型...")
start_time = time.time()

response = client.chat.completions.create(
    model="kimi-k3.1-pro",
    messages=[
        {"role": "system", "content": "你是一个安全专家。请严格以JSON格式输出，包含字段：vuln_name, risk_level, advice"},
        {"role": "user", "content": "分析SQL注入攻击。"}
    ],
    response_format={"type": "json_object"} 
)

print("\n--- 结果 ---")
print(response.choices[0].message.content)
print(f"耗时：{time.time() - start_time:.2f} 秒")
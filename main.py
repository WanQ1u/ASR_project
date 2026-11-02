import numpy as np
import requests

numbers = np.array([10, 20, 30, 40, 50])

print("ASR Project started!")
print("平均值：", np.mean(numbers))

response = requests.get("https://httpbin.org/get", timeout=10)
print("HTTP 状态码：", response.status_code)

print("Version 2")
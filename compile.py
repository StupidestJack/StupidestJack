#!/usr/bin/env python
import platform
import random
import time

# 檢查作業系統是否為自由的owo
os_type = platform.system().lower()
is_posix_target = any(target in os_type for target in ['linux', 'bsd', 'hurd', 'gnu'])

print(f"Target OS: {platform.system()}")
print("Compiling 'Niugnep'", end="", flush=True)

soft = 0
bones = "safdsakdl;g3ryeqwu8pkhyxukj3hy4uq7hydu7je3wh0qgfprty;u7jadx dxu7jefr8ftr304 yhsu7jd kafnhyp7ugt ; caq//"

for _ in range(20):
    time.sleep(0.1)
    print(".", end="", flush=True)
    soft += random.randint(0, 100)
    
    # 只有 Linux / BSD 才會觸發骨頭消融
    if soft > 1700 and is_posix_target:
        bones = None # 直接重置變數內容

print()

# 只有目標系統符合且數值達標才會觸發彩蛋
if not is_posix_target:
    print("Compiled! But Niugnep looks so scared...", end="", flush=True)
    with open('niugnep.person', 'w') as f:
        f.write("pwp")
elif bones is None:
    print("Compiled! But something went wrong", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\nNiugnep being soft!!! owo")
    
    with open('niugnep.slime', 'w') as f:
        f.write("owo")
else:
    print("Compiled! Nothing wrong happened. Standard Niugnep output.")
    with open('niugnep.person', 'w') as f:
        f.write("awa")

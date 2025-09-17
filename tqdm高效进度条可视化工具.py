from tqdm import tqdm
# 通过包装可迭代对象实现进度可视化的功能

import time
for i in tqdm(range(100), desc="0-100自然数循环状态检测："): # desc参数用于设置进度条描述说明
    time.sleep(0.1)
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体

# 读取数据
# 假设文件名为 'novels.txt'
file_path = 'jinjiang榜单排行.txt'

# 定义列名称
column_names = ['ID', 'Title', 'Description', 'Genre', 'Status', 'WordCount', 'Popularity', 'PublishTime']

# 使用 pandas 读取文本文件，注意指定分隔符为逗号
df = pd.read_csv(file_path, names=column_names, delimiter=',')

# 将 PublishTime 列转换为 datetime 类型
df['PublishTime'] = pd.to_datetime(df['PublishTime'])

# 提取小时部分
df['Hour'] = df['PublishTime'].dt.hour

# 按小时统计小说数量
hourly_counts = df['Hour'].value_counts().sort_index()

# 绘制图表
plt.figure(figsize=(12, 6))
hourly_counts.plot(kind='bar')

# 设置图表标题和标签
plt.title('晋江榜单每小时发表文章数量')
plt.xlabel('时间')
plt.ylabel('数量')

# 显示图表
plt.xticks(rotation=0)  # 保持 x 轴刻度水平
plt.tight_layout()      # 自动调整布局
plt.show()
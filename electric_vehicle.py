import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import folium
from folium.plugins import HeatMap

# 加载 CSV 文件
file_path = "Electric_Vehicle_Population_Data.csv"  # 确保这个文件路径正确
data = pd.read_csv(file_path)

# 查看前几行数据，确认加载成功
print(data.info())  # 数据基本信息
print(data.describe())  # 数值字段的统计信息
print(data.head())  # 查看前几行数据

data = data.dropna(subset=['Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'State', 'Electric Vehicle Type'])
# 检查字段是否有缺失值
print("---------------------------------------------------")
print(data.isnull().sum())

# 检查分类字段的唯一值
print(data['Electric Vehicle Type'].unique())
print(data['State'].unique())
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据文件
data = pd.read_excel("C:/Users/86176/Desktop/统计建模/数据分析/相关性分析.xlsx")

# 计算相关性矩阵
correlation_matrix = data.corr()

# 计算协方差矩阵
covariance_matrix = data.cov()

# 计算皮尔逊相关系数
pearson_corr = data.corr(method='pearson')

# 计算斯皮尔曼相关系数
spearman_corr = data.corr(method='spearman')

# 计算肯德尔相关系数
kendall_corr = data.corr(method='kendall')

# 计算点二列相关系数
point_biserial_corr = data.corr().iloc[0, 1]

# 绘制协方差矩阵热图
plt.figure(figsize=(10, 8))
sns.heatmap(covariance_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("covariance_matrix")
plt.show()

# 绘制相关性矩阵热图
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("correlation_matrix")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("pearson_corr")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("spearman_corr")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(kendall_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Kendall’s Tau Correlation Coefficient")
plt.show()

print("点二列相关系数：\n", point_biserial_corr)

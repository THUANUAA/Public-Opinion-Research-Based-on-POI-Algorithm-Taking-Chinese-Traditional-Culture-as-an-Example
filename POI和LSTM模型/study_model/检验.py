from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer import FactorAnalyzer
import pandas as pd
import numpy as np


def cronbach_alpha(items):
    """
    计算 Cronbach's alpha 系数

    参数：
    items : numpy.ndarray or list
        二维数组或列表，每一行代表一个被试者，每一列代表问卷的一个题目，每个元素为题目的得分

    返回值：
    float
        Cronbach's alpha 系数
    """
    # 转换成 numpy 数组
    items = np.array(items)

    # 计算每个题目的得分的均值
    mean_scores_per_item = np.mean(items, axis=0)

    # 计算每个被试者的总分
    total_score_per_subject = np.sum(items, axis=1)

    # 计算所有被试者的题目得分之间的协方差
    covariance_items = np.cov(items.T)

    # 计算题目的方差之和
    sum_of_variances = np.sum(np.diag(covariance_items))

    # 计算 alpha 系数
    num_items = items.shape[1]
    cronbach_alpha = (num_items / (num_items - 1)) * (1 - (sum_of_variances / np.var(total_score_per_subject)))

    return cronbach_alpha


# 读取 csv 文件并指定编码格式为 GBK
data = pd.read_csv('C:/Users/86176/Desktop/统计建模/网络舆情对中华传统文化的影响调研问卷.csv', encoding='GBK')

# 删除第一列和第一行
data = data.drop(columns=[data.columns[0]])
data = data.drop(index=[0])

# 将数据转换为二维数组
items = data.values.astype(int)

# 计算 Cronbach's alpha 系数
alpha = cronbach_alpha(items)
print("Cronbach's alpha 系数为:", alpha)


# 计算 KMO
kmo_all, kmo_model = calculate_kmo(items)
print("KMO值为:", kmo_model)

# 进行巴特利特球形度检验
chi_square_value, p_value = calculate_bartlett_sphericity(items)
print("巴特利特球形度检验结果:")
print("Chi-square值为:", chi_square_value)
print("P值为:", p_value)

import numpy as np


def relu(x):
    return np.maximum(0, x)


def calculate_EIt(df_n_t_N, df_i_t_N, n):
    sum_df_n = df_n_t_N[n]
    sum_df_i = sum([df_i_t_N[t] for t in range(1, n)])
    sum_df_i_n_1 = sum_df_i/(n-1)
    EIt = relu((sum_df_n-sum_df_i_n_1)) / (1 + sum_df_i_n_1)

    return EIt


# 示例数据
df_n_t_N = {1: 10, 2: 15, 3: 20}  # 第n天主题词t出现的消极博文数量
df_i_t_N = {1: 5, 2: 8, 3: 12}    # 第i天主题词t出现的消极博文数量
n = 1  # 第n天
EIt = calculate_EIt(df_n_t_N, df_i_t_N, n)
print(EIt)

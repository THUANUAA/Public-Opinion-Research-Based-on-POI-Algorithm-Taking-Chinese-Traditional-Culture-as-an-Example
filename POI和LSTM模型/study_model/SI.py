import numpy as np


def relu(x):
    return np.maximum(0, x)


def calculate_SIt(df_n_t_N, df_n_t_P, df_i_t_N, df_i_t_P, n):
    sum_df_n = df_n_t_N[n]
    sum_df_p = df_n_t_P[n]

    sum_i_df_n = sum([df_i_t_N[t] for t in range(1, n)])  # 第i天主题词t出现的消极博文数量从1加到n-1
    sum_i_df_p = sum([df_i_t_P[t] for t in range(1, n)])  # 第i天主题词t出现的积极博文数量从1加到n-1

    SIt = relu(sum_df_n / (1 + sum_i_df_n) - sum_df_p / (1 + sum_i_df_p))

    return SIt


# 示例数据
df_n_t_N = {1: 5, 2: 8, 3: 12}  # 第n天主题词t出现的消极博文数量
df_n_t_P = {1: 3, 2: 6, 3: 9}  # 第n天主题词t出现的积极博文数量
df_i_t_N = {1: 5, 2: 8, 3: 12}  # 第i天主题词t出现的消极博文数量
df_i_t_P = {1: 3, 2: 6, 3: 9}  # 第i天主题词t出现的积极博文数量
n = 1  # 第n天

SIt = calculate_SIt(df_n_t_N, df_n_t_P, df_i_t_N, df_i_t_P, n)
print(SIt)

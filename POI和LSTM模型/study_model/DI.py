import numpy as np


def relu(x):
    return np.maximum(0, x)


def calculate_DI_t(df_n_t_N, df_i_t_N, n):
    sum_df_n = df_n_t_N[n]
    sum_df_i = sum([df_i_t_N[t] for t in range(1, n)])
    sum_df_i_n_1 = sum_df_i / (n - 1)
    DI_temp = relu((sum_df_n - sum_df_i_n_1))
    DI_t = np.arctan(np.log(10) * (1 + DI_temp))

    return DI_t


# 示例数据
df_t = {1: 5, 2: 8, 3: 12}  # 主题词t出现的博文数量
df_i_t = {1: 5, 2: 8, 3: 12}  # 第i天主题词t出现的博文数量
n = 3  # 第n天

# 将示例数据以正确的参数传递给函数
DI_t = calculate_DI_t(df_t, df_i_t, n)
print(DI_t)

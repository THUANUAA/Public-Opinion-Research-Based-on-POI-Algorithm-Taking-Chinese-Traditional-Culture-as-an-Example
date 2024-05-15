import pandas as pd
import re


def contains_chinese(s):
    pattern = re.compile(r'[\u4e00-\u9fff]+')
    return bool(pattern.search(s))


def keep_english_numbers_punctuation(text):
    # 使用正则表达式替换非匹配字符为空字符串
    if isinstance(text, str):  # 确保text是字符串类型
        return re.sub(r'[^A-Za-z0-9\s\.,!?;:\'\"-]', '', text)
    else:
        return text


def remove_chinese(text):
    if isinstance(text, str):  # 确保text是字符串类型
        return re.sub(r'[\u4e00-\u9fff]+', '', text)
    else:
        return text


# 保留中文
def extract_chinese_and_punctuation(text):
    # 汉字和中文标点符号的正则表达式
    pattern = re.compile(r'[\u4e00-\u9fff\u3002\uff0c\uff1b\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]')
    if isinstance(text, str):
        chinese_and_punctuation = pattern.findall(text)
        return ''.join(chinese_and_punctuation)
    else:
        return text


df = pd.read_csv('孙悟空.csv', delimiter=',', encoding='utf-8-sig')
df1 = pd.read_csv('孙悟空1.csv', delimiter=',', encoding='utf-8-sig')


# 合并三个文件

ret = pd.concat([df, df1])
# 保留指定列
ret = ret[[ 'content','create_date_time','ip_location','nickname']]
# 列名格式化
ret.columns = ['content','create_date_time','ip_location','nickname']

# 去除英文
for i in range(ret.shape[0]):
    ret.content.values[i] = extract_chinese_and_punctuation(ret.content.values[i])

# 将 content 列转换为字符串类型，并处理可能存在的 NaN 值
df['content'] = df['content'].fillna('').astype(str)
# 现在你可以安全地应用 split 和 join 了
df['content'] = df['content'].apply(lambda x: ' '.join(x.split()))  # 将多个空格替换为一个空格


# 删除基于ip_location和nickname组合的重复项（保留第一个出现的组合）
ret = ret.drop_duplicates(subset=['content','create_date_time','ip_location','nickname'], keep='first')

ret.to_csv("处理后孙悟空.csv", index=False, encoding='utf-8-sig')

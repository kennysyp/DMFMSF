import numpy as np
import pandas as pd
import math

# 读取数据
association_matrix = pd.read_csv('output/association_matrix.csv', header=None, encoding='gb18030').values

# 556行，80列，每列表示一个病和各circrna是否有联系，每行表示一个rna和每个病是否有联系

# 计算disease之间的相似度

association_matrix = association_matrix.T

# 转置之后有100行，676列，每行一个disease

disease_similarity = np.zeros([80, 80])  # 100种病之间的相似度，初始化矩阵

width = 0

for m in range(80):
    width += np.sum(association_matrix[m])**0.5  # 按定义用二阶范数计算width parameter

print(width)

# 计算association_matrix
count = 0
for m in range(80):
    for n in range(80):
        disease_similarity[m, n] = math.exp((np.sum((association_matrix[m] - association_matrix[n])**2)**0.5
                                        * width/80) * (-1))  # 计算不同行（disease）之间的二阶范数
        if disease_similarity[m, n] == 1:
            disease_similarity[m, n] = 0.8  # 这里是一个大问题，两个向量相同可以说它有一定相关度，可是计算出相关度等于1又不合理，只能定义一个值


# 保存结果

result = pd.DataFrame(disease_similarity)
result.to_csv('output/disease_GaussianSimilarity.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除


# 计算circRNA之间的相似度

association_matrix = association_matrix.T  # 转置方便计算
print(len(association_matrix))
rna_similarity = np.zeros([556, 556])  # 676种circRNA之间的相似度，初始化矩阵

# 计算association_matrix
count = 0
for m in range(556):
    for n in range(556):
        rna_similarity[m, n] = math.exp((np.sum((association_matrix[m] - association_matrix[n])**2)**0.5
                                        * width/556) * (-1))
        if rna_similarity[m, n] == 1:
            rna_similarity[m, n] = 0.8  # 这里是一个大问题，两个向量相同可以说它有一定相关度，可是计算出相关度等于1又不合理，只能定义一个值


# 保存结果

result = pd.DataFrame(rna_similarity)
result.to_csv('output/rna_GaussianSimilarity.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除





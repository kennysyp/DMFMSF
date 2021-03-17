import numpy as np
import pandas as pd

# 读取数据
association_tr = pd.read_csv('data/association1.csv', header=0, encoding='gb18030')

print(len(association_tr))

rna_tr = pd.read_csv('data/rna1.csv', header=0, encoding='gb18030')
rna = rna_tr['RNA'].tolist()

disease_tr = pd.read_csv('data/disease1.csv', header=0, encoding='gb18030')
disease = disease_tr['disease'].tolist()

uniqueRna_tr = pd.read_csv('data/uniqueRna1.csv', header=0, encoding='gb18030')
rna1 = uniqueRna_tr['rna'].tolist()

uniqueDisease_tr = pd.read_csv('data/uniqueDisease1.csv', header=0, encoding='gb18030')
disease1 = uniqueDisease_tr['disease'].tolist()

print(len(rna1))
print(len(disease1))


association_matrix = np.zeros([len(rna1), len(disease1)])

# 计算association_matrix
count = 0
for m in range(len(rna1)):
    for n in range(len(disease1)):
        if len(association_tr[np.logical_and(association_tr['rna'] == rna1[m],
                                             association_tr['disease'] == disease1[n])]):
            association_matrix[m, n] = 1
            count += 1
print(count)
print(association_matrix[0: 10, 0: 10])


# 保存结果
# rna: 676, disease: 100
# 最后得到725个关系，比原始少了14个，因为这14个是重复的（如果单看rna和disease）

result = pd.DataFrame(association_matrix)
result.to_csv('output/association_matrix.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除

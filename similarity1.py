import numpy as np
import pandas as pd

# 读取数据
meshid = pd.read_csv('data/MeSH_id.csv', header=0)
disease = meshid['disease'].tolist()
id = meshid['ID'].tolist()

meshDis = pd.read_csv('data/MeSH_disease.csv', header=0)
unique_disease = meshDis['C1'].tolist()

# 初始化疾病
for j in range(len(disease)):
    disease[j] = {}

print("开始计算疾病的DV")
# DV有重复也没关系，之后再合并

for j in range(len(disease)):

    if len(id[j]) > 3:
        disease[j][id[j]] = 1
        id[j] = id[j][:-4]
        if len(id[j]) > 3:
            disease[j][id[j]] = round(1 * 0.8, 5)
            id[j] = id[j][:-4]
            if len(id[j]) > 3:
                disease[j][id[j]] = round(1 * 0.8 * 0.8, 5)
                id[j] = id[j][:-4]
                if len(id[j]) > 3:
                    disease[j][id[j]] = round(1 * 0.8 * 0.8 * 0.8, 5)
                    id[j] = id[j][:-4]
                    if len(id[j]) > 3:
                        disease[j][id[j]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                        id[j] = id[j][:-4]
                        if len(id[j]) > 3:
                            disease[j][id[j]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                            id[j] = id[j][:-4]
                            if len(id[j]) > 3:
                                disease[j][id[j]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                                id[j] = id[j][:-4]
                                if len(id[j]) > 3:
                                    disease[j][id[j]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                                    id[j] = id[j][:-4]
                                else:
                                    disease[j][id[j][:3]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                            else:
                                disease[j][id[j][:3]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                        else:
                            disease[j][id[j][:3]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                    else:
                        disease[j][id[j][:3]] = round(1 * 0.8 * 0.8 * 0.8 * 0.8, 5)
                else:
                    disease[j][id[j][:3]] = round(1 * 0.8 * 0.8 * 0.8, 5)
            else:
                disease[j][id[j][:3]] = round(1 * 0.8 * 0.8, 5)
        else:
            disease[j][id[j][:3]] = round(1 * 0.8, 5)
    else:
        disease[j][id[j][:3]] = 1

# 合并相同的病不同ID的DV

unique_disease = meshDis['C1'].tolist()

# 这个name用来判断
disease_name = meshid['disease'].tolist()
unique_disease_name = meshDis['C1'].tolist()

for j in range(len(unique_disease)):
    unique_disease[j] = {}
    for i in range(len(disease_name)):
        if unique_disease_name[j] == disease_name[i]:
            unique_disease[j].update(disease[i])


similarity = np.zeros([len(unique_disease_name), len(unique_disease_name)])

# print(similarity)

print("计算相似度")

for m in range(len(unique_disease_name)):
    for n in range(len(unique_disease_name)):
        denominator = sum(unique_disease[m].values()) + sum(unique_disease[n].values())
        numerator = 0
        for k, v in unique_disease[m].items():
            if k in unique_disease[n].keys():
                numerator += v + unique_disease[n].get(k)
        similarity[m, n] = round(numerator/denominator, 5)

print("保存结果")

# 保存结果

result = pd.DataFrame(similarity)
result.to_csv('output/similarity1.csv')

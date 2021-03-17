import math
import numpy as np
import pandas as pd

# disease = ["Meningitis, Pneumococcal", "Meningitis, Pneumococcal", "Mycetoma", "Botulism", "Botulism2", "Botulism3"]
# id = ["C01.252.200.500.600", "C08.345.654.570", "C01.252.410.040.692.606", "C01.252.410.222.151", "C01.252.410.222.151", "C03.252.410.222.151"]

print("开始读取数据")
# 读取数据
meshid = pd.read_csv('data/MeSH_id.csv', header=0)
disease = meshid['disease'].tolist()
id = meshid['ID'].tolist()

meshdis = pd.read_csv('data/MeSH_disease.csv', header=0)
unique_disease = meshdis['C1'].tolist()

# 先把各个病的整个家族储存到一个list中，把所有病储存到一个fullID中

disease_list = []
fullID = []

for j in range(len(id)):

    disease_family = [disease[j], id[j]]
    fullID.append(id[j])
    if len(id[j]) > 3:
        id[j] = id[j][:-4]
        disease_family.append(id[j])
        fullID.append(id[j])
        if len(id[j]) > 3:
            id[j] = id[j][:-4]
            disease_family.append(id[j])
            fullID.append(id[j])
            if len(id[j]) > 3:
                id[j] = id[j][:-4]
                disease_family.append(id[j])
                fullID.append(id[j])
                if len(id[j]) > 3:
                    id[j] = id[j][:-4]
                    disease_family.append(id[j])
                    fullID.append(id[j])
                    if len(id[j]) > 3:
                        id[j] = id[j][:-4]
                        disease_family.append(id[j])
                        fullID.append(id[j])
                        if len(id[j]) > 3:
                            id[j] = id[j][:-4]
                            disease_family.append(id[j])
                            fullID.append(id[j])
                            if len(id[j]) > 3:
                                id[j] = id[j][:-4]
                                disease_family.append(id[j])
                                fullID.append(id[j])
                                if len(id[j]) > 3:
                                    id[j] = id[j][:-4]
                                    disease_family.append(id[j])
                                    fullID.append(id[j])

    disease_list.append(disease_family)


id = meshid['ID'].tolist()


disease_dv = {}
countdis = len(disease)

for key in fullID:
    disease_dv[key] = round(math.log((disease_dv.get(key, 0) + 1)/countdis, 10)*(-1), 5)


id = meshid['ID'].tolist()
disease = meshid['disease'].tolist()

# 初始化疾病
for j in range(len(disease)):
    disease[j] = {}

# DV有重复也没关系，之后再合并

for j in range(len(disease)):

    if len(id[j]) > 3:
        disease[j][id[j]] = disease_dv[id[j]]
        id[j] = id[j][:-4]
        if len(id[j]) > 3:
            disease[j][id[j]] = disease_dv[id[j]]
            id[j] = id[j][:-4]
            if len(id[j]) > 3:
                disease[j][id[j]] = disease_dv[id[j]]
                id[j] = id[j][:-4]
                if len(id[j]) > 3:
                    disease[j][id[j]] = disease_dv[id[j]]
                    id[j] = id[j][:-4]
                    if len(id[j]) > 3:
                        disease[j][id[j]] = disease_dv[id[j]]
                        id[j] = id[j][:-4]
                        if len(id[j]) > 3:
                            disease[j][id[j]] = disease_dv[id[j]]
                            id[j] = id[j][:-4]
                            if len(id[j]) > 3:
                                disease[j][id[j]] = disease_dv[id[j]]
                                id[j] = id[j][:-4]
                                if len(id[j]) > 3:
                                    disease[j][id[j]] = disease_dv[id[j]]
                                    id[j] = id[j][:-4]
                                else:
                                    disease[j][id[j][:3]] = disease_dv[id[j][:3]]
                            else:
                                disease[j][id[j][:3]] = disease_dv[id[j][:3]]
                        else:
                            disease[j][id[j][:3]] = disease_dv[id[j][:3]]
                    else:
                        disease[j][id[j][:3]] = disease_dv[id[j][:3]]
                else:
                    disease[j][id[j][:3]] = disease_dv[id[j][:3]]
            else:
                disease[j][id[j][:3]] = disease_dv[id[j][:3]]
        else:
            disease[j][id[j][:3]] = disease_dv[id[j][:3]]
    else:
        disease[j][id[j][:3]] = disease_dv[id[j][:3]]


# 合并相同的病不同ID的DV

unique_disease = meshdis['C1'].tolist()

# 这个name用来判断
disease_name = meshid['disease'].tolist()
unique_disease_name = meshdis['C1'].tolist()

for j in range(len(unique_disease)):
    unique_disease[j] = {}
    for i in range(len(disease_name)):
        if unique_disease_name[j] == disease_name[i]:
            unique_disease[j].update(disease[i])


similarity = np.zeros([len(unique_disease_name), len(unique_disease_name)])


for m in range(len(unique_disease_name)):
    for n in range(len(unique_disease_name)):
        denominator = sum(unique_disease[m].values()) + sum(unique_disease[n].values())
        numerator = 0
        for k, v in unique_disease[m].items():
            if k in unique_disease[n].keys():
                numerator += v + unique_disease[n].get(k)
        similarity[m, n] = round(numerator/denominator, 5)


# 保存结果

result = pd.DataFrame(similarity)
result.to_csv('output/similarity2.csv')

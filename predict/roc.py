import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

threshold = 0.5


def roc(x, y):
    ROW_num = x.shape[0]
    COL_num = x.shape[1]
    fpr_vec = [0] * ROW_num
    tpr_vec = [0] * ROW_num
    for i in range(0, COL_num):
        lABEL = list(y[:, i])
        SCORE = list(x[:, i])
        POS = [i for i, x in enumerate(lABEL) if x == 1]
        while len(POS) > 0:
            index = lABEL.index(1)
            del lABEL[index]
            del SCORE[index]
            POS = [i for i, x in enumerate(lABEL) if x == 1]

        ## cal fpr,tpr
        col_sortedIndices = (-np.array(SCORE)).argsort()
        row_COL = len(lABEL)
        X = [0] * ROW_num
        Y = [0] * ROW_num
        P = lABEL.count(0)
        N = row_COL - P

        TP = 0
        FP = 0
        for j in range(0, row_COL):
            if lABEL[col_sortedIndices[j]] == 0:
                TP = TP + 1
            else:
                FP = FP + 1
            X[j] = FP / N  ### FPR
            Y[j] = TP / P  ### TPR

        if row_COL < ROW_num:  ### complete each column vec
            for k in range(row_COL, ROW_num):
                X[k] = X[row_COL - 1]
                Y[k] = Y[row_COL - 1]

        fpr_vec = np.array(fpr_vec) + np.array(X)
        tpr_vec = np.array(tpr_vec) + np.array(Y)

    fpr_vec = fpr_vec / COL_num
    tpr_vec = tpr_vec / COL_num

    return (fpr_vec, tpr_vec)


xs = np.load('xs.npy')
ys = np.load('ys.npy')

print(xs.shape, ys.shape)

fpr, tpr = roc(xs, ys)

auc = metrics.auc(fpr, tpr)

print("AUC:%.3f" % auc)

plt.plot(fpr, tpr, 'k--', label='Mean ROC (area = {0:.3f})'.format(auc))


plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，设置宽一点，以免和边缘重合，可以更好的观察图像的整体

plt.ylim([-0.05, 1.05])

plt.xlabel('False Positive Rate')

plt.ylabel('True Positive Rate')  # 可以使用中文，但需要导入一些库即字体

plt.title('Receiver operating characteristic example')

plt.legend(loc="lower right")

plt.show()

ROW_num, COL_num = xs.shape

y_pred = []
y_true = []
count = 0
for i in range(COL_num):
    for j in range(ROW_num):
        if ys[j][i] == 0:
            y_pred.append(1 if xs[j][i] >= threshold else 0)
            y_true.append(1)
            count += 1

PS = metrics.precision_score(y_true, y_pred)
RS = metrics.recall_score(y_true, y_pred)
F1 = metrics.f1_score(y_true, y_pred)

print(
    (' F1:%.3f, Recall:%.3f, Precision:%.3f' % (
        F1, RS, PS)).center(
        50, '='))


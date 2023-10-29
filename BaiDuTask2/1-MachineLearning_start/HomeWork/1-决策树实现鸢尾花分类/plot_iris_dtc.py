# 使用sklearn的决策树接口实现鸢尾花分类
# 补全下方的代码

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree


n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

# 加载鸢尾花数据集
iris = load_iris()

#[0,1]表示鸢尾花数据集的第一个特征和第二个特征进行配对，[0, 2] 表示使用第一个特征和第三个特征进行配对，以此类推。这样的配对组合有六种。
for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
    # 只使用两个特征
    X = iris.data[:, pair]
    y = iris.target

    # 训练决策树模型
    clf =

    # 绘制决策边界
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

    #使用训练好的决策树模型对网格点进行预测
    Z =
    Z = Z.reshape(xx.shape)

    # 对决策边界进行可视化
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    # 绘制训练数据点
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=15)


# 使用特征配对绘制决策树的决策边界
plt.suptitle("Decision surface of a decision tree using paired features")
plt.legend(loc='lower right', borderpad=0, handletextpad=0)
plt.axis("tight")

plt.figure()
# 建立一个决策树模型，用于对新样本进行分类。
clf =
#将训练好的决策树模型可视化
plot_tree(clf, filled=True)
plt.show()

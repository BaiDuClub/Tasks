# 你可以使用sklearn得逻辑回归接口来实现手写数字集MNIST的识别
# 请补全下面的代码：

import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils import check_random_state



# 记录开始时间
t0 = time.time()

# 设置训练样本数
train_samples = 5000

# 加载 MNIST 数据集
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

# 创建随机状态对象
random_state = check_random_state(0)

# 随机打乱数据集的索引
permutation = random_state.permutation(X.shape[0])
X = X[permutation]
y = y[permutation]

# 将特征数据转换为二维形式
x = X.reshape((X.shape[0], -1))

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_samples, test_size=10000)

# 特征数据预处理

x_train =
x_test =

# 创建逻辑回归分类器对象
clf =

# 训练模型


# 计算稀疏性
sparsity =

# 计算模型在测试集上的准确率
score =

# 复制特征权重
coef =

# 绘制特征权重图像
plt.figure(figsize=(10, 5))
scale = np.abs(coef).max()

for i in range(10):
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(coef[i].reshape(28, 28), interpolation='nearest',
                   cmap=plt.cm.RdBu, vmin=-scale, vmax=scale)
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l1_plot.set_xlabel('Class %i' % i)

plt.suptitle('Classification vector for...')
plt.show()

# 输出稀疏性和准确率
print("Sparsity with L1 penalty: %.2f%%" % sparsity)
print("Test score with L1 penalty: %.4f" % score)

# 计算运行时间
run_time = time.time() - t0
print('Example run in %.3f s' % run_time)
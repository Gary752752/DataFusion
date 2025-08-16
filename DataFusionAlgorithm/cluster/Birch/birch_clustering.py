import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import Birch
from collections import defaultdict

def load_multidimensional_data_with_filenames(folder_path, column_index=2):
    """
    从给定文件夹中加载多维数据，每个文件代表一个数据点，
    每个文件中的每一行的指定列（默认为第三列）代表该点的一个维度。
    同时保存文件名和对应的数据点。

    :param folder_path: 包含数据文件的文件夹路径
    :param column_index: 表示维度值的列索引，默认为2（即第三列）
    :return: 返回两个元素：一个是NumPy数组，其中每一行对应一个数据点的所有维度；
             另一个是文件名列表，顺序与NumPy数组一致。
    """
    data_points = []
    filenames = []

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                dimensions = []
                for line in file:
                    # 假设文件是用空格、逗号或其他分隔符分隔的
                    values = line.strip().split()  # 或者根据实际情况调整分隔符
                    if len(values) > column_index:
                        try:
                            dimension_value = float(values[column_index])
                            dimensions.append(dimension_value)
                        except ValueError:
                            print(f"Warning: Could not convert value to float in file {filename}.")
                            continue

                if dimensions:
                    data_points.append(dimensions)
                    filenames.append(filename)

    return np.array(data_points), filenames


# 设置数据文件夹路径
folder_path = 'D:\\myIdeaProject\\TREC\\2020Health\\Adhoc\input_nor30_60_classification\\'  # 替换为你的文件夹实际路径

# 加载数据并获取文件名
X, filenames = load_multidimensional_data_with_filenames(folder_path)

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("数据形状:", X_scaled.shape)  # 打印数据的形状以确认加载正确


# 创建Birch聚类模型实例
birch = Birch(threshold=0.5, branching_factor=18, n_clusters=12)

# 训练模型（拟合数据）
birch.fit(X_scaled)

# 获取每个样本所属的簇标签
labels = birch.labels_


# 创建一个字典来存储每个簇的文件名
clustered_files = defaultdict(list)

# 将文件名按照簇标签分组
for idx, label in enumerate(labels):
    clustered_files[label].append(filenames[idx])

# 将簇ID转换为列表并排序
sorted_clusters = sorted(clustered_files.items())

# 打印每个簇及其包含的文件名，按cluster_id顺序
print("分簇结果如下：")
for cluster_id, files in sorted_clusters:
    # 将文件列表中的文件名用 '\t' 连接成一个字符串，并在前面加上一个 tab
    files_str = '\t' + '\t'.join(files)
    # 打印簇 ID 和连接后的文件名字符串
    print(f"cluster {cluster_id}{files_str}")
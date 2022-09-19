import numpy as np
import operator

def DataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片']
    return group, labels

def knn(in_x, x_labels, y_labels, k):
    x_labels_size = x_labels.shape[0]    #0访问行数，1访问列数
    distances = (np.tile(in_x, (x_labels_size, 1)) - x_labels) ** 2
    ad_distances = distances.sum(axis=1)#按列进行相加，0的话是按行相加
    sq_distances = ad_distances ** 0.5
    ed_distances = sq_distances.argsort()#返回的是排序前的索引
    classdict = {}
    for i in range(k):
        voteI_label = y_labels[ed_distances[i]]
        classdict[voteI_label] = classdict.get(voteI_label, 0) + 1
    sort_calssdict = sorted(classdict.items(), key=operator.itemgetter(1), reverse=True)
    return sort_calssdict[0][0]

if __name__ == '__main__':
    group, labels = DataSet()
    test_x = [53, 55]
    print('输入数据对应的类型是: {}'.format(knn(test_x, group, labels, 3)))

















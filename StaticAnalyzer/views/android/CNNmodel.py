#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# sess = tf.InteractiveSession()


#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#数据读入
# Train_DataArray, Train_LabelArray, Test_DataArray, Test_LabelArray = input_data.input_file(DATASET)
# 函数申明

def weight_variable(shape):
    # 正态分布，标准差为0.1，默认最大为1，最小为-1，均值为0

    initial = tf.truncated_normal(shape, stddev=0.1)

    return tf.Variable(initial)


def bias_variable(shape):
    # 创建一个结构为shape矩阵也可以说是数组shape声明其行列，初始化所有值为0.1

    initial = tf.constant(0.1, shape == shape)

    return tf.Variable(initial)


def conv2d(x, W):
    # 卷积遍历各方向步数为1，SAME：边缘外自动补0，遍历相乘

    # padding 一般只有两个值

    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # 池化卷积结果（conv2d）池化层采用kernel大小为2*2，步数也为2，SAME：周围补0，取最大值。数据量缩小了4倍

    # x 是 CNN 第一步卷积的输出量，其shape必须为[batch, height, weight, channels];

    # ksize 是池化窗口的大小， shape为[batch, height, weight, channels]

    # stride 步长，一般是[1，stride， stride，1]

    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def cnnmodel(xs,drop=1.0):
    # 定义输入输出结构

    # 可以理解为形参，用于定义过程，执行时再赋值

    # dtype 是数据类型，常用的是tf.float32,tf.float64等数值类型

    # shape是数据形状，默认None表示输入图片的数量不定，28*28图片分辨率

    # 类别是0-9总共10个类别，对应输出分类结果

    #keep_prob = tf.placeholder(tf.float32)

    # x_image又把xs reshape成了28*28*1的形状，灰色图片的通道是1.作为训练时的input，-1代表图片数量不定

    x_image = tf.reshape(xs, [-1, 42, 26, 1])

    # 搭建网络

    # 第一层卷积池化

    # 第一二参数值得卷积核尺寸大小，即patch

    w_conv1 = weight_variable([5, 5, 1, 32])

    b_conv1 = bias_variable([32])  # 32个偏置值

    h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)  # 得到42*26*32

    h_pool1 = max_pool_2x2(h_conv1)  # 得到21*13*32

    # 第二层卷积池化

    # 第三个参数是图像通道数，第四个参数是卷积核的数目，代表会出现多少个卷积特征图像;

    w_conv2 = weight_variable([5, 5, 32, 64])

    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)  # 得到21*13*64

    h_pool2 = max_pool_2x2(h_conv2)  # 得到11*7*64

    # 第三层全连接层

    w_fc1 = weight_variable([11 * 7 * 64, 1024])

    b_fc1 = bias_variable([1024])

    # 将第二层卷积池化结果reshape成只有一行7*7*64个数据

    # [n_samples, 7, 7, 64] == [n_samples, 7 * 7 * 64]

    h_pool2_flat = tf.reshape(h_pool2, [-1, 11 * 7 * 64])

    # 卷积操作，结果是1*1*1024，单行乘以单列等于1*1矩阵，matmul实现最基本的矩阵相乘

    # 不同于tf.nn.conv2d的遍历相乘，自动认为是前行向量后列向量

    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

    # 对卷积结果执行dropout操作

    h_fc1_dropout = tf.nn.dropout(h_fc1, keep_prob=drop)

    # 第四层输出操作

    # 二维张量，1*1024矩阵卷积，共10个卷积，对应ys长度为10

    w_fc2 = weight_variable([1024, 2])

    b_fc2 = bias_variable([2])

    y_conv = tf.nn.softmax(tf.matmul(h_fc1_dropout, w_fc2) + b_fc2)
    return y_conv
#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# sess = tf.InteractiveSession()


#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#���ݶ���
# Train_DataArray, Train_LabelArray, Test_DataArray, Test_LabelArray = input_data.input_file(DATASET)
# ��������

def weight_variable(shape):
    # ��̬�ֲ�����׼��Ϊ0.1��Ĭ�����Ϊ1����СΪ-1����ֵΪ0

    initial = tf.truncated_normal(shape, stddev=0.1)

    return tf.Variable(initial)


def bias_variable(shape):
    # ����һ���ṹΪshape����Ҳ����˵������shape���������У���ʼ������ֵΪ0.1

    initial = tf.constant(0.1, shape == shape)

    return tf.Variable(initial)


def conv2d(x, W):
    # ���������������Ϊ1��SAME����Ե���Զ���0���������

    # padding һ��ֻ������ֵ

    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # �ػ���������conv2d���ػ������kernel��СΪ2*2������ҲΪ2��SAME����Χ��0��ȡ���ֵ����������С��4��

    # x �� CNN ��һ����������������shape����Ϊ[batch, height, weight, channels];

    # ksize �ǳػ����ڵĴ�С�� shapeΪ[batch, height, weight, channels]

    # stride ������һ����[1��stride�� stride��1]

    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def cnnmodel(xs,drop=1.0):
    # ������������ṹ

    # �������Ϊ�βΣ����ڶ�����̣�ִ��ʱ�ٸ�ֵ

    # dtype ���������ͣ����õ���tf.float32,tf.float64����ֵ����

    # shape��������״��Ĭ��None��ʾ����ͼƬ������������28*28ͼƬ�ֱ���

    # �����0-9�ܹ�10����𣬶�Ӧ���������

    #keep_prob = tf.placeholder(tf.float32)

    # x_image�ְ�xs reshape����28*28*1����״����ɫͼƬ��ͨ����1.��Ϊѵ��ʱ��input��-1����ͼƬ��������

    x_image = tf.reshape(xs, [-1, 42, 26, 1])

    # �����

    # ��һ�����ػ�

    # ��һ������ֵ�þ���˳ߴ��С����patch

    w_conv1 = weight_variable([5, 5, 1, 32])

    b_conv1 = bias_variable([32])  # 32��ƫ��ֵ

    h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)  # �õ�42*26*32

    h_pool1 = max_pool_2x2(h_conv1)  # �õ�21*13*32

    # �ڶ������ػ�

    # ������������ͼ��ͨ���������ĸ������Ǿ���˵���Ŀ���������ֶ��ٸ��������ͼ��;

    w_conv2 = weight_variable([5, 5, 32, 64])

    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)  # �õ�21*13*64

    h_pool2 = max_pool_2x2(h_conv2)  # �õ�11*7*64

    # ������ȫ���Ӳ�

    w_fc1 = weight_variable([11 * 7 * 64, 1024])

    b_fc1 = bias_variable([1024])

    # ���ڶ������ػ����reshape��ֻ��һ��7*7*64������

    # [n_samples, 7, 7, 64] == [n_samples, 7 * 7 * 64]

    h_pool2_flat = tf.reshape(h_pool2, [-1, 11 * 7 * 64])

    # ��������������1*1*1024�����г��Ե��е���1*1����matmulʵ��������ľ������

    # ��ͬ��tf.nn.conv2d�ı�����ˣ��Զ���Ϊ��ǰ��������������

    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

    # �Ծ�����ִ��dropout����

    h_fc1_dropout = tf.nn.dropout(h_fc1, keep_prob=drop)

    # ���Ĳ��������

    # ��ά������1*1024����������10���������Ӧys����Ϊ10

    w_fc2 = weight_variable([1024, 2])

    b_fc2 = bias_variable([2])

    y_conv = tf.nn.softmax(tf.matmul(h_fc1_dropout, w_fc2) + b_fc2)
    return y_conv
#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#����ѡȡ������Ҫ�뽨��ģ��ʱʹ�õ������ļ���ͬ
import DNN3 as DNN
import input_data
import evaluation
import CNNmodel
###############��������#################
#���ݼ���ѡ�񣬾���ο�input_data�е�ע��
DATASET = 1
#ģ��·��
Model_path = "./model1/"
#############�������ֽ���###############


#######################################���ݶ���######################################################
Train_DataArray, Train_LabelArray, Test_DataArray, Test_LabelArray = input_data.input_file(DATASET)
print(Test_DataArray.shape)
######################################���ݶ������####################################################

################placeholder�趨#####################
x = tf.placeholder('float', shape=[None, 1092], name='x-input')
y_ = tf.placeholder('float', shape=[None, 2], name='y-input')
drop_out =  tf.placeholder('float', name='dropout')
##############placeholder�趨���###################

# y��Ԥ��ֵ
y = CNNmodel.cnnmodel(x)

####################################׼ȷ�ʺ���##################################################
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#####################################�趨���###################################################

saver = tf.train.Saver()

with tf.Session() as sess:
    #������󱣴��ģ��
    sess.run(tf.global_variables_initializer())
    ckpt = tf.train.get_checkpoint_state(Model_path)
    #��ģ�ͼ��ص���ǰ������
    saver.restore(sess, ckpt.model_checkpoint_path)
    print("accuracy:",sess.run(accuracy,feed_dict={x: Test_DataArray, y_: Test_LabelArray, drop_out:0.8}))
    y_now=sess.run(y,feed_dict={x: Test_DataArray, y_: Test_LabelArray, drop_out:0.8})
    predictLabel = tf.constant(y_now)
    realLabel = tf.convert_to_tensor(Test_LabelArray)  # ��ndarrayתΪtensor
    evaluation.tf_confusion_metrics(predictLabel, realLabel, sess, feed_dict={predictLabel: y_now, realLabel: Test_LabelArray})


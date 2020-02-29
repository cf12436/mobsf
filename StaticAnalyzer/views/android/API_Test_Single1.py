#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import json
import CNNmodel as CNN
import os
def detection(API_path):
    ###############��������#################
    #ģ��·��
    Model_path = "E:/mobsf/Mobsf/StaticAnalyzer/views/android/model1/"
    #############�������ֽ���###############


    #######################################���ݶ���######################################################
    TestList=[]
    for file_name in os.listdir(API_path):
        file_path = os.path.join(API_path,file_name)
        with open(file_path, encoding='UTF-8') as f:
            data_list = json.load(f)
            TestList.append(data_list)
    x_input = np.asarray(TestList)
    ######################################���ݶ������####################################################

    ################placeholder�趨#####################
    x = tf.placeholder('float', shape=[None, 1092], name='x-input')
    drop_out =  tf.placeholder('float', name='dropout')
    ##############placeholder�趨���###################

    # y��Ԥ��ֵ
    y = CNN.cnnmodel(x,drop_out)

    saver = tf.train.Saver()

    with tf.Session() as sess:
        #������󱣴��ģ��
        sess.run(tf.global_variables_initializer())
        ckpt = tf.train.get_checkpoint_state(Model_path)
        #��ģ�ͼ��ص���ǰ������
        saver.restore(sess, ckpt.model_checkpoint_path)
        y_now = sess.run(y,feed_dict={x:x_input,drop_out:1.0})
        tf.reset_default_graph()
        return y_now

#################################################################
##           ������   ��2019.8����
##           394933437@qq.com
#################################################################
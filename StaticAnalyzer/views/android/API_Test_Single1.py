#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import json
import CNNmodel as CNN
import os
def detection(API_path):
    ###############常数部分#################
    #模型路径
    Model_path = "E:/mobsf/Mobsf/StaticAnalyzer/views/android/model1/"
    #############常数部分结束###############


    #######################################数据读入######################################################
    TestList=[]
    for file_name in os.listdir(API_path):
        file_path = os.path.join(API_path,file_name)
        with open(file_path, encoding='UTF-8') as f:
            data_list = json.load(f)
            TestList.append(data_list)
    x_input = np.asarray(TestList)
    ######################################数据读入完毕####################################################

    ################placeholder设定#####################
    x = tf.placeholder('float', shape=[None, 1092], name='x-input')
    drop_out =  tf.placeholder('float', name='dropout')
    ##############placeholder设定完毕###################

    # y是预测值
    y = CNN.cnnmodel(x,drop_out)

    saver = tf.train.Saver()

    with tf.Session() as sess:
        #读入最后保存的模型
        sess.run(tf.global_variables_initializer())
        ckpt = tf.train.get_checkpoint_state(Model_path)
        #将模型加载到当前环境中
        saver.restore(sess, ckpt.model_checkpoint_path)
        y_now = sess.run(y,feed_dict={x:x_input,drop_out:1.0})
        tf.reset_default_graph()
        return y_now

#################################################################
##           金悦祺   于2019.8整理
##           394933437@qq.com
#################################################################
#coding=gbk
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#这里选取的网络要与建立模型时使用的网络文件相同
import DNN3 as DNN
import input_data
import evaluation
import CNNmodel
###############常数部分#################
#数据集的选择，具体参考input_data中的注释
DATASET = 1
#模型路径
Model_path = "./model1/"
#############常数部分结束###############


#######################################数据读入######################################################
Train_DataArray, Train_LabelArray, Test_DataArray, Test_LabelArray = input_data.input_file(DATASET)
print(Test_DataArray.shape)
######################################数据读入完毕####################################################

################placeholder设定#####################
x = tf.placeholder('float', shape=[None, 1092], name='x-input')
y_ = tf.placeholder('float', shape=[None, 2], name='y-input')
drop_out =  tf.placeholder('float', name='dropout')
##############placeholder设定完毕###################

# y是预测值
y = CNNmodel.cnnmodel(x)

####################################准确率函数##################################################
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#####################################设定完毕###################################################

saver = tf.train.Saver()

with tf.Session() as sess:
    #读入最后保存的模型
    sess.run(tf.global_variables_initializer())
    ckpt = tf.train.get_checkpoint_state(Model_path)
    #将模型加载到当前环境中
    saver.restore(sess, ckpt.model_checkpoint_path)
    print("accuracy:",sess.run(accuracy,feed_dict={x: Test_DataArray, y_: Test_LabelArray, drop_out:0.8}))
    y_now=sess.run(y,feed_dict={x: Test_DataArray, y_: Test_LabelArray, drop_out:0.8})
    predictLabel = tf.constant(y_now)
    realLabel = tf.convert_to_tensor(Test_LabelArray)  # 将ndarray转为tensor
    evaluation.tf_confusion_metrics(predictLabel, realLabel, sess, feed_dict={predictLabel: y_now, realLabel: Test_LabelArray})


import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)
sum1 =tf.add(a,b)


# placeholder是一个占位符，feed_dict 是一个字典
"""一般用于训练模型时，实时的提供数据去进行训练"""
plt = tf.placeholder(tf.float32,[None,3])
# Tensor("Placeholder:0", shape=(?, 3), dtype=float32)
print(plt)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    # print(sess.run(sum1))
    print(sess.run(plt,feed_dict={plt:[[1,2,3],[4,5,6]]}))

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 定义一个初始化权重的函数
def weight_variables(shape):
    w = tf.Variable(tf.random_normal(shape=shape, mean=0, stddev=1.0))
    return w


# 定义一个初始化偏置的函数
def bias_variables(shape):
    bias = tf.Variable(tf.constant(0.0, shape=shape))
    return bias


def model():
    # 1. 准备数据的占位符
    with tf.variable_scope('data'):
        x = tf.placeholder(tf.float32, [None, 784])
        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2. 一卷基层 [5,5,1,32],卷积，激活，池化
    with tf.variable_scope('conv1'):
        # 随机初始化权重 [5,5,1,32]
        w_conv1 = weight_variables([5, 5, 1, 32])
        b_conv1 = bias_variables([32])

        # 对x进行形状的改变,[None,784]  [None,28,28,1]
        x_reshape = tf.reshape(x, [-1, 28, 28, 1])

        # 卷积+激活[None,28,28,1] --> [None,28,28,32]
        x_relu1 = tf.nn.relu(tf.nn.conv2d(x_reshape, w_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)

        # 池化 2*2 ,strides 2 [None,28,28,32] --> [None,14,14,32]
        x_pool1 = tf.nn.max_pool(x_relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    # 3. 二卷基层
    with tf.variable_scope('conv2'):
        # 随机初始化权重，权重[5,5,32,64],偏重[64]
        w_conv2 = weight_variables([5, 5, 32, 64])
        b_conv2 = bias_variables([64])

        x_relu2 = tf.nn.relu(tf.nn.conv2d(x_pool1, w_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)

        x_pool2 = tf.nn.max_pool(x_relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        # 4. 全连接层

        with tf.variable_scope('fullconnection'):
            # 随机初始化权重和偏置
            w_fc = weight_variables([7 * 7 * 64, 10])
            bias_fc = bias_variables([10])

            # 修改形状 [None,7,7,64] --> [None,7*7*64]
            x_fc_reshape = tf.reshape(x_pool2, [-1, 7 * 7 * 64])

            y_predict = tf.matmul(x_fc_reshape, w_fc) + bias_fc

        return x, y_true, y_predict


def con_fc():
    # 获取真实数据
    mnist = input_data.read_data_sets('./data/mnist', one_hot=True)

    x, y_true, y_predict = model()

    # 计算交叉熵损失
    with tf.variable_scope('soft_cross'):
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true,logits=y_predict))

    # 梯度下降
    with tf.variable_scope('optimizer'):
        train_op = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

    #  计算准确率
    with tf.variable_scope('acc'):
        equal_list = tf.equal(tf.argmax(y_true, 1), tf.argmax(y_predict, 1))
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 定义变量初始化op
    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)
        for i in range(2000):
            # 取出真实存在的目标值和特征值
            mnist_x, mnist_y = mnist.train.next_batch(50)
            # 运行train_op
            sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})
            print('训练第%d步，准确率为:%f' % (i, sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})))
    return None


if __name__ == '__main__':
    con_fc()

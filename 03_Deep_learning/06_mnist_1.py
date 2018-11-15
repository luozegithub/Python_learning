from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('is_train',0,'指定程序是训练还是预测')
def fullconnected():

    #获取真实数据
    mnist = input_data.read_data_sets('./data/mnist',one_hot=True)
    # 1. 建立数据的占位符，x[None,784] y[None,10]
    with tf.variable_scope('data'):
        x = tf.placeholder(tf.float32, [None, 784])
        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2. 建立一个全连接层的神经网络 w[784,10] b[10]
    with tf.variable_scope('fullconnected_model'):
        # 随机化初始权重和偏置
        weight = tf.Variable(tf.random_normal([784, 10], mean=0, stddev=1.0), name='weight')
        bias = tf.Variable(tf.constant(0.0, shape=[10]))

        # 计算预测值
        y_predict = tf.matmul(x, weight) + bias

    # 3.计算所有样本的交叉熵损失,并求出平均值
    with tf.variable_scope('softmax_cross'):
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    #   4.梯度下降
    with tf.variable_scope('optimizer'):
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    #  5.计算准确率
    with tf.variable_scope('acc'):
        equal_list = tf.equal(tf.argmax(y_true,1),tf.argmax(y_predict,1))
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))
    # 单个变量收集
    tf.summary.scalar('loss',loss)
    tf.summary.scalar('accuracy',accuracy)

    # 高纬度变量收集
    tf.summary.histogram('weight',weight)
    tf.summary.histogram('bias',bias)

    # 定义一个初始化变量的op
    init_op = tf.initialize_all_variables()

    # 定义一个合并变量
    merge_all = tf.summary.merge_all()

    # 保存模型
    saver = tf.train.Saver()
    # 开启会话去训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)
        # 迭代步数去训练，更新参数预测

        # 建立events文件，然后写入
        filewriter = tf.summary.FileWriter('./tmp',graph=sess.graph)
        if FLAGS.is_train == 1:
            for i in range(2000):
                # 取出真实存在的目标值和特征值
                mnist_x,mnist_y = mnist.train.next_batch(50)
                # 运行train_op
                sess.run(train_op,feed_dict={x:mnist_x,y_true:mnist_y})

                summary = sess.run(merge_all,feed_dict={x:mnist_x,y_true:mnist_y})

                filewriter.add_summary(summary,i)

                print('训练第%d步，准确率为:%f' %(i,sess.run(accuracy,feed_dict={x:mnist_x,y_true:mnist_y})))
            saver.save(sess,'./tmp/ckpt/fc_model')
        else:
            # 加载模型
            saver.restore(sess,'./tmp/ckpt/fc_model')

            for i in range(100):
                x_test,y_test = mnist.test.next_batch(100)
                # print('第%d张图片，手写数字图片目标值：%d，预测记过为：%d' %(
                #     i,
                #     tf.argmax(y_test,1).eval(),
                #     tf.argmax(sess.run(y_predict,feed_dict={x:x_test,y_true:y_test}),1).eval())
                # )
                print(sess.run(accuracy,feed_dict={x:x_test,y_true:y_test}))



    return None


if __name__ == '__main__':
    fullconnected()
# tensorboard --logdir="./03_Deep_learning/tmp"
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 静态形状与动态形状
def demo1():
    plt = tf.placeholder(tf.float32, [None, 2])
    print(plt)
    # 对于静态形状来说，一旦固定，不能够再次修改
    plt.set_shape([3, 2])
    print(plt)

    # 动态形状，可以跨纬度，生成一个新的对象
    plt_reshape = tf.reshape(plt, [2, 3])
    print(plt_reshape)

    with tf.Session() as sess:
        pass


# Variable 在使用的时候需要全局初始化
def demo2():
    a = tf.constant(3.0, name='a')
    b = tf.constant(4.0, name='b')
    c = tf.add(a, b, name='add')
    var = tf.Variable(tf.random_normal([2, 3], mean=0, stddev=1.0), name='var')
    print(a, b, var)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        # 生成events 事件文件，方便我们使用tensorboard可视化，tensorboard --logdir="./03_Deep_learning/tmp"
        filewriter = tf.summary.FileWriter('./tmp/', graph=sess.graph)

        print(sess.run([c, var]))


# 1、训练参数问题:trainable
# 学习率和步数的设置：

# 2、添加权重参数，损失值等在tensorboard观察的情况 1、收集变量2、合并变量写入事件文件
def myRegression():
    """自实现线性回归"""
    # 1. 准备数据 x 特征值 [100,1] y 目标值 [100]
    x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
    # 矩阵相乘 必须是二维的，我们自己造一个y
    y_true = tf.matmul(x, [[0.7]]) + 0.8

    # 2. 建立线性回归模型，1个特征，1个偏置 y = wx + b
    # 随机给一个权重，偏置的值，让他去计算损失，然后在当前状态下优化
    # trainable参数：指定这个参数是否能跟着梯度下降一起优化
    weight = tf.Variable(tf.random_normal([1, 1]), name='weight')
    bias = tf.Variable(0.0, name='bias')

    y_predict = tf.matmul(x, weight) + bias

    #  3. 建立损失函数，计算均方误差
    loss = tf.reduce_mean(tf.square(y_predict - y_true))

    #  4. 梯度下降优化损失 learning_rate 0 ~ 1, 2, 3, 5, 7, 10
    train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    init_op = tf.global_variables_initializer()

    #  scalar,histogram 展示到tensorboard
    tf.summary.scalar('losses', loss)
    tf.summary.histogram('weight', weight)

    # 定义合并到事件文件
    merged = tf.summary.merge_all()

    #  定义一个保存模型的实例
    saver = tf.train.Saver()
    # 通过会话 运行程序
    with tf.Session() as sess:
        sess.run(init_op)

        #     打印随机最先初始化的权重和偏置
        print('随机初始化的参数权重值为：%f,偏置为%f' % (weight.eval(), bias.eval()))
        file_writer = tf.summary.FileWriter('./tmp/', graph=sess.graph)

        # 加载模型，覆盖模型当中随机定义的参数，从上次训练的参数结果开始
        if os.path.exists("./tmp/ckpt/checkpoint"):
            print('load checkpoint')
            saver.restore(sess,'./tmp/ckpt/model')
        # 循环训练 运行优化
        for i in range(100):
            sess.run(train_op)

            # 运行合并的tensor
            summary = sess.run(merged)
            file_writer.add_summary(summary,i)
            print('第%d次参数权重值为：%f,偏置为%f' % (i, weight.eval(), bias.eval()))
        saver.save(sess,'./tmp/ckpt/model')
    return None


if __name__ == '__main__':
    myRegression()

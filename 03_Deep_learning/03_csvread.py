import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def csvread(filelist):
    # 1. 构造文件的队列
    file_queue = tf.train.string_input_producer(filelist)
    # 2.构造阅读器读取队列数据（默认读取一行数据）
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)
    print(key, value)

    # 3.decode
    records = [['None'], ['None']]
    example, label = tf.decode_csv(value, record_defaults=records)

    # 批处理
    # batch_size批处理大小与队列，数据的数量没有关系，只是决定了取多少个数据出来，可以重复，对结果没有影响
    # capacity 看作是容器，可以一次容纳的数据量，一般与batch_size相等，若小于，则子线程多取几次数据，达到批处理大小后，调用主线程开始训练数据
    example_batch,label_batch = tf.train.batch([example,label],batch_size=9,num_threads=1,capacity=9)

    return example_batch,label_batch


if __name__ == '__main__':
    filename = os.listdir('./data/csv')
    filelist = [os.path.join('./data/csv', file) for file in filename]
    example, label = csvread(filelist)

    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()
        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)
        # 打印读取的内容
        print(sess.run([example,label]))
        # print(example.eval())
        # 回收线程
        coord.request_stop()
        coord.join(threads)


import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('cifar_dir', './data/cifar/', '文件的目录')
tf.app.flags.DEFINE_string('cifar_tfrecords', './tmp/cifar.tfrecords', 'cifar_tfrecords的目录')


# 二进制文件的读取
class CifarRead():
    def __init__(self, filelist):
        self.filelist = filelist
        self.height = 32
        self.width = 32
        self.channel = 3
        # 存储的字节
        self.label_bytes = 1
        self.image_bytes = self.height * self.width * self.channel
        self.bytes = self.label_bytes + self.image_bytes

    def read_and_decode(self):
        # 1、构造文件队列
        file_queue = tf.train.string_input_producer(self.filelist)

        # 2、构造二进制文件读取器，读取内容, 每个样本的字节数
        reader = tf.FixedLengthRecordReader(self.bytes)

        key, value = reader.read(file_queue)

        # 3、解码内容, 二进制文件内容的解码
        label_image = tf.decode_raw(value, tf.uint8)

        print(label_image)

        # 4、分割出图片和标签数据，切除特征值和目标值
        label = tf.cast(tf.slice(label_image, [0], [self.label_bytes]), tf.int32)

        image = tf.slice(label_image, [self.label_bytes], [self.image_bytes])

        # 5、可以对图片的特征数据进行形状的改变 [3072] --> [32, 32, 3]
        image_reshape = tf.reshape(image, [self.height, self.width, self.channel])

        print(label, image_reshape)
        # 6、批处理数据
        image_batch, label_batch = tf.train.batch([image_reshape, label], batch_size=10, num_threads=1, capacity=10)

        print(image_batch, label_batch)
        return image_batch, label_batch

    def write_to_tfrecords(self, image_batch, label_batch):
        """
        注意的一点：需要提前将文件夹创建好，否则会报错，文件会自动创建
        将图片的特征值和目标值存进tfrecords
        :param image_batch: 10张图片的特征值
        :param label_batch: 10张图片的目标值
        :return: None
        """
        # 1、建立TFRecord存储器
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        # 2、循环将所有样本写入文件，每张图片样本都要构造example协议
        for i in range(10):
            # 取出第i个图片数据的特征值和目标值
            image = image_batch[i].eval().tostring()

            label = int(label_batch[i].eval()[0])

            # 构造一个样本的example
            example = tf.train.Example(features=tf.train.Features(feature={
                "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))

            # 写入单独的样本
            writer.write(example.SerializeToString())

        # 关闭
        writer.close()
        return None

    def read_from_tfrecords(self):
        # 1、构造文件队列
        file_queue = tf.train.string_input_producer([FLAGS.cifar_tfrecords])

        # 2、构造文件阅读器，读取内容example,value=一个样本的序列化example
        reader = tf.TFRecordReader()

        key, value = reader.read(file_queue)

        # 3、解析example
        features = tf.parse_single_example(value, features={
            "image": tf.FixedLenFeature([], tf.string),
            "label": tf.FixedLenFeature([], tf.int64),
        })

        # 4、解码内容, 如果读取的内容格式是string需要解码， 如果是int64,float32不需要解码
        image = tf.decode_raw(features["image"], tf.uint8)

        # 固定图片的形状，方便与批处理
        image_reshape = tf.reshape(image, [self.height, self.width, self.channel])

        label = tf.cast(features["label"], tf.int32)

        print(image_reshape, label)

        # 进行批处理
        image_batch, label_batch = tf.train.batch([image_reshape, label], batch_size=10, num_threads=1, capacity=10)

        return image_batch, label_batch

if __name__ == '__main__':
    filename = os.listdir(FLAGS.cifar_dir)
    filelist = [os.path.join(FLAGS.cifar_dir, file) for file in filename if file[0:4] == 'data']
    print(filelist)
    cf = CifarRead(filelist)
    # image_batch, label_batch = cf.read_and_decode()

    image_batch, label_batch = cf.read_from_tfrecords()
    #     开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()
        # 开启读取文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)
        #
        # print('start')
        # cf.write_to_tfrecords(image_batch, label_batch)
        # print('end')

        print(sess.run([image_batch, label_batch]))


        coord.request_stop()
        coord.join(threads)

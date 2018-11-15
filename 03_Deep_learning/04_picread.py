import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def picread(filelist):
    # 1. 构造文件队列
    file_squeue = tf.train.string_input_producer(filelist)
    # 2. 构造阅读器取读取内容
    reader = tf.WholeFileReader()
    key, value = reader.read(file_squeue)
    print(value)
    # 3. decode
    img = tf.image.decode_jpeg(value)
    print(img)
    # 4. 对图片大小进行处理，使得特征数量相同
    image_resize = tf.image.resize_images(img, [200, 200])
    print(image_resize)
    image_resize.set_shape([200,200,3])
    print(image_resize)
    # 5.在进行批处理之前需要对所有的形状进行定义，
    # 6.批处理
    image_batch=tf.train.batch([image_resize],batch_size=2,num_threads=1,capacity=2)
    return image_batch


if __name__ == '__main__':
    filename = os.listdir('./data/img')
    filelist = [os.path.join('./data/img', file) for file in filename]
    image_batch = picread(filelist)

    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()
        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)
        # 打印读取的内容
        print(sess.run(image_batch))
        # print(example.eval())
        # 回收线程
        coord.request_stop()
        coord.join(threads)

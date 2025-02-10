import time
import threading
from queue import Queue # 先入先出满足生产者消费者模型

count = 0
# 生产者
class Producer(threading.Thread):
    def __init__(self, nowTime):
        threading.Thread.__init__(self)
        self.nowTime = nowTime
    def run(self):
        global queue
        global count
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    queue.put(count)
                    print("生产了{}个产品，当前时间为：{}".format(count, self.nowTime))
            else:
                print("产品已满，当前时间为：{}".format(self.nowTime))
            time.sleep(1)

# 消费者
class Consumer(threading.Thread):
    def __init__(self, nowTime):
        threading.Thread.__init__(self)
        self.nowTime = nowTime
    def run(self):
        global queue
        global count
        while True:
            if queue.qsize() > 100:
                for i in range(30):
                    count -= 1
                    msg = self.nowTime + "消费了" + str(queue.get())
                    print(msg)
            else:
                print("产品不足，当前时间为：{}".format(self.nowTime))
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    producer = Producer(time.ctime())
    consumer = Consumer(time.ctime())
    producer.start()
    time.sleep(1)
    consumer.start()

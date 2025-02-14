import time

# 生产者
def producer(c):
    c.send(None)
    for i in range(1, 6):
        print('生产者生产了第%s个包子' % i)
        c.send(str(i) + '号包子')
        time.sleep(1)

# 消费者
def consumer():
    res = ''
    while True:
        data = yield res
        if not data:
            return
        print('消费者吃了%s' % data)

if __name__ == '__main__':
    c = consumer()
    producer(c)
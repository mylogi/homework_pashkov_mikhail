import multiprocessing
import os
import time

# Example 1:

# def test(name):
#     print(f'here {name}')
#
#
# def multi_now():
#     processes = []
#     for i in range(5):
#         t = multiprocessing.Process(target=test, args=(i,))
#         processes.append(t)
#         t.start()
#
#     for process in processes:
#         process.join()
#
#
# if __name__ == '__main__':
#     multi_now()

# Example 2:

# def test(name):
#     print(f'here {name}, process: {os.getpid()}, parent process: {os.getpid()}')
#
#
# def multi_here():
#     processes = []
#     for i in range(5):
#         t = multiprocessing.Process(target=test, args=(i,))
#         processes.append(t)
#         t.start()
#
#     for process in processes:
#         process.join()
#
#
# if __name__ == '__main__':
#     multi_here()


# Example 3:

# result = []
#
#
# def square_list(mylist):
#     global result
#     for num in mylist:
#         result.append(num * num)
#     print(f"Result(in process p1): {result}")
#
#
# def multi_process():
#     temp = [1, 2, 3, 4]
#
#     p1 = multiprocessing.Process(target=square_list, args=(temp,))
#     p1.start()
#     p1.join()
#
#
# if __name__ == '__main__':
#     multi_process()
#     print(result)


# Example 4:

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
#
# num = multiprocessing.Value('d', 0.0)
# arr = multiprocessing.Array('i', range(10))
#
#
# # print(num.value)
# # print(arr)
#
# def new_multi():
#     p = multiprocessing.Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#     print(num.value)
#     print(arr[:])
#
#
# if __name__ == '__main__':
#     new_multi()


# Example 5:

# def square_list(mylist, res):
#     global result
#     for ind, num in enumerate(mylist):
#         res[ind] = num * num
#     print(f"Result(in process p1): {res[:]}")
#
#
# temp = [1, 2, 3, 4]
# result = multiprocessing.Array('i', 4)
#
#
# def multi_process():
#     p1 = multiprocessing.Process(target=square_list, args=(temp, result))
#     p1.start()
#     p1.join()
#
#
# if __name__ == '__main__':
#     multi_process()
#     # print(result[:])


# Example 6:

# def square_list(mylist, q):
#     for num in mylist:
#         q.put(num * num)
#
#
# def read_from_queue(q):
#     while not q.empty():
#         print(q.get())
#
#
# temp = [1, 2, 3, 4]
#
#
# def multi_func():
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=square_list, args=(temp, q))
#     p2 = multiprocessing.Process(target=read_from_queue, args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#
# if __name__ == '__main__':
#     multi_func()


# Example 7:

# def sender(conn, msgs):
#     for msg in msgs:
#         conn.send(msg)
#         print(f'Send the message: {msg} from process {os.getpid()}')
#
#
# def receiver(conn):
#     while True:
#         msg = conn.recv()
#         if msg == 'END':
#             break
#         print(f'Received the message: {msg} in process {os.getpid()}')
#
#
# msgs = ['hello', 'hey', 'hru?', 'END']
#
# # creating a pipe
# parent_conn, child_conn = multiprocessing.Pipe()
#
# # creating new processes
# p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
# p2 = multiprocessing.Process(target=receiver, args=(child_conn, ))
#
# if __name__ == '__main__':
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


# Example 8:

# def f(x):
#     return x * x
#
#
# def new_attempt():
#     with multiprocessing.Pool(processes=4) as pool:
#         result = pool.apply_async(f, (10,))
#         print(result.get(timeout=1))
#
#         print(pool.map(f, range(10)))
#
#         it = pool.imap(f, range(10))
#         print(next(it))
#         print(next(it))
#         print(it.next(timeout=1))
#
#         result = pool.apply_async(time.sleep, (10,))
#         print(result.get(timeout=1))
#
#
# if __name__ == '__main__':
#     new_attempt()

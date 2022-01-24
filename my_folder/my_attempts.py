# Example 1

# with open('temp.txt', 'r') as f:
#     data = f.read()
#     print(data)
#
# print(f.closed)


# Example 2

# class ContextManager:
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# class MyCounter:
#     counter = 0
#
#     @classmethod
#     def get_num_of_usage(cls):
#         return cls.counter
#
#     def __enter__(self):
#         MyCounter.counter += 1
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'Closing context, number of contexts is {self.counter}')
#         return None
#
#
# with MyCounter() as counter:
#     print('Inside context manager suite')
#     print('Call context manager instance method to get counter value: ', counter.get_num_of_usage())
#
# with MyCounter() as counter:
#     print('Inside context manager suite')
#     print('Call context manager instance method to get counter value: ', counter.get_num_of_usage())
#
# with MyCounter() as counter:
#     print('Inside context manager suite')
#     print('Call context manager instance method to get counter value: ', counter.get_num_of_usage())


# Example 3

# from contextlib import contextmanager
#
# counter_value = 0
#
#
# @contextmanager
# def counter_func():
#     global counter_value
#     counter_value += 1
#     print('Same as inside __enter__')
#     yield counter_value
#     print('Same as inside __exit__')
#
#
# with counter_func() as counter:
#     print('Inside context manager suite')
#     print('Call context manager instance method to get counter value: ', counter)
#
# with counter_func() as counter:
#     print('Inside context manager suite')
#     print('Call context manager instance method to get counter value: ', counter)

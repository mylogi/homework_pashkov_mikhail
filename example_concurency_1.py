# from multiprocessing import Process
from threading import Thread, Lock

from config.init_logging import init_logging
from config.loggers import get_inner_logger, get_core_logger

my_thread_lock = Lock()


def make_something(value: int):
    get_inner_logger().info(value)

    with my_thread_lock:
        get_inner_logger().info(f'value_in_lock-{value}')

    return value ** 2


def main():
    # thread = Thread(
    #     target=functools.partial(
    #         make_something,
    #         13,
    #     ),
    #
    #     # target=make_something,
    #     # args=(12),
    #
    #     daemon=True,
    # )
    #
    # thread.start()
    #
    # thread.join()

    # process = Process()

    threads = [
        Thread(target=make_something, args=(item,)) for item in range(10)
    ]
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    init_logging()
    logger_ = get_core_logger()
    logger_.info('app.started')

    main()

    logger_.info('app.finished')

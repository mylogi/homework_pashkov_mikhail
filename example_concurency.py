import concurrent.futures
import random
from time import sleep

from config.init_logging import init_logging
from config.loggers import get_inner_logger, get_core_logger


def make_something(value: int):
    get_inner_logger().info(f'start-{value}')

    sleep(random.randint(0, 10) / 10)

    get_inner_logger().info(f'end-{value}')
    return value ** 2


def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     results = list(executor.map(make_something, range(100)))
    #
    # print(results)

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        results_2 = list(executor.map(make_something, range(100)))

    print(results_2)


if __name__ == '__main__':
    init_logging()
    logger_ = get_core_logger()
    logger_.info('app.started')

    main()

    logger_.info('app.finished')

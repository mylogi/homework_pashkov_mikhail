import asyncio
from asyncio import sleep

from config.init_logging import init_logging
from config.loggers import get_core_logger, get_example_logger, get_inner_logger


async def make_something(value: int):
    get_inner_logger().info(value)
    return value ** 2


async def main():
    logger = get_example_logger()

    results = await asyncio.gather(
        *[make_something(item) for item in range(10)]
    )
    logger.info(results)

    await sleep(1)

    logger.info(await make_something(23))

    loop = asyncio.get_event_loop()
    result_raw = loop.create_task(make_something(27))

    result = await result_raw
    logger.info(result)

    logger.info('Finish')


if __name__ == '__main__':
    init_logging()
    logger_ = get_core_logger()
    logger_.info('app.started')

    asyncio.run(main())

    logger_.info('app.finished')

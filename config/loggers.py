import logging


def get_core_logger():
    return logging.getLogger('core')


def get_example_logger():
    return logging.getLogger('example')


def get_inner_logger():
    return logging.getLogger('inner')


def get_custom_logger(class_name: str):
    return logging.getLogger(class_name)

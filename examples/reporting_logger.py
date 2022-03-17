import datetime
import sys

from memory_profiler import profile, LogFile
import logging


# # create logger
# logger = logging.getLogger('memory_profile_log')
# logger.setLevel(logging.DEBUG)
#
# # create file handler which logs even debug messages
# fh = logging.FileHandler("memory_profile.log")
# fh.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
#
# # add the handlers to the logger
# logger.addHandler(fh)
#
# from memory_profiler import LogFile
# import sys
#
# sys.stdout = LogFile('memory_profile_log', reportIncrementFlag=False)


def create_memory_profiler_logger(logger_name, log_file_name, logging_level, log_format):
    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(log_file_name)
    fh.setLevel(logging_level)

    # create formatter
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    sys.stdout = LogFile(logger_name)


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


@profile
def my_func1():
    a = [2] * (10 ** 6)
    b = [3] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    logger_name = 'my_memory_profiler_logger'
    logfile_name = f"memory_log_{datetime.datetime.now().isoformat()}.log"
    logging_level = logging.DEBUG
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    create_memory_profiler_logger(logger_name=logger_name, log_file_name=logfile_name, logging_level=logging_level,
                                  log_format=log_format)
    my_func()
    my_func1()

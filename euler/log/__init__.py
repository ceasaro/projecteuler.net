import logging

__author__ = 'cvw'

logging.basicConfig(filename='euler.log', level=logging.DEBUG)

def header(header):
    info("")
    info("")
    info("")
    info(header)
    info("--------------")

def debug(message):
    logging.debug(msg=message)

def info(message):
    logging.info(msg=message)

def warn(message):
    logging.warn(msg=message)

def error(message):
    logging.error(msg=message)


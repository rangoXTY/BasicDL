import logging

initialized_logger = {}


def get_root_logger(logger_name="my_dl", log_level=logging.INFO, log_file=None):
    """Get the root logger

    Args:
        logger_name (str, optional): root logger name. Default 'my_dl'.
        log_level (): Defaults to logging.INFO.
        log_file (str | None): The log filename. If specified, a FileHandler will
            be added to the root logger.

    Returns:
        logging.Logger: The root logger.
    """
    logger = logging.getLogger(logger_name)
    # if the logger has been initialized, just return it.
    if logger_name in initialized_logger:
        return logger

    format_str = "%(asctime)s %(levelname)s: %(message)s"
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(format_str))
    logger.addHandler(stream_handler)
    logger.propagate = False
    if log_file is None:
        logger.setLevel(log_level)
    elif log_file is not None:
        logger.setLevel(log_level)
        # add file handler
        file_handler = logging.FileHandler()
        file_handler.setFormatter(logging.Formatter(format_str))
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
    initialized_logger[logger_name] = True

    return logger

import os
from loguru import logger


def setup_logger(lop_path):
    logger.remove()
    logger.add(
        f"{lop_path}/service_pars_{{time:YYYY-MM-DD}}.log",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {extra}",
        level="INFO",
        mode="w",
        serialize=True
    )
    return logger


log_dir = os.getenv("LOG_DIR", "/logs")
os.makedirs(log_dir, exist_ok=True)

lg = setup_logger(log_dir)


def log_event(event, level="INFO", **kwargs):
    log = lg.bind(event=event, **kwargs)
    log_method = getattr(log, level.lower(), log.info)
    log_method(f"Event: {event}")


def log_error(error_message, exception=None, context=None):
    extra = context or {}
    
    log = lg.bind(event="error", **extra)
    if exception:
        log.error(f"Error: {error_message}", exc_info=exception)
    else:
        log.error(f"Error: {error_message}")

import logging.config

from ecommerce_worker.configuration.logger import get_logger_config
from ..base import *

# For the record, we can't import settings from production module because a syslogger is
# configured there.

BROKER_URL = "redis://redis:6379"

JWT_SECRET_KEY = "6cOM7Nag34onNqtCSa5V4HWP"
JWT_ISSUER = "http://local.overhang.io/oauth2"

logging.config.dictConfig(
    get_logger_config(
        log_dir="/var/log",
        edx_filename="ecommerce_worker.log",
        dev_env=True,
        debug=False,
        local_loglevel="INFO",
    )
)
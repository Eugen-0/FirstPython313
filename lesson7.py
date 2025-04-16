import os
import logging.config

LOGGING_CFG = {
    "version": 1,
    'formatters': {
        'lesson7_format': {
            'format': '%(asctime) s [%(levelname)s]% (filename)s:%(lineno)i%(message) s'
        },
    },
    "handlers": {
        "lesson7_handle": {
            "level": "info",
            "class": "logging.FileHandler",
            'formatter': 'lesson7_format',
            "filename": os.path.join(os.getcwd(), "../lesson7.log"),
        },
    },
    "loggers":{
        "lesson7_log":{
            "handlers":["lesson7_handle"],
            "level":"INFO",
        },
    },
}
logging.config.dictConfig(LOGGING_CFG)
logger = logging.getLogger(lesson7_log)
logger.info('test')

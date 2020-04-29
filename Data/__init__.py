import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError, DBAPIError

Base = declarative_base()

def retryableTransaction(retries=5):
    def decoratorFunction(f):
        def retryFunction(callerObject, *args, **kwargs):
            handleTries = retries
            while handleTries > 0:
                try:
                    return f(callerObject, *args, **kwargs)
                except (SQLAlchemyError, DBAPIError) as exception:
                    callerObject.session.rollback()
                    logger = logging.getLogger("cjsnow")
                    logger.error("{} {}".format(exception._message, "Retrying!" if handleTries > 1 else "Giving up..."))
                    handleTries -= 1
            return f
        return retryFunction
    return decoratorFunction
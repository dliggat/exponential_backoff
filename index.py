import logging
import os

from exponential_backoff.utility import Utility
from exponential_backoff.retryer import Retryer


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    """Entry point for the Lambda function."""
    a = Retryer('vol-09df3b7e27d642083')


    for i in range(20):
        logger.info('Attempt: {0}'.format(i))
        snapshot_id = a.go()
        logger.info('The snapshot id is: {0}'.format(snapshot_id))


if __name__ == '__main__':
    from exponential_backoff.localcontext import LocalContext
    handler(None, LocalContext())

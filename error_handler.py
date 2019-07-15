import boto3
import os
from datetime import datetime

failure = 'FAILURE'


def error_handling(expr, notify_type=failure):
    def error_handling_decorator(func):
        def wrapper(*args):
            try:
                return func(*args)

            except Exception as e:
                if 'local_vars' not in dir(e):
                    e.local_vars = vars()

                if notify_type == failure:
                    send_message(message=f'Error Raised {e}')

                raise e

        return wrapper
    return error_handling_decorator


def send_message(message):
    s3 = boto3.resource('s3')
    filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    s3.Object(os.environ['S3_BUCKET'], filename1).put(Body=message)


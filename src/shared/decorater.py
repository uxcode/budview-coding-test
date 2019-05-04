import datetime


def timer(func):
    def decorated(*args):
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()

        delta_time = end_time - start_time
        print()
        print('It has taken {} secs'.format(delta_time.total_seconds()))

    return decorated

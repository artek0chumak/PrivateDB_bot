import datetime
from numpy import floating


def pretty_view(data):
    if isinstance(data, datetime.datetime):
        return data.isoformat(sep=' ', timespec='seconds')
    elif isinstance(data, (float, floating)):
        return '{0:.3%}'.format(data)
    else:
        return str(data)
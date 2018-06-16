import datetime
import json
from numpy import floating


class PrettyView:
    def __init__(self):
        with open('config.json', 'r') as f:
            format_config = json.load(f)['format']

        self.point = format_config['float_point']
        self.date = format_config['date_format']
        self.timespec = format_config['timespec']
        self.sep = format_config['date_time_separator']

    def __call__(self, data):
        if isinstance(data, datetime.datetime):
            if self.date == 'ISO':
                return data.isoformat(sep=self.sep, timespec=self.timespec)
            else:
                return data.strftime(self.date)
        elif isinstance(data, (float, floating)):
            return ('{0:.' + '{0}'.format(self.point) + '}').format(data)
        else:
            return str(data)

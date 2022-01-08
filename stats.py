from datetime import datetime

class Stats:
    def __init__(self, command, id):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()
        # self.print_stats()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print(f'\nid: {self.id}')
        print(f'command: {self.command}')
        print(f'response: {self.response}')
        print(f'start time: {self.start_time}')
        print(f'end_time: {self.end_time}')
        print(f'duration: {self.duration} \n')

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        str = ''
        str +=  (f'\nid: {self.id}\n')
        str += (f'command: {self.command}\n')
        str += (f'response: {self.response}\n')
        str += (f'start time: {self.start_time}\n')
        str += (f'end_time: {self.end_time}\n')
        str += (f'duration: {self.duration}\n')
        return str
"""TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.


The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels=None):
        if channels is None:
            channels = CHANNELS
        self.channels = channels
        self.current_channel_counter = 0

    def first_channel(self):
        print(self.channels[0])
        self.current_channel_counter = 0

    def last_channel(self):
        print(self.channels[-1])
        self.current_channel_counter = -1

    def turn_channel(self, turn_channel):
        self.current_channel_counter = turn_channel - 1
        print(self.channels[self.current_channel_counter])

    def next_channel(self):
        self.current_channel_counter += 1
        print(self.channels[self.current_channel_counter])

    def previous_channel(self):
        self.current_channel_counter -= 1
        print(self.channels[self.current_channel_counter])

    def current_channel(self):
        print(self.channels[self.current_channel_counter])

    def is_exist(self, what):
        if type(what) == str:
            if what in self.channels:
                print('Yes')
            else:
                print('No')
        elif type(what) == int:
            if what in range(len(self.channels)):
                print('Yes')
            else:
                print('No')


TVC = TVController()
TVC.first_channel()
TVC.last_channel()
TVC.turn_channel(2)
TVC.next_channel()
TVC.previous_channel()
TVC.current_channel()
TVC.is_exist(4)
TVC.is_exist('BBC')

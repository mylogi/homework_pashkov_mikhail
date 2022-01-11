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

# CHANNELS = ["BBC", "Discovery", "TV1000"]
#
#
# class TVController:
#     controller = CHANNELS
#
#     def __init__(self, current_channel):
#         self.current_channel = current_channel
#
#     def first_channel(self, first_channel=0):
#         print(TVController.controller[first_channel])
#
#     def last_channel(self, last_channel=-1):
#         print(TVController.controller[last_channel])
#
#     def turn_channel(self, turn_channel):
#         self.current_channel = turn_channel - 1
#         print(TVController.controller[self.current_channel])
#
#     def next_channel(self, next_channel):
#         if self.current_channel =
# # like = TVController(0)
# # print(like.current_channel)
# # like.turn_channel()
# # print(like.current_channel)

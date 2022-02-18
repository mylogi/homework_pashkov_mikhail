# import requests
#
# url = 'https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol'
#
# requests.get(url)
#
# resp = requests.get(url)
#
# # help(resp)
#
# print(resp.status_code)
#
# print(resp.ok)
#
# # print(resp.text)
#
# # print(resp.content)
#
# resp = requests.get('https://api.github.com')
#
# # print(resp.json())
# #
# # print(resp.headers)
#
# base_url = 'https://api.pushshift.io/reddit/comment/search/'
#
# r = requests.get(base_url)
# data = r.json()
# # print(data)
#
#
# def get_data(url, params):
#     r = requests.get(base_url, params=params)
#     print('Requests sent to: ', r.url)
#     return r.json()
#
#
# data = get_data(base_url, {'subreddit': 'python'})
# # print(data)
#
# # print(data['data'][0])
#
# params = {'subreddit': 'python', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 5}
# data = get_data(base_url, params)
# print(data)Add

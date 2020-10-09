# # import subprocess
# # # youtube-dl is required to be up-to-date
# # subprocess.call('pip install --upgrade youtube-dl', shell=True)
# #
# # import youtube_dl
# #
# # ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})
# #
# # print("################## Online Video Downloader ##################")
# # # url = input("I am asking you for a URL: ")
# #
# # with ydl:
# #     result = ydl.extract_info(
# #         url='put your url here',
# #         download=False
# #     )
# #
# # #
# # # for key,value in result.items():
# # #     print(key,"  :::  ",value)
# #
# # # available_formats = []
# # #
# # # for value in result['formats']:
# # #     print(value)
# # #     available_formats.append('extension: {}, Quality: {}'.format(value['ext'], value['format_note']))
# # #
# # # print(end='\n)))))))))))))))))))))))))))))))))))))))))))))))))))))))\n')
# # # for x in available_formats:
# # #     print(x)
# #
# # if 'entries' in result:
# #     # Can be a playlist or a list of videos
# #     video = result['entries'][0]
# # else:
# #     # Just a video
# #     video = result
# #
# # print(video)
# #
#
# # arr = [1,2,3,4]
# # print(sum(arr[:2]))
#
#
# ##############################
# #
# # import bisect as b
# # b.bisect_left()
# # n, m, k = [int(x) for x in input().split()]
# # sum_ = m*k
# # a = [k] * m
# # arr = [int(y)-1 for y in input().split()]
# # count = 0
# #
# # print(len(arr), len(a))
# #
# # for x in arr:
# #     if x>= 1200:
# #         print(x, True)
# #
# # for j in range(n):
# #     x = arr[j]-1
# #     if sum_ == 0:
# #         count += 1
# #     elif a[x] > 0:
# #         sum_ -= 1
# #         a[x] -= 1
# #     else:
# #         count += 1
# #         i = x
# #         while a[i] == 0:
# #             i = (i+1) % m
# #         a[i] -= 1
# #         sum_ -= 1
# #
# # print(count)
#
# ##################
# dict_ = {'a' : 1,
#          'b': 2,
#          'c': 3}
#
# keys = list(dict_.keys())
# print(keys)
#
# l1 = [1,2,3,4]
# import bisect as b
# index = b.bisect_left(l1, 5)
# print(index)
#
# # n, m, k = [int(x) for x in input().split()]
# # sum_ = m*k
# # a = [k] * m
# # arr = [int(y)-1 for y in input().split()]
# # count = 0
# # for j in range(n):
# #     x = arr[j]
# #     if sum_ == 0:
# #         count += 1
# #     elif a[x] > 0:
# #         sum_ -= 1
# #         a[x] -= 1
# #     else:
# #         count += 1
# #         i = x
# #         while a[i] == 0:
# #             i = (i+1) % m
# #         a[i] -= 1
# #         sum_ -= 1
# #
# # print(count)
#
#
# import bisect as b
# n, m, k = [int(x) for x in input().split()]
# a = [k] * m
# arr = [int(y)-1 for y in input().split()]
# count = 0
#
# available_rows = list(range(0, m))
#
# for j in range(n):
#     x = arr[j]
#     if not available_rows:
#         count += 1
#     elif a[x] > 0:
#         a[x] -= 1
#         if a[x] == 0:
#             deleting_index = b.bisect_left(available_rows, x)
#             del available_rows[deleting_index]
#     else:
#         count += 1
#         index = b.bisect_left(available_rows, x)
#         try:
#             a[available_rows[index]] -= 1
#         except IndexError:
#             index = 0
#             a[available_rows[index]] -= 1
#         if a[available_rows[index]] == 0:
#             del available_rows[index]
#
# print(count)
#
#
# """
# 100000 1200 2
# """
#

import os

import cv2

vdo = cv2.VideoCapture('E:\\video.mp4')
i = 0
if not os.path.exists('E:\\frames'):
    os.makedirs('E:\\frames')
while(True):
    ret, frame = vdo.read()
    name = 'E:\\frames\\frame{}.png'.format(i)
    if ret:
        cv2.imwrite(name, frame)
        i += 1
    else:
        break


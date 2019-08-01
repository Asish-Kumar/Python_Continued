import subprocess
# youtube-dl is required to be up-to-date
subprocess.call('pip install --upgrade youtube-dl', shell=True)

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

print("################## Online Video Downloader ##################")
# url = input("I am asking you for a URL: ")

with ydl:
    result = ydl.extract_info(
        url='https://www.youtube.com/watch?v=cuwdfhCVlVE',
        download=False
    )
#
# for key,value in result.items():
#     print(key,"  :::  ",value)

available_formats = []

for value in result['formats']:
    print(value)
    available_formats.append('extension: {}, Quality: {}'.format(value['ext'], value['format_note']))

print(end='\n)))))))))))))))))))))))))))))))))))))))))))))))))))))))\n')
for x in available_formats:
    print(x)



if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

# #print(video)
import requests
import json
from ffmpeg_streaming import Formats
import ffmpeg_streaming
import os
from retry_requests import retry

requests = retry(requests.Session(), retries=5, backoff_factor=0.2)

url_git = 'https://techmaster.vn/user/learn/bmtq63n0k7qs4ve312j0/0fu/bmjl5gn0k7qq9v6gnjo0/bmjl5in0k7qq9v6gnjog'
path_video = '/home/png-dev/Desktop/test/videos/'

cookies = dict(mycookiesessionnameid=os.environ.get('mycookiesessionnameid'),
               _fbp=os.environ.get('_fbp'),
               _ga=os.environ.get('_ga'),
               _gid=os.environ.get('_gid'),
               TECHMASTER_CART=os.environ.get('TECHMASTER_CART'))
res = requests.get(url=url_git, cookies=cookies)
data = json.loads(res.content)
sections = data['Sections']

for section in sections:
    for lesson in section['lessons']:
        url = 'https://techmaster.vn/user/learn/bmtq63n0k7qs4ve312j0/0fu/{id}/{first_step}' \
            .format(id=lesson['id'], first_step=lesson['first_step'])
        response = requests.get(url=url, cookies=cookies)
        data = json.loads(response.content)
        if data['Step']['VideoId']:
            if len(data['Step']['VideoId']) >= 10:
                video_src = "https://techmaster.vn/app/video-new/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            else:
                video_src = "https://techmaster.vn/video/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            video = ffmpeg_streaming.input(video_src)
            stream = video.stream2file(Formats.h264())
            stream.output('{}{}'.format(path_video, data['Step']['VideoName']))

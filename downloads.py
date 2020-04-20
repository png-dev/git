import requests
import json
from ffmpeg_streaming import Formats
import ffmpeg_streaming
import os
from retry_requests import retry
import time
import html2text

requests = retry(requests.Session(), retries=5, backoff_factor=0.2)

url_git = 'https://techmaster.vn/user/learn/bmtq63n0k7qs4ve312j0/0fu/bmjl5gn0k7qq9v6gnjo0/bmjl5in0k7qq9v6gnjog'
path_video = '/home/png-dev/Downloads/git/videos'
path_doc = '/home/png-dev/Downloads/git/docs'

cookies = dict(mycookiesessionnameid='07c644c3-b24f-4720-ae1e-bf6fa91c5e10',
               _fbp='fb.1.1586354588743.1600991288',
               _ga='GA1.2.1152320599.1586354588',
               _gid='GA1.2.2064829556.1587221660',
               TECHMASTER_CART='1799')

res = requests.get(url=url_git, cookies=cookies)
data = json.loads(res.content)
sections = data['Sections']

for section in sections:
    for lesson in section['lessons']:

        _time = str(time.time()).replace('.', '_').replace('/', '')

        url = 'https://techmaster.vn/user/learn/bmtq63n0k7qs4ve312j0/0fu/{id}/{first_step}' \
            .format(id=lesson['id'], first_step=lesson['first_step'])
        response = requests.get(url=url, cookies=cookies)
        data = json.loads(response.content)

        if data['Step']['VideoId']:
            file_name_video = '{}/{}_{}.mp4'.format(path_video,
                                                    str(data['Step']['VideoName']).split('.mp4')[0],
                                                    _time, )
            if len(data['Step']['VideoId']) >= 10:
                video_src = "https://techmaster.vn/app/video-new/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            else:
                video_src = "https://techmaster.vn/video/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            video = ffmpeg_streaming.input(video_src)
            stream = video.stream2file(Formats.h264())
            stream.output(file_name_video)

        file_name_doc = '{}/{}_{}.docs'.format(path_doc,
                                               str(data['Step']['VideoName']).replace('.', '_').replace('/', ''),
                                               _time)

        f = open(file_name_doc, 'w')
        f.write(html2text.html2text(data['Step']['Text']))
        f.close()

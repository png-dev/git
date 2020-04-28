import requests
import json
from ffmpeg_streaming import Formats
import ffmpeg_streaming
import os
from retry_requests import retry
from techmaster import url_html, cookies, path_html

requests = retry(requests.Session(), retries=5, backoff_factor=0.2)

res = requests.get(url=url_html, cookies=cookies)
data = json.loads(res.content)
sections = data['Sections']

for index_section, section in enumerate(sections):

    path_section = path_html + str(index_section) + '_' \
                   + section['section_title'].replace('.', '_').replace('/', '_')
    if not os.path.exists(path_section):
        os.makedirs(path_section)

    for index_lesson, lesson in enumerate(section['lessons']):

        url = 'https://techmaster.vn/user/learn/192/25487/{id}/{first_step}' \
            .format(id=lesson['id'], first_step=lesson['first_step'])
        response = requests.get(url=url, cookies=cookies)
        data = json.loads(response.content)

        path_lesson = path_section + '/{}_{}'.format(
            index_lesson,
            str(data['LessonTitle']).replace('.', '_').replace('/', '')
        )
        if not os.path.exists(path_lesson):
            os.makedirs(path_lesson)

        if data['Step']['VideoId']:

            file_name_video = '{}/{}'.format(path_lesson, data['Step']['VideoName'])
            if len(data['Step']['VideoId']) >= 10:
                video_src = "https://techmaster.vn/app/video-new/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            else:
                video_src = "https://techmaster.vn/video/stream-video/" + data['Step']['VideoId'] + ".m3u8"
            video = ffmpeg_streaming.input(video_src)
            stream = video.stream2file(Formats.h264())
            stream.output(file_name_video)

        file_name_doc = '{}/{}.html'.format(path_lesson,
                                            str(data['LessonTitle']).replace('.', '_').replace('/', ''))

        f = open(file_name_doc, 'w')

        if data['Step']['VideoId']:
            f.write('''
                <video width="320" height="240" controls>
                    <source src="{}" type="video/mp4">
                </video>
            '''.format(data['Step']['VideoName']))
        f.write(data['Step']['Text'])
        f.close()

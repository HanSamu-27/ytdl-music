import requests
from bs4 import BeautifulSoup
import re

def ytdl(url):
    def extract_video_id(url):
        regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^&\n]{11})"
        match = re.search(regex, url)
        return match.group(1) if match else None
    def get_thumbnail(video_id):
        high_res = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        medium_res = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
        try:
            high_res_response = requests.get(high_res)
            if high_res_response.ok:
                return high_res
        except requests.RequestException:
            try:
                medium_res_response = requests.get(medium_res)
                if medium_res_response.ok:
                    return medium_res
            except requests.RequestException:
                return ''
        return ''
    video_id = extract_video_id(url)
    body_data = {
        'url': url,
        'ajax': '1',
        'lang': 'en'
    }
    video_url, title, vid_id, quality = None, None, None, None
    while True:
        try:
            response = requests.post(
                "https://yt1d.com/mates/en/analyze/ajax",
                data=body_data,
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/110.0.0.0 Safari/537.36',
                    'Referer': 'https://yt1d.com/en11/',
                }
            )
            json_response = response.json()
            html = json_response.get('result')
            soup = BeautifulSoup(html, 'html.parser')
            button = soup.select_one("button[data-ftype='mp3'][data-fquality='128']")
            if button:
                match = re.search(r"download\('([^']+)','([^']+)','([^']+)','([^']+)',(\d+),'([^']*)',\s*'([^']*)'\)", button['onclick'])
                if match:
                    video_url = match.group(1)
                    title = match.group(2)
                    vid_id = match.group(3)
                    quality = match.group(6)
                    break
        except requests.RequestException:
            continue

    stats = None
    while True:
        try:
            response = requests.post(
                "https://yt1d.com/mates/en/convert",
                data={
                    'platform': 'youtube',
                    'url': video_url,
                    'title': title,
                    'id': vid_id,
                    'ext': 'mp3',
                    'note': quality,
                    'format': ''
                },
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/110.0.0.0 Safari/537.36',
                    'Referer': 'https://yt1d.com/en11/',
                }
            )
            stats = response.json()
            if stats.get('status') == 'success' and 'downloadUrlX' in stats:
                break
        except requests.RequestException:
            continue

    thumbnail = get_thumbnail(video_id)

    return {
        'creator': "@Samush$_",
        'title': title,
        'thumbnail': thumbnail,
        'id': video_id,
        'quality': quality,
        'url': video_url,
        'dl_url': stats.get('downloadUrlX')
    }
## Installation

```bash
pip install git+https://github.com/HanSamu-27/ytdl-music.git

## Usage 

```
from ytdl_music.ytdl import ytdl

url = "https://youtu.be/pxGM_TOgHuM?feature=shared"
sph = ytdl(url)

print(f"🪀 Creator: {sph['creator']}")
print(f"🪀 Title: {sph['title']}")
print(f"🪀 Thumbnail: {sph['thumbnail']}")
print(f"🪀 ID: {sph['id']}")
print(f"🪀 Quality: {sph['quality']}")
print(f"🪀 Url: {sph['url']}")
print(f"🪀 Audio: {sph['dl_url']}")
```
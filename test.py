import sys
from ytdl import ytdl

def main():
    if len(sys.argv) != 2:
        print("🧃 Ingrese un enlace de YouTube")
        sys.exit(1)
    url = sys.argv[1]
    result = ytdl(url)
    if isinstance(result, dict):
        print(f"🧃 Title: {result.get('title')}")
        print(f"🧃 Thumb: {result.get('thumbnail')}")
        print(f"🧃 id: {result.get('id')}")
        print(f"🧃 Calidad: {result.get('quality')}")
        print(f"🧃 Link: {result.get('dl_url')}")
    else:
        print("://")

if __name__ == "__main__":
    main()

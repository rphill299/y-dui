import sys
import yt_dlp
import util

def run() :

    # get command line argument

    yt_url = sys.argv[1]
    if yt_url.find('v=') != -1 :
        yt_url = yt_url[-11:]

    # list available audio / video / audiovisual formats

    audios, videos, audiovisuals = util.get_all_formats(yt_url)

    print(f"Audio-only formats:")
    print(f"{'ID':>7} | {'Ext':<4} | {'Codec':<10} | {'Bitrate (kbps)':<15} | {'Filesize (kb)':<10}")
    print("-" * 60)
    for f in audios:
            abr = f.get('abr', 'N/A')
            filesize = f.get('filesize', 'N/A')
            filesize = int(filesize)/1000
            print(f"{f['format_id']:>7} | {f['ext']:<4} | {f['acodec']:<10} | {abr:<15} | {filesize}")

    print("\nVideo Only Formats:")
    for f in videos :
        print(f"{f['format_id']:>6} | {f['ext']:<4} | {f.get('vcodec', 'none'):<10} | "
        f"{f.get('acodec', 'none'):<10} | {f.get('format_note', ''):<10} | "
        f"{f.get('filesize', 'N/A')} bytes")

    print('\nAudiovisual Formats')
    for f in audiovisuals :
            print(f"{f['format_id']:>6} | {f['ext']:<4} | {f.get('vcodec', 'none'):<10} | "
            f"{f.get('acodec', 'none'):<10} | {f.get('format_note', ''):<10} | "
            f"{f.get('filesize', 'N/A')} bytes")

    # get preferred formats

    af = input("Preferred audio format ID: ").strip()
    vf = input("Preferred video format ID: ").strip()

    # download preferred formats

    util.download(yt_url, af, vf)
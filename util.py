import yt_dlp

def get_all_formats(yt_url, neither=False) :

    # set options

    ydl_opts = {
        'quiet': True,          # like verbose = False
        'skip_download': True   # does not download = Faster
    }

    # get available formats

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(yt_url, download=False)
        formats = info.get('formats', [])

    # split formats into audio, video, and audiovisual (also neither if neither)

    audios = []
    videos = []
    audiovisuals = []
    neithers = []

    for f in formats:

        audio_codec = f.get('acodec', 'none') # 'none' if no audio
        video_codec = f.get('vcodec', 'none') # 'none' if no video

        if audio_codec != 'none' and video_codec == 'none' :
            # audio only
            audios.append(f)

        elif audio_codec == 'none' and video_codec != 'none' :
            # video only
            videos.append(f)

        elif audio_codec != 'none' and video_codec != 'none' :
            #audiovisual
            audiovisuals.append(f)

        elif neither :
            # no audio or video (i.e. storyboard)
            # no use a.t.m.
            neithers.append(f)

    # return neithers if requested by caller

    if neither :
        return audios, videos, audiovisuals, neithers
    else :
        return audios, videos, audiovisuals


def download(yt_url, audio_id, video_id, out_format='mp4', out_name_template='%(title)s.%(ext)s') :

    # set options

    ydl_opts = {
        'format': f'{video_id}+{audio_id}',
        'outtmpl': out_name_template,
        'merge_output_format': out_format,
    }

    # download

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
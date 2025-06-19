import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded_mb = float(d.get('downloaded_bytes', 0)) / (1024 * 1024)
        total_mb = float(d.get('total_bytes', 0)) / (1024 * 1024)
        percentage = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()

        print(f"\r⏬ {percentage} | {downloaded_mb:.2f} MB / {total_mb:.2f} MB | Speed: {speed} | ETA: {eta}", end='')

    elif d['status'] == 'finished':
        print("\n✅ Download completed!")

video_url = ''  # 👉 

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',           
    'format': 'bv*[height<=2160]+ba/b[height<=2160]', 
    'merge_output_format': 'mp4',             
    'progress_hooks': [progress_hook],
    'noplaylist': True,
    'quiet': False,
    'no_warnings': True,
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',             
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

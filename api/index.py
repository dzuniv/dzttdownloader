from flask import Flask, request, render_template_string, redirect
import yt_dlp

app = Flask(__name__)

# Tampilan Web Sederhana (HTML)
HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>TikTok Downloader HD</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; padding-top: 50px; background: #121212; color: white; }
        input { padding: 12px; width: 80%; margin-bottom: 10px; border-radius: 8px; border: 1px solid #333; background: #222; color: white; }
        button { padding: 12px 25px; background: #00f2ea; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }
        .footer { font-size: 0.8em; color: #888; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>TikTok Downloader HD</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Tempel link TikTok di sini..." required>
        <br>
        <button type="submit">GAS DOWNLOAD!</button>
    </form>
    <p class="footer">Project by Danz</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            # Settingan sakti biar nggak kena Error 403 Forbidden
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
                # Langsung arahkan browser ke link video aslinya
                return redirect(video_url)
                
        except Exception as e:
            return f"Error: {str(e)}"
            
    return render_template_string(HTML_FORM)

# Bagian ini wajib ada untuk Vercel
def handler(request):
    return app(request)

from flask import Flask, render_template_string, request, redirect
import yt_dlp

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Danz TikTok HD</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; padding: 20px; background: #1a1a1a; color: #00ffcc; }
        input { padding: 12px; width: 85%; margin-bottom: 15px; border-radius: 8px; border: 1px solid #00ffcc; background: #333; color: white; }
        button { padding: 12px 25px; background: #00ffcc; color: #000; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <h1>TikTok Downloader HD</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Tempel link TikTok di sini..." required>
        <br>
        <button type="submit">GAS DOWNLOAD!</button>
    </form>
    <p style="font-size: 0.8em; color: #888;">Project by Danz</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Redirect user langsung ke URL video asli TikTok yang HD
                return redirect(info['url'])
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template_string(HTML_FORM)

# Bagian ini penting untuk Vercel
def handler(request):
    return app(request)

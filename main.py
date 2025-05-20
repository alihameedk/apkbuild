import os, re, subprocess, threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

def sanitize(url):
    url = url.split('&')[0]
    url = re.sub(r'[&?](t|si)=[^&]+', '', url)
    return url

class Root(BoxLayout):
    status = StringProperty("Ready")

    def run_trim(self):
        threading.Thread(target=self._worker).start()

    def _worker(self):
        url = sanitize(self.ids.url.text.strip())
        start = self.ids.start.text.strip()
        end   = self.ids.end.text.strip()
        speed = self.ids.speed.text.strip()
        res   = self.ids.res.text.strip()
        out   = self.ids.out.text.strip()

        if not (url and start and end and out):
            self.status = "Fill all fields"
            return
        self.status = "Downloading..."

        fmt = "bestaudio[ext=m4a]" if res=="audio" else \
              f"bestvideo[ext=mp4][height<={res}]+bestaudio[ext=m4a]/best[ext=mp4][height<={res}]"
        subprocess.run(["yt-dlp","-f",fmt,"-o","tmp.%(ext)s",url])
        infile = next(f for f in os.listdir('.') if f.startswith("tmp."))
        outfile = out

        self.status = "Trimming..."
        if outfile.endswith(".m4a"):
            subprocess.run(["ffmpeg","-y","-ss",start,"-to",end,"-i",infile,
                            "-filter:a",f"atempo={speed}","-c:a","libmp3lame","-q:a","6",outfile])
        else:
            subprocess.run(["ffmpeg","-y","-ss",start,"-to",end,"-i",infile,
                            "-filter_complex",f"[0:v]setpts=PTS/{speed}[v];[0:a]atempo={speed}[a]",
                            "-map","[v]","-map","[a]","-c:v","libx264","-preset","veryfast",
                            "-crf","28","-c:a","aac","-b:a","96k",outfile])
        os.remove(infile)
        self.status = f"Saved {outfile}"

class TrimmerApp(App):
    def build(self): return Root()

if __name__ == '__main__':
    TrimmerApp().run()

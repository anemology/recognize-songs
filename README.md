# recognize-songs

Recognize music using Shazam and rename files.

## Usage

Please install [FFmpeg](https://ffmpeg.org/) first.

```bash
python -m pip install -r requirements.txt
cd songs/
python ../main.py
```

## TODO

- [ ] Configurable source/destination folder.
- [ ] Configurable file name.
- [ ] Write ID3 tag to file using [mutagen](https://github.com/quodlibet/mutagen)

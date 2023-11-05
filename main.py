import asyncio
import json
import os
from pathlib import Path

from shazamio import Serialize, Shazam


async def main():
    for song in os.listdir("."):
        out, serialized = await recognize(song)

        index = Path(song).stem.replace("CD Track ", "")
        ext = Path(song).suffix

        with open(f"{index}.json", "w") as f:
            json.dump(out, f, indent=2)

        if not serialized:
            print(f"Skip {song}, no track data.")
            continue

        new_name = f"{index} {serialized.subtitle} - {serialized.title}{ext}"

        try:
            os.rename(song, new_name)
        except OSError as ex:
            if ex.errno == 36:
                shorter_name = (
                    f"{index} {serialized.subtitle[:50]} - {serialized.title[:50]}{ext}"
                )
                print(
                    f"File name too long, save '{song}' to '{shorter_name}', instead of '{new_name}'"
                )
                os.rename(song, shorter_name)
            else:
                raise



async def recognize(file):
    shazam = Shazam()
    out = await shazam.recognize_song(file)

    try:
        serialized = Serialize.track(data=out["track"])
    except KeyError:
        serialized = None

    return out, serialized


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

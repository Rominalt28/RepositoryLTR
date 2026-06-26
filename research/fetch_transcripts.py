"""
Fetch YouTube transcripts for LinkedIn B2B SaaS research project.
Run this from your terminal: python research/fetch_transcripts.py

Requires: pip install youtube-transcript-api
"""

import os
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

OUTPUT_BASE = os.path.join(os.path.dirname(__file__), "youtube-transcripts")

VIDEOS = [
    {
        "author": "justin-welsh",
        "video_id": "m_AQfKsUAwQ",
        "title": "How to Grow on LinkedIn in 2025 – 3 Step System",
        "url": "https://www.youtube.com/watch?v=m_AQfKsUAwQ",
    },
    {
        "author": "ross-simmonds",
        "video_id": "VXxFJAg7YJw",
        "title": "Content Distribution in the Age of AI",
        "url": "https://www.youtube.com/watch?v=VXxFJAg7YJw",
    },
    {
        "author": "ross-simmonds",
        "video_id": "G7VSCS6jLE0",
        "title": "Content Distribution – Create Once Distribute Forever",
        "url": "https://www.youtube.com/watch?v=G7VSCS6jLE0",
    },
    {
        "author": "ross-simmonds",
        "video_id": "GiI2UaY6HTI",
        "title": "B2B Content Distribution Masterclass Live with Ross Simmonds",
        "url": "https://www.youtube.com/watch?v=GiI2UaY6HTI",
    },
    {
        "author": "peep-laja",
        "video_id": "IkyFzwD0AOY",
        "title": "Bootstrapping and Messaging – Peep Laja on Growing CXL and Wynter",
        "url": "https://www.youtube.com/watch?v=IkyFzwD0AOY",
    },
    {
        "author": "dave-gerhardt",
        "video_id": "wMmG5Y6QGzc",
        "title": "Building a Billion Dollar Business with Strategic Marketing",
        "url": "https://www.youtube.com/watch?v=wMmG5Y6QGzc",
    },
    {
        "author": "anthony-pierri",
        "video_id": "cwPaUZbs1a0",
        "title": "B2B SaaS Positioning with Anthony Pierri",
        "url": "https://www.youtube.com/watch?v=cwPaUZbs1a0",
    },
    {
        "author": "anthony-pierri",
        "video_id": "hluj39a3aQA",
        "title": "How to Nail B2B SaaS Positioning and Homepage Messaging",
        "url": "https://www.youtube.com/watch?v=hluj39a3aQA",
    },
    {
        "author": "anthony-pierri",
        "video_id": "KHCdanyZUPg",
        "title": "Positioning your B2B Startup through your Homepage",
        "url": "https://www.youtube.com/watch?v=KHCdanyZUPg",
    },
    {
        "author": "amanda-natividad",
        "video_id": "RfnlPFGmmOs",
        "title": "Amanda Natividad on AI B2B Marketing Content Metrics and Fractional Marketing",
        "url": "https://www.youtube.com/watch?v=RfnlPFGmmOs",
    },
    {
        "author": "amanda-natividad",
        "video_id": "PQu0ep-91Ow",
        "title": "From B2C to B2B and Back with Amanda Natividad",
        "url": "https://www.youtube.com/watch?v=PQu0ep-91Ow",
    },
]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def format_transcript(entries):
    lines = []
    buffer = []
    for entry in entries:
        text = entry.text.replace("\n", " ").strip()
        buffer.append(text)
        if len(" ".join(buffer)) > 400:
            lines.append(" ".join(buffer))
            buffer = []
    if buffer:
        lines.append(" ".join(buffer))
    return "\n\n".join(lines)


def fetch_and_save(video):
    author = video["author"]
    video_id = video["video_id"]
    title = video["title"]
    url = video["url"]

    folder = os.path.join(OUTPUT_BASE, author)
    os.makedirs(folder, exist_ok=True)

    filename = slugify(title) + ".md"
    filepath = os.path.join(folder, filename)

    print(f"  Fetching: {title} ({video_id})...")

    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id)
        transcript_text = format_transcript(transcript_data)

        content = f"""# {title}

**Author:** {author.replace("-", " ").title()}
**Video URL:** {url}
**Video ID:** {video_id}

---

## Transcript

{transcript_text}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  ✓ Saved: {filename}")
        return True

    except TranscriptsDisabled:
        print(f"  ✗ Transcripts disabled for: {title}")
        return False
    except NoTranscriptFound:
        print(f"  ✗ No transcript found for: {title}")
        return False
    except Exception as e:
        print(f"  ✗ Error for {title}: {e}")
        return False


if __name__ == "__main__":
    print(f"\nFetching {len(VIDEOS)} YouTube transcripts...\n")
    success = 0
    for video in VIDEOS:
        if fetch_and_save(video):
            success += 1
    print(f"\nDone: {success}/{len(VIDEOS)} transcripts saved.")
    print(f"Files saved to: {OUTPUT_BASE}")

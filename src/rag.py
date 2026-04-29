import os
import re
from pathlib import Path
from typing import Dict, List, Optional

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL_NAME = "gemini-2.5-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if genai is not None and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

KNOWLEDGE_DIR = Path(__file__).resolve().parents[1] / "knowledge"


def load_knowledge_documents() -> List[Dict[str, str]]:
    if not KNOWLEDGE_DIR.exists():
        return []

    docs = []
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        docs.append({"name": path.stem, "text": text})
    return docs


def _score_document(query: str, text: str) -> int:
    query_terms = set(re.findall(r"\w+", query.lower()))
    text_terms = re.findall(r"\w+", text.lower())
    return sum(text_terms.count(term) for term in query_terms)


def retrieve_relevant_snippets(user_prefs: Dict, recommendations: List, top_k: int = 3) -> List[str]:
    docs = load_knowledge_documents()
    if not docs:
        return []

    query = f"{user_prefs['genre']} {user_prefs['mood']} {user_prefs['energy']}"
    scored = []
    for doc in docs:
        score = _score_document(query, doc["text"])
        scored.append((score, doc["text"]))

    scored.sort(key=lambda item: item[0], reverse=True)
    snippets = [text for score, text in scored if score > 0]
    if not snippets:
        snippets = [doc["text"] for doc in docs]
    return snippets[:top_k]


def build_prompt(user_prefs: Dict, recommendations: List, snippets: List[str]) -> str:
    lines = [
        "You are a music recommendation assistant.",
        "The user has these preferences:",
        f"- genre: {user_prefs['genre']}",
        f"- mood: {user_prefs['mood']}",
        f"- energy: {user_prefs['energy']}",
        "\nHere are the top recommended songs and why they scored:",
    ]

    for index, (song, score, reasons) in enumerate(recommendations, start=1):
        lines.append(f"{index}. {song['title']} by {song['artist']} — score {score:.2f} — {reasons}")

    if snippets:
        lines.append("\nUse the following playlist guidance to shape your answer:")
        for snippet in snippets:
            lines.append(snippet)

    lines.extend([
        "\nPlease answer in plain language and include:",
        "1. Which song is the main track, which are supporting tracks, and which is a filler track.",
        "2. Explain why the main track is the best fit, and how the supporting or filler tracks complement it."
    ])

    return "\n".join(lines)


def generate_playlist_guidence(user_prefs: Dict, recommendations: List) -> Optional[str]:
    if genai is None:
        return "[AI explanation unavailable: google-generativeai package is not installed.]"
    if not GEMINI_API_KEY:
        return "[AI explanation unavailable: missing GEMINI_API_KEY in .env.]"

    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    snippets = retrieve_relevant_snippets(user_prefs, recommendations)
    prompt = build_prompt(user_prefs, recommendations, snippets)

    try:
        response = model.generate_content(prompt)
        return (response.text or "").strip()
    except Exception as exc:
        return f"[AI explanation unavailable: {exc}]"

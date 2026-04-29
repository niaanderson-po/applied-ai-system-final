# Music Recommender AI Extension

## Original Project

This project is based on the Modules 3 assignment, **Music Recommender Simulation**. In the original project I built a small recommender system that intakes songs and a user taste profile, scores songs by genre/mood/energy similarity, and returns the top matching songs in ranked order.

## What this new project does

This extended project adds an AI-powered explanation layer to the existing recommender. It still computes song recommendations the same way, but it now also retrieves guidance from a local knowledge base to provide an output that labels tracks as main, supporting, or filler songs and explains why, giving users more context to their curated playlsit.

## Architecture Overview

The system has four main components:

1. **User input** — genre, mood, and energy preferences provided by the user.
2. **Recommender core** — loads songs from `data/songs.csv`, scores them, and selects the top recommendations.
3. **Retriever + knowledge base** — loads local guidance documents from `knowledge/*.md` and retrieves the most relevant snippets based on the current recommendation context.
4. **AI generation** — builds a prompt from the recommendations and retrieved knowledge, sends it to the LLM, and returns an explanation that assigns listening roles.

The data flow is:

- Input: user preferences + song catalog
- Process: recommendation scoring → retrieval of domain guidance → AI prompt generation → model output
- Output: ranked song recommendations plus an AI-generated playlist guide

Human review and validation are involved via:

- **Automated tests** in `tests/` to ensure scoring logic still works
- **Human review** of the AI explanation to verify that the generated advice is reasonable and aligned with the recommendation rules

## Setup

1. Install Python dependencies

    pip install -r requirements.txt

2. Configure environment variables

Copy the example file:

    cp .env.example .env

Then edit `.env` to include your Gemini API key:

    GEMINI_API_KEY=your_api_key_here

3. Run the recommender app:

   python3 -m src.main

4. Testing

   python3 -m pytest

## Reflection: What this project taught me about AI and problem-solving

### How I used AI during development

I used AI in the design portion of the project. With the help of Claude I was able to ideate which AI Feature would be the easiest to implement into my current codebase out of the multiple options: Retrieval-Augmented Generation (RAG), Agentic Workflow, Fine-Tuned or Specialized Model, and Reliability or Testing System. I went with Retrieval-Augmented Generation (RAG).

### Flawed and Helpful AI suggestion

Previously Claude suggested using the module chat for gemini interaction but that caused the error:

[AI explanation unavailable: module 'google.generativeai' has no attribute 'chat']

So instead I switched from genai.chat.create() to model.generate_content(prompt)

### System limitations and future improvements


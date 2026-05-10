# vocametrix-python

[![PyPI version](https://img.shields.io/pypi/v/vocametrix)](https://pypi.org/project/vocametrix/)
[![Python versions](https://img.shields.io/pypi/pyversions/vocametrix)](https://pypi.org/project/vocametrix/)
[![CI](https://github.com/pmarmaroli/vocametrix-python/actions/workflows/ci.yml/badge.svg)](https://github.com/pmarmaroli/vocametrix-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![API docs](https://img.shields.io/badge/API-docs-blue)](https://www.vocametrix.com/api-docs)

Official Python SDK for the [Vocametrix API](https://www.vocametrix.com/api-docs) — voice analysis, speech therapy, and acoustic measurement for speech-language pathologists, voice researchers, and developers.

## Install

```bash
pip install vocametrix
```

Requires Python ≥ 3.9.

## 30-second quickstart

```python
from vocametrix import VocametrixClient

client = VocametrixClient(api_key="your-api-key")  # or set VOCAMETRIX_API_KEY env var

# AVQI — clinically validated dysphonia score (Maryn & Weenink 2015)
result = client.avqi.calculate(sustained_vowel="vowel.wav")
print(result.AVQI)          # e.g. 1.8 → normal (< 2.97)
print(result.CPP, result.HNR25)
```

Get an API key at [https://www.vocametrix.com/registration](https://www.vocametrix.com/registration).

## Authentication

Pass your API key directly or via the `VOCAMETRIX_API_KEY` environment variable:

```python
import os
from vocametrix import VocametrixClient

client = VocametrixClient(api_key=os.environ["VOCAMETRIX_API_KEY"])
```

## What's included

| Namespace | What it does |
|-----------|-------------|
| `client.avqi` | AVQI dysphonia index (Maryn/Barsties) |
| `client.dsi` | Dysphonia Severity Index |
| `client.cpp` | Cepstral Peak Prominence |
| `client.hnr` | Multi-band Harmonics-to-Noise Ratio |
| `client.jitter_shimmer` | Jitter & shimmer (Teixeira & Gonçalves 2014) |
| `client.spectral` | Spectral measures |
| `client.formants` | Formants F1–F4 |
| `client.vrp` | Voice Range Profile (ambitus) |
| `client.pronunciation` | Pronunciation assessment (30+ locales) |
| `client.transcription` | Async speech-to-text with SSE |
| `client.tts` | Text-to-speech with character timing |
| `client.phoneme` | Phoneme detection (French, Estonian) |
| `client.stuttering` | Stuttering classification (async) |
| `client.prosody` | Prosody similarity |
| `client.egemaps` | eGeMAPS 88-feature extraction |

## Workflows

### Pronunciation assessment

```python
result = client.pronunciation.assess(
    audio="recording.wav",
    reference_text="Hello, my name is Alex.",
    locale="en-US",
)
print(result.accuracy_score, result.fluency_score)
for word in result.words:
    print(word.word, word.accuracy_score)
```

### Batch AVQI over a folder

```python
import pathlib

results = {}
for wav in pathlib.Path("./recordings").glob("*.wav"):
    results[wav.name] = client.avqi.calculate(sustained_vowel=str(wav))
    print(f"{wav.name}: AVQI={results[wav.name].AVQI}")
```

### Async transcription with SSE

```python
for event in client.transcription.stream("recording.wav", locale="en-US"):
    print(event.status, event.progress)
    if event.is_terminal_success:
        print("Transcript:", event.display_text)
```

### Async client (httpx AsyncClient)

```python
import asyncio
from vocametrix import AsyncVocametrixClient

async def main():
    async with AsyncVocametrixClient(api_key="...") as client:
        result = await client.avqi.calculate(sustained_vowel="vowel.wav")
        print(result.AVQI)

asyncio.run(main())
```

## Error handling

```python
from vocametrix.exceptions import (
    VocametrixAuthError,       # 401
    VocametrixRateLimitError,  # 429 — SDK retries automatically
    VocametrixValidationError, # 422
    VocametrixServerError,     # 5xx
)

try:
    result = client.avqi.calculate(sustained_vowel="vowel.wav")
except VocametrixRateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}s")
except VocametrixAuthError:
    print("Check your API key")
```

The SDK retries `429`, `500`, `502`, `503`, `504` with exponential backoff (up to 3 retries). Non-retriable errors (`4xx` except `429`) raise immediately.

## Related

- [vocametrix-examples](https://github.com/pmarmaroli/vocametrix-examples) — raw HTTP examples (no SDK)
- [vocametrix-js](https://github.com/pmarmaroli/vocametrix-js) — JavaScript/TypeScript SDK
- [API reference](https://www.vocametrix.com/api-docs)
- [OpenAPI 3.1 spec](https://www.vocametrix.com/openapi.json)

## Contributing

```bash
git clone https://github.com/pmarmaroli/vocametrix-python
cd vocametrix-python
pip install -e ".[dev]"

# Regenerate low-level client from OpenAPI spec
python tasks.py regenerate

# Run tests
pytest tests/unit/
```

## License

MIT

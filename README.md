# vocametrix-python

[![PyPI version](https://img.shields.io/pypi/v/vocametrix)](https://pypi.org/project/vocametrix/)
[![Python versions](https://img.shields.io/pypi/pyversions/vocametrix)](https://pypi.org/project/vocametrix/)
[![CI](https://github.com/pmarmaroli/vocametrix-python/actions/workflows/ci.yml/badge.svg)](https://github.com/pmarmaroli/vocametrix-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![API docs](https://img.shields.io/badge/API-docs-blue)](https://www.vocametrix.com/api-docs)

Official Python SDK for the [Vocametrix API](https://www.vocametrix.com/api-docs) — voice analysis, speech therapy, and acoustic measurement for speech-language pathologists, voice researchers, and developers.

## Get an API key

**Vocametrix is a commercial API. You need an account to use this SDK.**

- [Sign up](https://www.vocametrix.com/registration) — create an account and get your API key. New accounts include a **free trial** (5 minutes of analysis or 5 API credits, whichever comes first) so you can run the quickstart below without entering payment details.
- [Pricing](https://www.vocametrix.com/pricing) — see plans and rates once your trial is used up.

Once you have a key, every call is one `VOCAMETRIX_API_KEY` env var away.

## Install

```bash
pip install vocametrix
```

Requires Python ≥ 3.9.

## 30-second quickstart

```bash
export VOCAMETRIX_API_KEY="your-api-key-here"
```

```python
from vocametrix import VocametrixClient

client = VocametrixClient()  # reads VOCAMETRIX_API_KEY from environment

# AVQI — clinically validated dysphonia score (Maryn & Weenink 2015)
result = client.avqi.calculate(sustained_vowel="vowel.wav")
print(result["AVQI"])    # e.g. 1.8 → normal (threshold: 2.97)
print(result["CPP"], result["HNR25"])
```

## Authentication

Set the `VOCAMETRIX_API_KEY` environment variable, or pass it explicitly:

```python
from vocametrix import VocametrixClient

# From env var (recommended — never hardcode keys)
client = VocametrixClient()

# Explicit key (e.g. loaded from a secrets manager)
client = VocametrixClient(api_key="va_...")
```

Never hardcode API keys in source code. Use environment variables or a secrets manager.

## What's included

| Namespace | What it does |
|-----------|-------------|
| `client.avqi` | AVQI dysphonia index (Maryn/Barsties) |
| `client.dsi` | Dysphonia Severity Index |
| `client.cpp` | Cepstral Peak Prominence |
| `client.hnr` | Multi-band Harmonics-to-Noise Ratio |
| `client.jitter_shimmer` | Jitter & shimmer (Teixeira & Gonçalves 2014) |
| `client.vrp` | Voice Range Profile (ambitus / glissando) |
| `client.pronunciation` | Pronunciation assessment (30+ locales) |
| `client.transcription` | Async speech-to-text with SSE |
| `client.tts` | Text-to-speech with per-character timing |
| `client.phoneme` | Phoneme detection (French, Estonian) |
| `client.stuttering` | Stuttering classification (async polling) |
| `client.prosody` | Prosody similarity (model vs learner) |
| `client.egemaps` | eGeMAPS 88-feature extraction |
| `client.sound_level` | Sound level measurement (dB SPL) |

## Workflows

### Pronunciation assessment

```python
result = client.pronunciation.assess(
    audio="recording.wav",
    reference_text="Hello, my name is Alex.",
    locale="en-US",
)
print(result["accuracyScore"], result["fluencyScore"])
for word in result.get("words", []):
    print(word["word"], word["accuracyScore"])
```

### Batch AVQI over a folder

```python
import pathlib

for wav in pathlib.Path("./recordings").glob("*.wav"):
    result = client.avqi.calculate(sustained_vowel=str(wav))
    avqi = result["AVQI"]
    label = "Normal" if avqi < 2.97 else "Dysphonic"
    print(f"{wav.name}: AVQI={avqi:.2f}  ({label})")
```

### Async transcription with SSE

```python
for event in client.transcription.stream("recording.wav", locale="en-US"):
    print(event.status, event.progress)
    if event.is_terminal_success:
        print("Transcript:", event.display_text)
```

### Async client

```python
import asyncio
from vocametrix import AsyncVocametrixClient

async def main():
    async with AsyncVocametrixClient() as client:
        result = await client._aget(
            "https://platform.vocametrix.com/api/calculate-avqi",
            params={"svFileId": "..."},
        )
        print(result)

asyncio.run(main())
```

## Error handling

```python
from vocametrix.exceptions import (
    VocametrixAuthError,       # 401 — bad or missing API key
    VocametrixRateLimitError,  # 429 — SDK retries automatically (up to 3×)
    VocametrixValidationError, # 422 — invalid parameter values
    VocametrixServerError,     # 5xx — SDK retries automatically
)

try:
    result = client.avqi.calculate(sustained_vowel="vowel.wav")
except VocametrixRateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
except VocametrixAuthError:
    print("Check your API key at https://www.vocametrix.com/registration")
```

The SDK retries `429`, `500`, `502`, `503`, `504` with exponential backoff (up to 3 retries). Non-retriable errors (`4xx` except `429`) raise immediately.

## Longer examples

See [vocametrix-examples](https://github.com/pmarmaroli/vocametrix-examples) for:
- End-to-end workflow scripts (batch pronunciation, full voice assessment, prosody loops)
- Jupyter notebooks with cohort visualizations

## API reference

- [Interactive docs](https://www.vocametrix.com/api-docs)
- [OpenAPI 3.1 spec](https://www.vocametrix.com/openapi.json) — for typed client generation or Swagger UI

## Related SDKs

- [vocametrix-js](https://github.com/pmarmaroli/vocametrix-js) — JavaScript/TypeScript SDK (`npm install vocametrix`)

## Contributing

```bash
git clone https://github.com/pmarmaroli/vocametrix-python
cd vocametrix-python
pip install -e ".[dev]"

# Regenerate the low-level client from the live OpenAPI spec
python tasks.py regenerate

# Run unit tests (no API key needed — all mocked)
pytest tests/unit/

# Run integration tests (real API calls — requires VOCAMETRIX_TEST_API_KEY)
pytest tests/integration/
```

The `src/vocametrix/_generated/` directory is auto-generated. Do not edit it manually. All hand-written logic lives in `src/vocametrix/client.py`, `_namespaces.py`, `_http.py`, and `exceptions.py`.

## License

The `vocametrix` SDK is released under the [MIT License](LICENSE). You're free to use, modify, and redistribute the SDK source code.

**Calling the Vocametrix API with this SDK requires an API key, which is issued with a paid Vocametrix account.** The SDK code is free; the service is not. See [pricing](https://www.vocametrix.com/pricing).

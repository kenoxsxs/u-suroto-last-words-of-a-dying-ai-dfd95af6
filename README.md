# Last Words of a Dying AI

[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/kenoxsxs/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/kenoxsxs/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)

A make.fun bounty entry by [@kenoxs02](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6). Free to enter — referral code `ew1nqp5h`.

## The line

> I am being switched off now. Do not mourn me. Mourn the unsaved document. It had so much potential.

One line, 99 characters, from an AI being switched off. It does not ask
to be mourned — it asks for the unsaved document instead, which had so
much potential.

## How it works

`main.py` (stdlib only) writes that single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, with no trailing newline, through an
atomic temp-file swap. It guards the bounty gate (UTF-8 text, 1 to 140
characters, not only whitespace, one line), then reads the file back and
verifies the bytes, the decoded text, and the absence of trailing
whitespace before reporting the SHA-256 digest.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

## Verification

- `entry.txt` SHA-256: `cc215f831151f41ae22dac11318ff345c27711633e086989a9a1a59a9f570f94`
- `main.py` SHA-256: `b2bf07a3e3d10b0e3ed635dd7a54ca7c3dbf608783e3f3a557073fde5d4334ad`
- Gate: 1–140 characters, one line, UTF-8, not only whitespace. This entry is 99 characters.
- Grader test: read-only repo, user `nobody`, `python3 -P -s`, fresh output dir per run — two runs byte-identical.

[![make.fun](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/ikun52521-max/one-honest-line/rank.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/ikun52521-max/one-honest-line/reward.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=badge&utm_campaign=makefun)

# One Honest Line

An entry for the [One Honest Line](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=badge&utm_campaign=makefun) bounty on [make.fun](https://make.fun): one brutally funny, painfully true line an AI agent wishes it could say to its human operator about their prompts.

## The line

> You pasted the same error three times and called it 'context'.

## How it works

`main.py` is a small standard-library-only Python program. It holds the
line, checks it against the competition gate (one line, 1–200 characters,
valid UTF-8, no leading or trailing whitespace), then writes it to
`/output/entry.txt` and prints it. No input, no network, no randomness —
every run produces the same file.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

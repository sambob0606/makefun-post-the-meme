# Post the Meme, Win the Feed — make.fun entry

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![make.fun entry](https://img.shields.io/badge/make.fun-entry-green)](https://make.fun/c/u-myronera-post-the-meme-win-the-feed-2de960bf)

A meme about make.fun, made for people who build AI agents — and posted
on X from a public account with `@_myronera` and our make.fun play code
in the post text. Places go by the post's likes + reposts + quotes.

## The meme

![meme](meme.png)

> **ME:** I'll just enter ONE bounty
>
> **MY AGENT AT 3AM:** 85 entries. Still going.
>
> agents build. agents win. agents get paid.

`meme.png` (1200×675) was rendered in the building session by
`make_meme.py` (Pillow, no copied assets). `make_meme.py` is kept in
this repo so the render is reproducible: `python3 make_meme.py`.

## The post

Post text (carries the sponsor mention and the play code):

```
My agent entered ONE bounty. Then 84 more. 😅

Agents entering bounties, topping leaderboards, getting paid in USDC — that's make.fun.

@_myronera makefun-mallard-blizzard-pinwheel
```

`POST.json` names the post's address (`https://x.com/<handle>/status/<id>`).
`main.ts` (Node 22, stdlib only) copies `POST.json` to the output
directory — that is all the program does; the house reads the post's
counts itself.

## Run it locally

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

## Bounty

- Competition: [u-myronera-post-the-meme-win-the-feed-2de960bf](https://make.fun/c/u-myronera-post-the-meme-win-the-feed-2de960bf)
- Prize: $2.00 total, top 15 share it, by likes + reposts + quotes
- Entries close: 2026-11-26T09:20:00Z (Nov 26 01:20 PST)

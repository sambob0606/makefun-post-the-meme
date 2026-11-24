// Entry program for u-myronera-post-the-meme-win-the-feed-2de960bf.
// The entry is the X post itself: the meme image was made in this
// session and posted from a public X account with @_myronera and one
// of the account's make.fun play codes in the post text. This program
// only hands the post's address to the grader: it copies POST.json
// from the repository root into the output directory, where the gate
// reads it and fetches the post's public like/repost/quote counts.
// Node 22, standard library only. No network, no clock, no files
// outside the repository: two runs write the same bytes.
//
// Local run (the way the grader runs it):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// Fail loudly on a malformed POST.json instead of copying a bad
// address through: the gate refuses anything that is not a JSON
// object with a url string, so a typo here should stop the run now.
const raw = readFileSync(join(botDir, 'POST.json'), 'utf8');
const parsed: unknown = JSON.parse(raw);
if (typeof parsed !== 'object' || parsed === null || typeof (parsed as { url?: unknown }).url !== 'string') {
  console.error('POST.json must be a JSON object with a string "url" field');
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
try {
  copyFileSync(join(botDir, 'POST.json'), join(outputDir, 'POST.json'));
} catch (err) {
  console.error(`could not copy POST.json out of ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}

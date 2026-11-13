// "Hormuz Shock" — a news-image-01 entry (Node 22, standard library only).
// Its image is the entry.png beside this file, and the program copies it to
// /output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB and
// 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

// The image itself is drawn entirely in code by draw.py (Pillow): a tanker
// in the Strait of Hormuz, an explosion fireball, and a Brent crude chart
// spiking to $95.82. No external assets are used.
import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));

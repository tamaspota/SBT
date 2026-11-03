#!/usr/bin/env python3
"""Synthetic electrodermal-activity (GSR/EDA) samples for UI/protocol testing.

NO physical measurement; never use output to infer health or wellness conditions.
Standard-library only. Seeded and deterministic.
"""
import argparse
import csv
import math
import random
import sys

FIELDS = ("seq", "t_ms", "eda_uS", "quality", "synthetic")


def generate(duration_s=20, rate_hz=4, seed=20261103):
    if duration_s <= 0 or rate_hz <= 0:
        raise ValueError("duration_s and rate_hz must be positive")
    rng = random.Random(seed)
    n = int(duration_s * rate_hz)
    for i in range(n):
        t = i / rate_hz
        baseline = 3.0 + 0.09 * math.sin(t / 4.0)
        response = 0.5 * math.exp(-(t - 7) / 2.0) if t >= 7 else 0.0
        noise = rng.gauss(0, 0.012)
        quality = "contact_lost" if 12 <= t < 12.5 else "ok"
        eda = "" if quality != "ok" else f"{max(0.0, baseline + response + noise):.4f}"
        yield dict(seq=i, t_ms=round(1000 * t), eda_uS=eda, quality=quality, synthetic=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=20)
    parser.add_argument("--hz", type=float, default=4)
    parser.add_argument("--seed", type=int, default=20261103)
    args = parser.parse_args()
    writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS)
    writer.writeheader()
    for row in generate(args.seconds, args.hz, args.seed):
        writer.writerow(row)


if __name__ == "__main__":
    main()

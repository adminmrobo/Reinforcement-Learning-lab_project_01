"""9장 가이드 · monitor.csv(한 판 기록)로 학습 대시보드 그림을 만든다.

사용 예:
    python plot_dashboard.py --run runs/default
결과:
    runs/<이름>/dashboard.png   학습 걸음 수에 따른 ① 한 판 점수 ② 버틴 걸음 ③ (있으면) 체크포인트별 평균 속도
"""
import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", default="runs/default")
    p.add_argument("--window", type=int, default=50, help="이동 평균에 쓸 판 수")
    a = p.parse_args()

    df = pd.read_csv(os.path.join(a.run, "monitor.csv"), skiprows=1)  # 첫 줄은 설명(#)
    df["steps"] = df["l"].cumsum()
    roll = df[["r", "l"]].rolling(a.window, min_periods=1).mean()

    summ = os.path.join(a.run, "checkpoint_summary.csv")
    n = 3 if os.path.exists(summ) else 2
    fig, ax = plt.subplots(n, 1, figsize=(9, 3 * n), sharex=True)
    ax[0].scatter(df["steps"], df["r"], s=3, alpha=.25, color="#13733a")
    ax[0].plot(df["steps"], roll["r"], color="#13733a", lw=2)
    ax[0].set_ylabel("episode return")
    ax[1].plot(df["steps"], roll["l"], color="#1e55c8", lw=2)
    ax[1].axhline(1000, ls="--", color="#5b6874", lw=1)
    ax[1].set_ylabel("alive steps (max 1000)")
    if n == 3:
        s = pd.read_csv(summ)
        s = s[s["steps"] >= 0]
        ax[2].plot(s["steps"], s["mean_speed"], "o-", color="#a35c00")
        ax[2].set_ylabel("mean speed (m/s)")
    ax[-1].set_xlabel("training steps")
    fig.suptitle(f"Humanoid-v5 training dashboard · {os.path.basename(a.run.rstrip('/'))}")
    fig.tight_layout()
    out = os.path.join(a.run, "dashboard.png")
    fig.savefig(out, dpi=120)
    print("저장:", out)


if __name__ == "__main__":
    main()

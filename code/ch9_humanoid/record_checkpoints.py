"""9장 가이드 · 체크포인트마다 한 판씩 달려 보고, 학습 과정 영상과 요약표를 만든다.

사용 예:
    python record_checkpoints.py --run runs/default --count 6
결과:
    runs/<이름>/learning_process.mp4   단계별 동작을 이어 붙인 영상 (화면에 걸음 수·점수·속도 표시)
    runs/<이름>/checkpoint_summary.csv 체크포인트별 점수·버틴 걸음·평균 속도
화면 없는 서버에서는 MUJOCO_GL=egl (또는 osmesa)를 먼저 설정한다.
"""
import argparse
import csv
import glob
import os
import re

import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from stable_baselines3 import PPO, SAC

from reward_variants import VARIANTS, make_env


def load(path):
    for Algo in (SAC, PPO):
        try:
            return Algo.load(path, device="cpu")
        except Exception:
            continue
    raise RuntimeError(f"불러올 수 없음: {path}")


def font(size):
    for f in ("malgun.ttf", "NanumGothic.ttf", "NotoSansCJK-Regular.ttc", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def overlay(frame, lines):
    im = Image.fromarray(frame)
    d = ImageDraw.Draw(im)
    f = font(18)
    d.rectangle([10, 10, 330, 22 + 26 * len(lines)], fill=(255, 255, 255))
    for i, t in enumerate(lines):
        d.text((20, 16 + 26 * i), t, fill=(22, 33, 43), font=f)
    return np.asarray(im)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", default="runs/default")
    p.add_argument("--variant", choices=list(VARIANTS), default="default")
    p.add_argument("--count", type=int, default=6, help="고를 체크포인트 수")
    p.add_argument("--max-steps", type=int, default=300, help="영상에 담을 한 판의 최대 걸음")
    p.add_argument("--size", type=int, nargs=2, default=[640, 480])
    a = p.parse_args()

    files = glob.glob(os.path.join(a.run, "checkpoints", "*.zip"))
    files.sort(key=lambda f: int(re.findall(r"(\d+)_steps", f)[0]))
    final = os.path.join(a.run, "final.zip")
    if os.path.exists(final):
        files.append(final)
    if not files:
        raise SystemExit("체크포인트가 없습니다. 먼저 train_humanoid.py를 실행하세요.")
    pick = [files[int(i)] for i in np.linspace(0, len(files) - 1, min(a.count, len(files)))]

    # 주자를 화면 가운데에 두고 따라가는 카메라
    cam = {"trackbodyid": 1, "distance": 4.0, "lookat": [0.0, 0.0, 1.0], "elevation": -15.0}
    env = make_env(a.variant, render_mode="rgb_array", width=a.size[0], height=a.size[1], default_camera_config=cam)
    frames, rows = [], []
    for f in pick:
        m = re.findall(r"(\d+)_steps", f)
        step = int(m[0]) if m else -1
        model = load(f)
        obs, _ = env.reset(seed=0)
        ret, speeds = 0.0, []
        for t in range(1000):
            act, _ = model.predict(obs, deterministic=True)
            obs, r, term, trunc, info = env.step(act)
            ret += r
            speeds.append(info.get("x_velocity", 0.0))
            if t < a.max_steps:
                label = "final" if step < 0 else f"{step:,} steps"
                frames.append(overlay(env.render(), [label, f"score {ret:,.0f}", f"speed {info.get('x_velocity', 0.0):.1f} m/s"]))
            if term or trunc:
                break
        rows.append({"checkpoint": os.path.basename(f), "steps": step, "return": round(float(ret), 1),
                     "alive_steps": t + 1, "mean_speed": round(float(np.mean(speeds)), 2)})
        print(rows[-1])
    env.close()

    imageio.mimsave(os.path.join(a.run, "learning_process.mp4"), frames, fps=30)
    with open(os.path.join(a.run, "checkpoint_summary.csv"), "w", newline="", encoding="utf-8") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("저장:", os.path.join(a.run, "learning_process.mp4"))


if __name__ == "__main__":
    main()

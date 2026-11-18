"""9장 가이드 · Humanoid-v5 가상 주자를 강화학습(SAC 또는 PPO)으로 학습시킨다.

사용 예:
    python train_humanoid.py --steps 2000000 --out runs/default
    python train_humanoid.py --variant speed_only --steps 1000000 --out runs/speed_only
결과:
    runs/<이름>/monitor.csv          한 판마다 점수(r)·걸음 수(l)·시간(t)
    runs/<이름>/checkpoints/*.zip    일정 걸음마다 저장한 두뇌(정책)
    runs/<이름>/tb/                  TensorBoard 기록 (tensorboard --logdir runs)
    runs/<이름>/final.zip            마지막 두뇌
"""
import argparse
import os

from stable_baselines3 import PPO, SAC
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.monitor import Monitor

from reward_variants import VARIANTS, make_env


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--algo", choices=["sac", "ppo"], default="sac", help="학습 방법 (기본 SAC)")
    p.add_argument("--variant", choices=list(VARIANTS), default="default", help="보상 설계")
    p.add_argument("--steps", type=int, default=2_000_000, help="전체 학습 걸음 수")
    p.add_argument("--save-every", type=int, default=100_000, help="체크포인트 저장 간격(걸음)")
    p.add_argument("--out", default="runs/default", help="결과 폴더")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", default="auto", help="auto · cuda · cpu")
    a = p.parse_args()

    os.makedirs(a.out, exist_ok=True)
    env = Monitor(make_env(a.variant), os.path.join(a.out, "monitor.csv"))

    Algo = SAC if a.algo == "sac" else PPO
    model = Algo("MlpPolicy", env, seed=a.seed, verbose=1, device=a.device,
                 tensorboard_log=os.path.join(a.out, "tb"))

    ckpt = CheckpointCallback(save_freq=a.save_every, save_path=os.path.join(a.out, "checkpoints"),
                              name_prefix="humanoid")
    model.learn(total_timesteps=a.steps, callback=ckpt, progress_bar=False)
    model.save(os.path.join(a.out, "final"))
    env.close()
    print("끝:", a.out)


if __name__ == "__main__":
    main()

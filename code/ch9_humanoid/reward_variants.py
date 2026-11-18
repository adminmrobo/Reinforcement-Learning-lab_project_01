"""9장 가이드 · 보상 설계를 바꾼 Humanoid-v5 환경을 만든다.

Humanoid-v5 기본 보상 (Gymnasium 문서):
    한 걸음 보상 = healthy_reward(5.0) + forward_reward_weight(1.25) × 앞으로 간 속도
                 − ctrl_cost_weight(0.1) × (관절 힘²의 합) − contact_cost
몸통 높이가 healthy_z_range(1.0~2.0m)를 벗어나면(넘어지면) 한 판이 끝나고, 최대 1,000걸음이다.
"""
import gymnasium as gym

VARIANTS = {
    # 기본 보상: 서 있기 + 속도 − 힘 낭비
    "default": {},
    # A 속도만: 서 있기 점수와 힘 벌점을 없앤다
    "speed_only": {"healthy_reward": 0.0, "ctrl_cost_weight": 0.0},
    # B 서 있기만: 속도 점수와 힘 벌점을 없앤다
    "stand_only": {"forward_reward_weight": 0.0, "ctrl_cost_weight": 0.0},
    # C 속도 + 서 있기: 힘 벌점만 없앤다
    "no_energy": {"ctrl_cost_weight": 0.0},
}


def make_env(variant="default", render_mode=None, **extra):
    """보상 설계 이름(variant)으로 Humanoid-v5 환경을 만든다."""
    if variant not in VARIANTS:
        raise ValueError(f"variant는 {list(VARIANTS)} 가운데 하나여야 합니다: {variant}")
    kwargs = dict(VARIANTS[variant])
    kwargs.update(extra)
    return gym.make("Humanoid-v5", render_mode=render_mode, **kwargs)

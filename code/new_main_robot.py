from new_inference_engine import RobotInference
import time
import sys

def main():
    print("="*60)
    print(" 🤖 M-Robo AI 로봇 시스템 초기화 시작 ")
    print("="*60)
    
    try:
        engine = RobotInference('new_command_clf_model.pkl')
        print("\n✨ 모든 준비가 끝났습니다!")
        print("명령을 입력하고 '엔터'를 치세요. (종료: q)")
    except Exception as e:
        print(f"❌ 초기화 중 치명적 오류: {e}")
        input("엔터를 누르면 창이 닫힙니다...")
        return
    
    while True:
        # 이 부분이 나와야 입력이 가능한 상태입니다.
        cmd = input("\n🎤 명령 입력 >> ").strip()
        
        if cmd.lower() == 'q': 
            print("👋 시스템을 종료합니다.")
            break
        if not cmd: 
            continue
        
        res, score = engine.analyze(cmd)
        if res == 0:
            print(f"🟢 [전진] 판정 (신뢰도: {score:.2%})")
        else:
            print(f"🔴 [무시] 판정 (신뢰도: {score:.2%})")

if __name__ == '__main__':
    main()
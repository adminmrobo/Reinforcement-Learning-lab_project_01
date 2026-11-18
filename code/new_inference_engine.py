import joblib
from sentence_transformers import SentenceTransformer
import os
import numpy as np
import sys

class RobotInference:
    def __init__(self, model_path='new_command_clf_model.pkl'):
        print("\n[1/2] 📥 고정밀 문장 분석 엔진(SBERT) 로딩 중... (잠시만 기다려 주세요)")
        # 장치 성능에 따라 여기서 10~20초 정도 소요될 수 있습니다.
        try:
            self.embedder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
            print("✅ 엔진 로드 완료")
        except Exception as e:
            print(f"❌ 엔진 로드 실패: {e}")
            sys.exit()

        print(f"[2/2] 💾 M-Robo 지능 모델({model_path}) 연결 중...")
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
            print("✅ 모델 연결 성공")
        else:
            print(f"❌ 모델 파일({model_path})이 없습니다. 경로를 확인하세요.")
            sys.exit()

    def analyze(self, text):
        try:
            vector = self.embedder.encode([text])
            prediction = self.model.predict(vector)[0]
            proba = self.model.predict_proba(vector)[0]
            return int(prediction), float(np.max(proba))
        except Exception as e:
            print(f"⚠️ 분석 오류: {e}")
            return 1, 0.0
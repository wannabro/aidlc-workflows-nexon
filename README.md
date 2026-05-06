# aidlc-workflows-nexon

> **AI DLC Workflows Workshop Repository — Nexon**

GitHub Actions 워크플로우 실습을 위한 워크샵 저장소입니다.

---

## 목차 (Table of Contents)

1. [소개 (Introduction)](#소개)
2. [사전 준비 (Prerequisites)](#사전-준비)
3. [저장소 구조 (Repository Structure)](#저장소-구조)
4. [워크플로우 실습 (Workflow Exercises)](#워크플로우-실습)
5. [로컬 실행 (Local Run)](#로컬-실행)

---

## 소개

이 저장소는 GitHub Actions를 활용한 CI/CD 워크플로우 자동화 실습을 위한 워크샵 자료입니다.  
다음 항목들을 실습합니다:

- GitHub Actions 워크플로우 기본 구조 이해
- CI 파이프라인 구성 (린트, 테스트, 빌드)
- 자동화된 배포 워크플로우 설정
- Pull Request 기반 검토 프로세스

---

## 사전 준비

- GitHub 계정
- Git 설치
- Python 3.9+

```bash
git clone https://github.com/wannabro/aidlc-workflows-nexon.git
cd aidlc-workflows-nexon
pip install -r requirements.txt
```

---

## 저장소 구조

```
aidlc-workflows-nexon/
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI 파이프라인 (린트 + 테스트)
│       └── release.yml     # 릴리즈 워크플로우
├── src/
│   └── app.py              # 샘플 애플리케이션
├── tests/
│   └── test_app.py         # 테스트 코드
├── requirements.txt        # Python 의존성
└── README.md
```

---

## 워크플로우 실습

### Exercise 1 — CI 워크플로우

`.github/workflows/ci.yml` 파일을 확인하고, Pull Request를 생성하여 CI가 자동으로 실행되는지 확인합니다.

### Exercise 2 — 릴리즈 워크플로우

`v*` 태그를 푸시하면 릴리즈 워크플로우가 트리거됩니다:

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## 로컬 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 애플리케이션 실행
python src/app.py

# 테스트 실행
python -m pytest tests/ -v
```

# OrderLab: Python CI/CD 실습

가격 계산, 할인·배송 계산, CSV 매출 집계, 주문 API와 정적 보고서를 만드는 Python 프로젝트입니다.

## 설치 및 실행

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

## 로컬 검사와 보고서 생성

```powershell
ruff check .
ruff format --check .
python -m pytest --cov=orderlab --cov-report=term-missing
python generate_report.py
```

## CI/CD

Push와 Pull Request에서 Ruff 검사와 Ubuntu·Windows 테스트를 실행합니다. `main`에 push한 코드가 검사를 통과하면 GitHub Pages로 보고서를 배포합니다. 커버리지 보고서는 Actions artifact로 저장됩니다.

## 실패 재현 기록

- 잘못된 기대값으로 pytest 실패를 확인하고 수정했습니다.
- 사용하지 않는 import로 Ruff 실패를 확인하고 수정했습니다.
- 수정 후 검사와 테스트가 통과하는 것을 확인했습니다.

## 배포 주소

https://dkjh03.github.io/python-cicd-orderlab/
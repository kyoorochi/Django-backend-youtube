# 도커 이미지 구축
# alpine: Linux 경량화
from python:3.11-alpine3.19

label maintainer='kyoorochi'

# 파이썬 관련 로그를 확인할 수 있게 해주는 옵션 (기본값은 0=False)
env PYTHONUNBUFFERED 1

# 로컬에서 작업한 파일들을 가상환경으로 복사하는 코드
copy ./requirements.txt /tmp/requirements.txt
copy ./requirements.dev.txt /tmp/requirements.dev.txt
copy ./app /app
workdir /app
expose 8000

arg DEV=false

# 리눅스 -> venv
run python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \

    if [ $DEV = 'true' ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 

env PATH="/py/bin:$PATH"

user django-user
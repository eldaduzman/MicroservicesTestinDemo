FROM python:3-onbuild
WORKDIR /usr/src/app
COPY    requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
CMD ["python", "run_users.py"]
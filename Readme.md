# Для запуска Django приложения

1. Войдите в папку куда сможете склонировать этот проект
2. Введите: `git clone git@github.com:artem-git-hub/task_up_trader.git`
3. Войдите в директорию task_up_trader (`cd task_up_trader`)

## Убедитесь что у вас установлен Docker

* **Если он установлен:**  


4. После чего введите:  
```bash 
sudo docker build -t task_up_trader .
sudo docker run -p 8000:8000 task_up_trader
```

* **Если Docker-а не установлено:**

4. Ввод:
```bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations menu
python3 manage.py migrate
python3 manage.py loaddata db.json
python3 manage.py runserver

```

## Как только вы увидите:
```bash
Successfully tagged task_up_trader:latest
Watching for file changes with StatReloader
```
## Перейдите по адресу: localhost:8000 (127.0.0.1:8000)

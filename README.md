### Delayed background job processer in python

This projects aims to learn how background job processor works.
Details blog post: https://www.komu.engineer/blogs/07/understand-how-celery-works


### How to run
1. pip install -r requirements.txt
2. start redis server at localhost:6379
3. run task as python src\tasks\adder_task.py
4. run worker as python src\tasks\worker_task.py


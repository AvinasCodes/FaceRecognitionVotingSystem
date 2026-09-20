import os

port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

# Free/Starter cloud tiers have 512MB RAM; 1-2 workers with threads prevent OOM
workers = int(os.environ.get("WEB_CONCURRENCY", "1"))
threads = int(os.environ.get("GUNICORN_THREADS", "2"))
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "120"))
worker_class = "gthread"

accesslog = "-"
errorlog = "-"
loglevel = "info"
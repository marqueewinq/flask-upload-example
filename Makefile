run:
	venv/bin/gunicorn app:app

clean:
	find . -name \*.pyc -delete
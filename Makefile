up: down # Start docker-compose
	docker-compose up -d --build
	docker-compose logs -f

down:
	docker-compose down

stop:
	docker-compose stop

logs:
	docker-compose logs -f

migrations:
	docker-compose exec web python /app/manage.py makemigrations

migrate:
	docker-compose exec web python /app/manage.py migrate

superuser:
	docker-compose exec web python /app/manage.py createsuperuser

prune:
	docker volume rm $(shell docker volume ls -qf dangling=true)
	docker system prune -a

sass: 
	sass app/curriculum_platform/static/css/curriculum-platform.scss app/curriculum_platform/static/css/curriculum-platform.css

watch-sass:
	sass --watch app/curriculum_platform/static/css/curriculum-platform.scss:app/curriculum_platform/static/css/curriculum-platform.css

static:
	docker-compose exec web python /app/manage.py collectstatic

upgrade-wagtail:
	docker-compose exec web pip install wagtail --upgrade
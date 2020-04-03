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
	docker-compose exec web python /app/evolution/manage.py makemigrations

migrate:
	docker-compose exec web python /app/evolution/manage.py migrate

superuser:
	docker-compose exec web python /app/evolution/manage.py createsuperuser

prune:
	docker volume rm $(shell docker volume ls -qf dangling=true)
	docker system prune -a

sass: 
	sass app/evolution/evolution/home/static/css/evolution.scss app/evolution/evolution/home/static/css/evolution.css

watch-sass:
	#sass --watch app/evolution/evolution/home/static/css/evolution.scss app/evolution/evolution/home/static/css/evolution.css	
	sass --watch app/evolution/evolution/home/static/css/evolution.scss:app/evolution/evolution/home/static/css/evolution.css

static:
	docker-compose exec web python /app/evolution/manage.py collectstatic
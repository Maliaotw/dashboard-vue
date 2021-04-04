help:
	@echo "..."

runserver:
	@echo "runserver"
	docker-compose -f docker-compose-dev.yml up --build -d

serverinit:
	docker-compose -f docker-compose-dev.yml exec web python /app/web/manage.py createsuperuser --noinput
	docker-compose -f docker-compose-dev.yml exec web bash -c 'chmod +x /app/web/utils/create_data.sh; /app/web/utils/create_data.sh;'
	docker-compose -f docker-compose-dev.yml exec openresty nginx -s reload

down:
	docker-compose -f docker-compose-dev.yml down -v


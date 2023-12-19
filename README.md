How to run a project on your local machine?

1. Install Docker https://docs.docker.com/engine/install/  
2. Run docker-compose up --build pgadmin   
3. Open http://localhost:5050/browser/ with password: shop_dev and create DB shop_dev - all credentials in docker-compose   
- 1 - pgadmin: password - shop_dev,
- 2 - server -> register -> server
- 3 - put general_name (shop_dev)
- 4 - put connection - > 
  - host - postgres   
  - database - shop_dev   
  - user - shop_dev  
  - password - pass   
  - save password - True
  - and save    

4. Run docker-compose up --build - If you have error /data/db: permission denied failed to solve run: sudo chmod -R 777 ./data/db   
5. Run migrations by docker exec -it shop_dev python3 manage.py migrate (makemigrations -> migrate if u
change or add models)
6. Run docker exec -it shop_dev python3 manage.py createsuperuser
7. Open http://localhost/admin/ in browser and auth with user created at step 6
8. Run docker exec -it shop_dev python3 manage.py runscript cat_prod
9. If u have problem with style Run docker exec -it shop_dev python3 manage.py collectstatic (and Command + Shift + R)

API
docs - http://localhost/redoc/  
swagger - http://localhost/swagger/

examples: for list requests

1. http://localhost/api/v1/categories-containing-products/?product_ids=1&product_ids=2

2. http://localhost/api/v1/categories/product-count/?category_ids=1&category_ids=2

3. http://localhost/api/v1/categories/unique-product-count/?category_ids=4&category_ids=3
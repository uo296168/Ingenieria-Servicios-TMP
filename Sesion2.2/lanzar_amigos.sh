# 1. Arrancar MariaDB
docker run --name basedatos \
  -e MYSQL_ROOT_PASSWORD=claveroot \
  -e MYSQL_USER=amigosuser \
  -e MYSQL_DATABASE=amigosdb \
  -e MYSQL_PASSWORD=amigospass \
  -v "$(pwd)/basedatos:/var/lib/mysql" \
  --rm -d --network pruebas mariadb

# 2. Arrancar Flask + Gunicorn
docker run --name amigos \
  -e DEPLOYMENT_MODE=production \
  -e DATABASE_URI=mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb \
  --rm -d --network pruebas amigos:1.0

# 3. Arrancar nginx
docker run --name nginx \
  --rm -d --network pruebas \
  -v "$(pwd)/sitios_nginx:/etc/nginx/conf.d:ro" \
  -p 80:80 nginx
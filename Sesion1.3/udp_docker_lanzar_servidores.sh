#!/bin/bash

docker rm -f broadcast1 broadcast2 broadcast3

docker run -d --name broadcast1 --network pruebas -v /home/uo295293/IngenieriaServiciosTMP/Sesion1.3:/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --name broadcast2 --network pruebas -v /home/uo295293/IngenieriaServiciosTMP/Sesion1.3:/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --name broadcast3 --network pruebas -v /home/uo295293/IngenieriaServiciosTMP/Sesion1.3:/app python:3.7 python /app/udp_servidor6_broadcast.py
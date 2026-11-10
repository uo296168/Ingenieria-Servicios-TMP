#!/bin/bash

docker rm -f cliente

docker run -it --network pruebas --name cliente -v /home/uo295293/IngenieriaServiciosTMP/Sesion1.3:/app python:3.7 python /app/udp_cliente6_broadcast.py 172.18.255.255
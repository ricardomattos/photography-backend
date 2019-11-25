#!/bin/sh

psql -U postgres -c "CREATE USER photography_user PASSWORD 'ph0t0gr4ph1'"
psql -U postgres -c "CREATE DATABASE photography OWNER photography_user"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE photography TO photography_user"
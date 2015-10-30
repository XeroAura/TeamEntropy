#!/bin/bash
for f in data/*
do
mysql -uxxxx -pxxxx -e "load data infile '/storage/data/"$f"' into table entropy.twitter character set utf8mb4 fields escaped by '' terminated by ',' enclosed by '"' lines terminated by '\t\n'"
done
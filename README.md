# potato-analytics sample

A demo app to illustrate import of two csv files that are linked and being imported with primary key preserved to csv column.

## data
The data is in two csv:
[countries.csv](https://github.com/evshvarov/potato-analytics/blob/1ee7677019463c39e146e89d3b795403daf10be2/data/countries.csv)
[potato_sales.csv](https://github.com/evshvarov/potato-analytics/blob/1ee7677019463c39e146e89d3b795403daf10be2/data/potato_sales.csv)

## Installation

### ZPM
It's packaged with ZPM so it could be installed as:
```
zpm "install esh-potato-analytics"
```
then open http://localhost:32794/dsw/index.html#/USER

you should see a dashboard with potato consumtion and import worldwide from 2000 to 2022 and with the ability to filter by countries:
<img width="1025" height="567" alt="Image" src="https://github.com/user-attachments/assets/cac519d1-01ac-479c-bf14-98eeceacbd59" />


### Docker
The repo is dockerised so you can  clone/git pull the repo into any local directory

```
$ git clone git@github.com:evshvarov/potato-analytics.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d
```
and open then http://localhost:32794/dsw/index.html#/USER


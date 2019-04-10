# Description

This is a simple application built using only Python. It provides /gene_suggest/:species/:gene/:limit endpoint which responds with a list of suggested gene names for the given gene query and target species. You can limit the number of suggestion hits using limit parameter.

# Starting the service
There are two ways to run this application
1) Run in a docker container
2) Clone the repo and run directly on your local machine

## Docker
Docker allows you to run applications in virtualized "containers". A docker image for this application is available from [DockerHub](https://hub.docker.com/r/sanjayboddu/python-gene-search)
### Requirements: Docker v18.09.0
```
docker run -p 8000:8011 -d sanjayboddu/python-gene-search
```
You should now be able to access the service at http://localhost:8000/ on your machine

## Local machine:
### Requirements: Python 3.x and Git
```
git clone https://github.com/sanjay-boddu/python-gene-search.git
cd python-gene-search/

# Install all the requirements for application
pip3 install --no-cache-dir -r requirements.txt

# Query Ensembl public MySQL server and create json files to use as data source
python dump_genes.py

# Start the app
python app.py 
```
You should now be able to access service at http://localhost:8011/ on your machine



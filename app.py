from flask import Flask, jsonify, make_response
import json
import re
from flask_restful import Resource, Api
import os

application = Flask(__name__)
api = Api(application)


class HelloEnsembl(Resource):
   def get(self, path=''):
       # Return 404 response status code with error message if user queries any endpoint other than gene_suggest
       return make_response(jsonify({'error': 'Use endpoint /gene_suggest/:species/:gene/:limit'}), 404)

class Gene(Resource):
   def get(self, species, gene, limit):
     
      # Search for species json file. If not found, return species not available message 
      species_data_file_path = "{}/data/{}.json".format(os.getcwd(), species.lower())
      if os.path.isfile(species_data_file_path):
         
         with open(species_data_file_path, 'r') as species_data_file:
            species_data = json.load(species_data_file)
         
         # Use compiled regex to find gene names starting with query gene string
         # Compiled regex helps in speeding up the process as we are dealing with large number of genes 
         search_regex = "^{}.*".format(gene)
         compiled_regex = re.compile(search_regex, re.IGNORECASE)
         found_genes = list(filter(compiled_regex.search, species_data))
        
         return make_response(jsonify({'gene_suggestions': found_genes[:limit]}), 200)
      else:
         return make_response(jsonify({'info': 'species {} not available'.format(species)}), 400)


api.add_resource(HelloEnsembl, '/', '/<path:path>')
api.add_resource(Gene, '/gene_suggest/<string:species>/<string:gene>/<int:limit>')


if __name__ == "__main__":
	application.run(host="0.0.0.0", port="8011")

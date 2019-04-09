from flask import Flask, jsonify
import json
import re
from flask_restful import Resource, Api
import os

application = Flask(__name__)
api = Api(application)


class HelloEnsembl(Resource):
    def get(self, path=''):
       return jsonify({'info': 'Use endpoint /gene_suggest/:species/:gene/:limit'})

class Gene(Resource):
   def get(self, species, gene, limit):
      
      species_data_file_path = "{}/data/{}.json".format(os.getcwd(), species.lower())
      if os.path.isfile(species_data_file_path):
         
         with open(species_data_file_path, 'r') as species_data_file:
            species_data = json.load(species_data_file)
        
         search_regex = "^{}.*".format(gene)
         compiled_regex = re.compile(search_regex, re.IGNORECASE)
         found_genes = list(filter(compiled_regex.search, species_data))
        
         return jsonify(found_genes[:limit])
      else:
         return jsonify({'info': 'species {} not available'.format(species)})


api.add_resource(HelloEnsembl, '/', '/<path:path>')
api.add_resource(Gene, '/gene_suggest/<string:species>/<string:gene>/<int:limit>')


if __name__ == "__main__":
	application.run(debug=True, host="0.0.0.0", port="8011")

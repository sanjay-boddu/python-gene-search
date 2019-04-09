from flask import Flask, jsonify
import json
import re
from flask_restful import Resource, Api
import os

application = Flask(__name__)
api = Api(application)


class HelloEnsembl(Resource):
    def get(self):
       return jsonify({'info': 'Use endpoint /<species>/<gene>'})

class Gene(Resource):
   def get(self, species, gene):
      
      species_data_file_path = "{}/data/{}.json".format(os.getcwd(), species.lower())
      if os.path.isfile(species_data_file_path):
         
         with open(species_data_file_path, 'r') as species_data_file:
            species_data = json.load(species_data_file)
        
         search_regex = "^{}.*".format(gene)
         compiled_regex = re.compile(search_regex, re.IGNORECASE)
         found_genes = list(filter(compiled_regex.search, species_data))
        
         return jsonify(found_genes)
      else:
         return jsonify({'info': 'species {} not available'.format(species)})


api.add_resource(HelloEnsembl, '/')
api.add_resource(Gene, '/<string:species>/<string:gene>')


if __name__ == "__main__":
	application.run(debug=True, host="0.0.0.0", port="8011")

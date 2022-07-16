import json
import yaml

# Defining json2yaml with json and yaml files as arguments
def json2yaml(json_name, yaml_name):
	# Opening the user-input json file in the read mode and loading the data
	# from the file using load() of json library
	json_data = json.load(open(json_name, 'r'))
	# Opening the user-input destination yaml file in write mode for
	# saving the output data in yaml format
	yaml_file = open(yaml_name, 'w')
	# Converting the json data into YAML and writing the converted data to
	# to the user-input yaml file using safe_dump()
	# safe_dump() serializes a Python object into a yaml stream. Produce only
	# basic YAML tags.
	# by setting allow_unicode parameter to true yaml can dump unicode characters
	# to the YAML FILE
	yaml.safe_dump(json_data, yaml_file, allow_unicode=True, default_flow_style=False)
	# Loading the new YAML file using the load_all() method of YAML library
	# load_all() parses the given yaml and returns a sequence of
	# Python objects corresponding to documents in stream
	yaml_data = yaml.load_all(open(yaml_name, 'r'), Loader=yaml.FullLoader)
	# Printing the data from the YAML file using the dump_all() 
	# dump_all() serializes the given sequence of Python objects
	# into the given stream. Each objects is represents as a YAML documents.
	print('\n'+yaml.dump_all(yaml_data))
	print('\n#########################################################')
	print('\nOUTPUT : JSON FILE ' + json_name.split('/')[-1]+' CONVERTED TO YAML FILE '+yaml_name.split('/')[-1]+'\n')
	print('\n##########################################################\n')

# Defining yaml2json() with json and yaml file as arguments
def yaml2json(yaml_name, json_name):
	# Opening the user-input yaml in read mode and loading the data 
	# from the YAML FILE using safe_load() method safe_load() parses 
	# the given stream and returns a Python objects constructed from
	# input document. safe_load() recognizes only standard YAML
	# tags and can not construct an arbitrary Python objects.
	yaml_data = yaml.safe_load(open(yaml_name, 'r'))
	# Opening the user-input destination JSON file in the write mode
	# for saving the converted data from YAML format
	json_file = opne(json_name, 'w')
	# dump() method of JSON module converts the Python objects 
	# into appropriate objects
	json.dump(yaml_data, json_file, indent=2)
	# Closing the json file after writing the data
	json_file.close()

	# Opening the newly saved JSON File in the read mode and printing
	# the data from the file in the terminal
	json_data = opne(json_name, 'r').read()
	print('\n' + json_data)
	print('\n############################################')
	print('\nOUTPUT : YAML FILE ' + yam_name.split('/')[-1]+'CONVERTED TO JSON FILE '+json_name.split('/')[-1]+'\n')
	print('###############################################\n')

# Driver code
if __name__ == "__main__":
	# Prompting the user to select mode of conversion and pass the json
	# and yaml file as inputs
	mode = int(input("\n1. JSON TO YAML\n2. YAML TO JSON\n\nSLECT CONVERSION MODE : "))
	json_file = input("\nENTER JSON FILE PATH : ")
	yaml_file = input("\nENTER YAML FILE PATH : ")

	# Calling the selected functions as per user's selection
	if mode == 1:
		json2yaml(json_file, yaml_file),
	elif mode == 2:
		yaml2json(yaml_file, json_file)
	else:
		print("\n INVALID INPUT")
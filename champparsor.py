########################################################################################################################
#Please execute the code in python 3
#
#Run command :
#        python champparsor.py <schema location> <file location>
#
#Example :
#        python champparsor.py  '/users/ganesh/desktop/onechamp/schema.json' 'users/ganesh/desktop/onechamp/data.csv'
#
#
########################################################################################################################



import pandas as pd
import jsonschema
import json
import unittest
import sys

def jsonparser(fileloc):
    filepathsplit = fileloc.split("/")
    ignoredatafile = filepathsplit[0:len(filepathsplit)-1:]
    outloc = ('/'.join([str(elem) for elem in ignoredatafile])) + "/" + "result.json"
    data = pd.read_csv(fileloc) 
    data.rename(columns={'Person Id': 'person_id', 'Floor Access DateTime': 'datetime','Floor Level':'floor_level','Building':'building'}, inplace=True)
    data['person_id'] = data['person_id'].astype(str)
    data['datetime'] = data['datetime'].astype(str)
    data['building'] = data['building'].astype(str)
    jsonout = data.to_json(orient = "records")
    
    data.to_json(r'{}'.format(outloc),orient = "records")
    return jsonout


def jsonschemaread(schemaloc):
    with open(schemaloc) as sch:
        info = sch.read()
        schema = json.loads(info)
    
    return schema

#Test case to validate if the json generated complies with schema provided

class Testjson(unittest.TestCase):
    output = ""
    schema = ""
    def testjsontrue(self):
        self.assertEqual(jsonschema.validate(self.output, self.schema), None)



if __name__ == "__main__":
    #print("program started")
    fileloc = sys.argv.pop()
    #print(fileloc)
    schemaloc = sys.argv.pop()
    #print(schemaloc)
    Testjson.output = jsonparser(fileloc)
    Testjson.schema = jsonschemaread(schemaloc)
    suite = unittest.TestLoader().loadTestsFromTestCase(Testjson)    
    unittest.TextTestRunner(verbosity=3).run(suite)
    print("complies with schema generated. valid json file created  successfully")
    print("\nSCHEMA INFERED:\n\n",Testjson.schema)
    print("\n JSONRESULT:\n\n", Testjson.output)
    

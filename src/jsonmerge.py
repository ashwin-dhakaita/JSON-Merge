import sys
import os
import re
import json
import copy
from collections import defaultdict

class JsonMerger:

    """
    JsonMerger class:

        The Json Merge utility is wrapped up in a single class JsonMerger.
        
    Merge Method:
        The merge method can be used to merge up the json files and output a single json file.
        
        @param f_path: The folder path where all of the json files are stored.
        @param i_base_name: The common base name of all the json files.
        @param o_base_name: The common base name of all the output files.
        @param max_f_sz: The maximum file size which should not be exceeded by the output file.    
    """

    #constructor of the JsonMerger class.
    def __init__(self):

        self.f_path = "";
        self.i_base_name = "";
        self.o_base_name = "";
        self.max_f_sz = 0;

    #helper method for calculating the counter value of the output file.
    def get_output_counter(self):

        matching_string = r"^%s(\d)+\.json$"%self.o_base_name;
        counter = 0;

        for file in os.listdir(self.f_path):
            if(re.match(matching_string, file)):
                counter += 1;
        
        return str(counter+1);
    
    #merges the json files.
    def merge(self, f_path, i_base_name, o_base_name, max_f_sz):

        self.f_path = f_path;
        self.i_base_name = i_base_name;
        self.o_base_name = o_base_name;
        self.max_f_sz = int(max_f_sz);

        files_to_open = [];
        matching_string = r"^%s(\d)+\.json$"%self.i_base_name;

        try:
            #retrieves all the files and folders in the specified path.
            for file in os.listdir(self.f_path):

                if(re.match(matching_string, file)):
                    files_to_open.append(file);   

            #sort the files in increasing order of their counter value.
            files_to_open = sorted(files_to_open, key= lambda f: int(re.search(r"(\d)+", f).group(0)));
            
            json_to_dump = defaultdict(lambda: None);

            #iterate thorugh all the files.
            for file in files_to_open:
                                
                f = None;
                prev_json_to_dump = copy.deepcopy(json_to_dump)
                try:
                    f = open(self.f_path+file, 'r');
                    loaded_json = json.load(f);
                    for key, _ in loaded_json.items():

                        if(json_to_dump[key] is None): 
                            json_to_dump[key] = []

                        if(type(loaded_json[key])==type([])):                            
                            json_to_dump[key] = json_to_dump[key] + loaded_json[key];
                        else:
                            json_to_dump[key].append(loaded_json[key]);
                                                                        
                except Exception as ex:
                    print(ex)
                
                finally:
                    if(f is not None):
                        f.close();

                #if the json file exceeds the max file limit the file is not merged.                                
                if(len(json.dumps(json_to_dump)) > self.max_f_sz):
                    json_to_dump = prev_json_to_dump;                    
                    break;
            
            #writes the merged json.
            f = open(self.f_path+self.o_base_name+self.get_output_counter()+".json", 'w+');            
            f.write(json.dumps(json_to_dump))
            f.close();        

        except Exception as e:
            print(e);

#if the script is used directly from command line instead of being imported as a class.
if __name__ == '__main__':
    
    f_path = sys.argv[1];
    i_base_name = sys.argv[2];
    o_base_name = sys.argv[3];
    max_f_sz = int(sys.argv[4]);

    jsonmerger = JsonMerger();
    jsonmerger.merge(f_path, i_base_name, o_base_name, max_f_sz);
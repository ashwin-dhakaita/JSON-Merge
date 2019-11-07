import unittest
import sys
import json

sys.path.insert(1, "../src");
from jsonmerge import JsonMerger

class TestMerge(unittest.TestCase):

    def test_merge(self):

        json_merger = JsonMerger();
        json_merger.merge("../json-files/", "DATA", "MERGE", "266");
        
        f = open("../output/MERGE.json");
        desired_json = json.load(f);

        f = open("../json-files/MERGE1.json");
        output_json = json.load(f);

        self.assertEqual(output_json, desired_json);
    
if __name__ == '__main__':
    unittest.main();





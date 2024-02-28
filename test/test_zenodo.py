import unittest
from zenodo_utils.deposition import Zenodo_deposition



class Test_Zenodo(unittest.TestCase):
    def test_deposition(self):
        """
        This method tests the File upload .
        """
        deposition_id = None
        with self.subTest():
            #print("Create")
            data = {
                "metadata": {
                    "title": "My first upload",
                    "upload_type": "image",
                    "image_type": "photo",
                    "access_right": "restricted",
                    "description": "This is my first upload",
                    "creators": [
                        {"name": "COPO", "affiliation": "Copo"}
                    ]
                }
            }
            deposition = Zenodo_deposition().create(deposition=data)
            deposition_id = deposition["id"] 
            assert deposition["metadata"]["upload_type"] == "image"
            assert deposition["metadata"]["image_type"] == "photo"
            deposition_file = Zenodo_deposition().upload_files(_id=deposition_id, file="/EDP/copo-project-org.png")
            assert deposition_file["filename"] == "copo-project-org.png"
            print(deposition_file)

      
        with self.subTest():
            deposition = Zenodo_deposition().publish(_id=deposition_id)
            assert deposition["submitted"] == True
            print(deposition)
       
        with self.subTest():
            deposition = Zenodo_deposition().unlock(_id=deposition_id)

        with self.subTest():
            deposition = Zenodo_deposition().read(deposition_id)
            assert deposition["metadata"]["upload_type"] == "image"
            assert deposition["metadata"]["image_type"] == "photo"
            deposition["metadata"]["description"] = "This is my first upload -- updated"

            deposition = Zenodo_deposition().update(deposition_id, {"metadata": deposition["metadata"]})
            assert deposition["metadata"]["description"] == "This is my first upload -- updated"

        with self.subTest():
            deposition = Zenodo_deposition().publish(_id=deposition_id)
            assert deposition["submitted"] == True
            print(deposition)
       

        with self.subTest():
            #print("Delete")
            pass
            Zenodo_deposition().delete(_id=deposition_id)
            
if __name__ == '__main__':
    unittest.main()
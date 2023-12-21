import unittest
from api.datatypes import Sample, Project
from utils.ppprint import print_p as pr


class TestSample(unittest.TestCase):
    def test_crud(self):
        """
        This method tests the CRUD (Create, Read, Update, Delete) operations of the Sample class.
        """
        recordId = None
        updated_sample_id = 'XYZ123'
        CustomerSampleName = 'COPOTestCustomerSampleName'
        with self.subTest():
            #print("Create")
            defin = Sample().get_type_definintion()
            assert type(defin) == dict
            assert defin["dataTypeName"] == "Sample"
            assert defin["dataTypeId"] == 143
            t_sample = Sample().create(data={"name": "test_sample", "description": "test_sample_description"})
            assert type(t_sample) == dict
            assert t_sample["dataTypeName"] == "Sample"
            assert type(t_sample["recordId"]) == int
            recordId = t_sample["recordId"]
        with self.subTest():
            #print("Update")
            assert Sample().update(_id=recordId, data={"SampleId": updated_sample_id, "TaxonId": 9606, "CustomerSampleName": CustomerSampleName})
        with self.subTest():
            #print("Read")
            t_sample = Sample().read(_id=recordId)
            assert type(t_sample) == dict
            assert t_sample["dataTypeName"] == "Sample"
            assert t_sample["fields"]["SampleId"] == updated_sample_id
            assert t_sample["fields"]["TaxonId"] == '9606'
            assert t_sample["fields"]["CustomerSampleName"] == CustomerSampleName
        with self.subTest():
            #print("Delete")
            assert Sample().delete(_id=recordId)



if __name__ == '__main__':
    unittest.main()

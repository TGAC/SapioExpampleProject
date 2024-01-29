import unittest
from api.datatypes import Sample, Project
from edp_utils.ppprint import print_p as pr
from sapiopylib.rest.pojo.DataRecord import DataRecord


class Test_Sample(unittest.TestCase):
    def test_crud(self):
        """
        This method tests the CRUD (Create, Read, Update, Delete) operations of the Sample class.
        """
        recordId = None
        updated_sample_id = 'XYZ123a'
        CustomerSampleName = 'COPOTestCustomerSampleName'
        comments = "This is a sample"
        with self.subTest():
            #print("Create")
            defin = Sample().get_type_definintion()
            assert type(defin) == dict
            assert defin["dataTypeName"] == "Sample"
            assert defin["dataTypeId"] == 143
            t_sample = Sample().create(data={"Comments":comments, "OtherSampleId": "Test sample"})
            assert type(t_sample) == DataRecord
            assert t_sample.data_type_name == "Sample"
            assert type(t_sample.record_id) == int
            recordId = t_sample.record_id
            print(t_sample)
        with self.subTest():
            #print("Update")
            Sample().update(_id=recordId, data={ "TaxonID": 9606, "CustomerSampleName": CustomerSampleName})
        with self.subTest():
            #print("Read")
            t_sample = Sample().read(_id=recordId)
            assert type(t_sample) == DataRecord
            assert t_sample.data_type_name == "Sample"
            #assert t_sample.fields["SampleId"] == updated_sample_id
            assert t_sample.fields["TaxonID"] == '9606'
            assert t_sample.fields["CustomerSampleName"] == CustomerSampleName
            assert t_sample.fields["Comments"] == comments
            print(t_sample)
        with self.subTest():
            #print("Delete")
            pass
            #Sample().delete(_id=recordId)
            

class TestProject(unittest.TestCase):
    def test_crud(self):
        """
        This method tests the CRUD (Create, Read, Update, Delete) operations of the Project class.
        """
        recordId = None
        updated_project_id = 'XYZ123'
        project_name = "test_project"
        with self.subTest():
            #print("Create")
            defin = Project().get_type_definintion()
            assert type(defin) == dict
            assert defin["dataTypeName"] == "Project"
            assert defin["dataTypeId"] == 119
            #t_project = Project().create(data={"name": "test_project", "description": "test_project_description"})
            t_project = Project().create(data={"ProjectName":project_name})
            assert type(t_project) == DataRecord
            assert t_project.data_type_name == "Project"
            assert type(t_project.record_id) == int
            recordId = t_project.record_id
        with self.subTest():
            #print("Update")
            Project().update(_id=recordId, data={"ProjectId": updated_project_id})
        with self.subTest():
            #print("Read")
            t_project = Project().read(_id=recordId)
            assert type(t_project) == DataRecord
            assert t_project.data_type_name == "Project"
            assert t_project.fields["ProjectId"] == updated_project_id
            assert t_project.fields["ProjectName"] == project_name
            print(t_project)
        with self.subTest():
            #print("Delete")
            Project().delete(_id=recordId)
            pass
if __name__ == '__main__':
    unittest.main()

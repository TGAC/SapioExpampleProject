import unittest
from api.datatypes import Sample, Project, Request, AssignedProcess
from edp_utils.ppprint import print_p as pr
from edp_utils.sapio_datamanager import Sapio
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



class TestRequest(unittest.TestCase):
    def test_crud(self):
        """
        This method tests the CRUD (Create, Read, Update, Delete) operations of the Project class.
        """
        recordId = None
        customer_name = "copo"
        requestName = "PIP-COPO"
        costCode = "Invoice"
        quoteRef = "quote"
        dataAccessGroup = "Internal"
        with self.subTest():
            #print("Create")
            defin = Request().get_type_definintion()
            assert type(defin) == dict
            assert defin["dataTypeName"] == "Request"
            assert defin["dataTypeId"] == 146
            #t_project = Project().create(data={"name": "test_project", "description": "test_project_description"})
            t_request = Request().create(data={"Customer_Name":customer_name, "RequestName": requestName, "CostCode": costCode, "QuoteRef":quoteRef, "DataAccessGroup":dataAccessGroup})
            assert type(t_request) == DataRecord
            assert t_request.data_type_name == "Request"
            assert type(t_request.record_id) == int
            recordId = t_request.record_id
        with self.subTest():
            #print("Update")
            Request().update(_id=recordId, data={"RequesterName": "debby"})
        with self.subTest():
            #print("Read")
            t_request = Request().read(_id=recordId)
            assert type(t_request) == DataRecord
            assert t_request.data_type_name == "Request"
            assert t_request.fields["Customer_Name"] == customer_name
            assert t_request.fields["RequestName"] == requestName
            assert t_request.fields["CostCode"] == costCode
            assert t_request.fields["QuoteRef"] == quoteRef
            assert t_request.fields["DataAccessGroup"] == dataAccessGroup
            assert t_request.fields["RequesterName"] == "debby"

            print(t_request)
        with self.subTest():
            #print("Delete")
            Request().delete(_id=recordId)
            pass
 
"""
class TestRequestSample(unittest.TestCase):
    def test_children(self):
        customer_name = "copo"
        requestName = "PIP-COPO"
        costCode = "Invoice"
        quoteRef = "quote"
        dataAccessGroup = "Internal"
        request_record = Sapio().inst_man.add_new_record("Request")
        request_record.set_field_values({"Customer_Name": customer_name, "RequestName": requestName, "CostCode": costCode, "QuoteRef":quoteRef, "DataAccessGroup":dataAccessGroup})
        print(request_record)

        request_record = Sapio().inst_man.get_known_record_with_record_id(request_record.record_id)   

        sample_record = Sapio().inst_man.add_new_record("Sample")
        sample_record.set_field_values({"ExemplarSampleType": "gDNA"})
        request_record.add_child(sample_record)

        assigned_process = Sapio().inst_man.add_new_record("AssignedProcess")
        assigned_process.set_field_values({"ProcessName":"Illumina LT"})
        assigned_process = Sapio().inst_man.get_known_record_with_record_id(request_record.record_id)   
        assigned_process.add_child(sample_record)
        Sapio().rec_man.store_and_commit()
"""

class TestRequestSample(unittest.TestCase):
    def test_children(self):
        request_recordId = None
        sample_recordId = None
        assignedProcess_recordId = None
        customer_name = "copo"
        requestName = "PIP-COPO"
        costCode = "Invoice"
        quoteRef = "quote"
        dataAccessGroup = "Internal"
        with self.subTest():
            t_request = Request().create(data={"Customer_Name":customer_name, "RequestName": requestName, "CostCode": costCode, "QuoteRef":quoteRef, "DataAccessGroup":dataAccessGroup, "PIP_Link": "jira url"})
            assert type(t_request) == DataRecord
            assert t_request.data_type_name == "Request"
            assert type(t_request.record_id) == int
            request_recordId = t_request.record_id

        CustomerSampleName = 'COPOTestCustomerSampleName'
        comments = "This is a sample"
        with self.subTest():
            t_sample = Sample().create(data={"Comments":comments, "OtherSampleId": "Test sample", "ExemplarSampleType": "gDNA", "ContainerType": "Tube"})
            assert type(t_sample) == DataRecord
            assert t_sample.data_type_name == "Sample"
            assert type(t_sample.record_id) == int
            sample_recordId = t_sample.record_id
            print(t_sample)

        with self.subTest():
            children = [
                {
                    "dataTypeName": "Sample",
                    "recordId": sample_recordId,
                    "fields" : {
                        "RecordId":sample_recordId,
                        "ExemplarSampleType" : "gDNA"
                    }
                }
            ]
            Request().add_childern(request_recordId,children )

        '''   
        with self.subTest():
            t_assignedProcess = AssignedProcess().create(data={"ProcessName":"Illumina LT", "SampleRecordId": sample_recordId, "RequestRecordId": request_recordId , "Data"})
            assert type(t_assignedProcess) == DataRecord
            assert t_assignedProcess.data_type_name == "AssignedProcess"
            assert type(t_assignedProcess.record_id) == int
            assignedProcess_recordId = t_assignedProcess.record_id           

        with self.subTest():
            children = [
                {
                    "dataTypeName": "Sample",
                    "recordId": sample_recordId,
                    "fields" : {
                        "RecordId":sample_recordId,
                    }
                }
            ]
            AssignedProcess().add_childern(assignedProcess_recordId, children)
        '''

        with self.subTest():
            #print("Delete")
            #Request().delete(_id=request_recordId, recursive_delete=True)
            pass
 
if __name__ == '__main__':
    unittest.main()
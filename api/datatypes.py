from edp_utils.sapioclient import SapioClient as client
from edp_utils.sapio_datamanager import Sapio
from sapiopylib.rest.pojo.DataRecord import DataRecord


class DataType():
    """
    Represents a generic data type.

    Attributes:
        sc (SapioClient): An instance of the SapioClient class.
        data_type (str): The name of the data type.
    """

    def __init__(self):
        
        """
        Initializes a new instance of the DataType class.
        """
        self.sc = client()
        self.data_type = None


    def get_type_definintion(self):
        """
        Retrieves the definition of the data type.

        Returns:
            dict: The definition of the data type.
        """
        return self.sc.do_get(method='/datatypemanager/datatypedefinition/' + self.data_type)

    def create(self, data):
        """
        Creates a new data record.

        Args:
            data (dict): The data to be included in the data record.

        Returns:
            dict: The created data record.
        """
        samples = Sapio().dataRecordManager.add_data_records_with_data(data_type_name=self.data_type, field_map_list=[data])
        return samples[0] if len(samples)>0 else None
        #return self.sc.do_post(method='/datarecord', dataType=self.data_type, params=data)

    def read(self, _id):
        """
        Retrieves a specific data record.

        Args:
            _id (str): The ID of the data record.

        Returns:
            dict: The retrieved data record.
        """
        #return self.sc.do_get(method='/datarecord', params={"dataTypeName": self.data_type, "recordId": _id})
        return Sapio().dataRecordManager.query_system_for_record(data_type_name=self.data_type, record_id=_id)

    def update(self, _id, data):
        """
        Updates a specific data record.

        Args:
            _id (str): The ID of the data record.
            data (dict): The updated data.

        Returns:
            dict: The updated data record.
        """
        #return self.sc.do_put(method='/datarecordlist/fields', _id=_id, params=data)
        data_record = self.read(_id=_id)
        data_record.set_fields(data)
        Sapio().dataRecordManager.commit_data_records(records_to_update= [data_record])

    def delete(self, _id):
        """
        Deletes a specific data record.

        Args:
            _id (str): The ID of the data record.

        Returns:
            dict: The response indicating the success of the deletion.
        """
        #return self.sc.do_delete(method='/datarecord', params={"dataTypeName": self.data_type}, _id=_id)
        data_record = DataRecord(data_type_name=self.data_type, record_id=_id, fields=[])
        Sapio().dataRecordManager.delete_data_record(record=data_record)

class Sample(DataType):
    """
    Represents a sample data type.

    Inherits from the DataType class.
    """

    def __init__(self):
        """
        Initializes a new instance of the Sample class.
        """
        super().__init__()
        self.data_type = "Sample"


class Project(DataType):
    """
    Represents a project data type.

    Inherits from the DataType class.
    """

    def __init__(self):
        """
        Initializes a new instance of the Project class.
        """
        super().__init__()
        self.data_type = "Project"

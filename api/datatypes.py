from utils.sapioclient import SapioClient as client

class Sample():
    def __init__(self):
        self.sc = client()
    
    def get_sample(self, sample_id):
        """
        Get a sample by ID.
        
        Args:
            sample_id (str): The ID of the sample to retrieve.
            
        Returns:
            dict: The sample object.
        """
        return self.sc.do_get(method='/datarecord', params={"dataTypeName": "Sample", "recordId": sample_id})


    
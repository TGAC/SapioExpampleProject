from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.DataMgmtService import DataMgmtServer
import os

class Sapio():
    sapio_user = SapioUser(url=os.getenv('SAPIOURL'),
                 guid=os.getenv('SAPIOGUID'), api_token=os.getenv('SAPIOTOKEN'), verify_ssl_cert=False)
    dataRecordManager = DataMgmtServer.get_data_record_manager(sapio_user)
    
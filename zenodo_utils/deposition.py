from zenodo_utils.zenodoclient import ZenodoClient

class Zenodo_deposition:
    def __init__(self, metadata={}, creators=[]):
        self.metadata = metadata
        self.creators = creators

    def read(self, _id):
        return ZenodoClient().do_get(method=f"/deposit/depositions/{_id}")

    def create(self, deposition):
        return ZenodoClient().do_post(method="/deposit/depositions", params=deposition)

    def update(self, _id, deposition ):
        return ZenodoClient().do_put(method=f"/deposit/depositions/{_id}", params=deposition)
    
    def upload_files(self, _id, file ) :
        files = {'file': open(file, 'rb')}
        return ZenodoClient().do_post(method=f"/deposit/depositions/{_id}/files",  files=files )

    def delete(self, _id):
        return ZenodoClient().do_delete(method=f"/deposit/depositions/{_id}")
    
    def publish(self, _id):
        return ZenodoClient().do_post(method=f"/deposit/depositions/{_id}/actions/publish")
    
    def unlock(self, _id):
        return ZenodoClient().do_post(method=f"/deposit/depositions/{_id}/actions/edit")

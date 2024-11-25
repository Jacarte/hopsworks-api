from common.hopsworks_client import HopsworksClient
import numpy as np

if __name__ == "__main__":
    hopsworks_client = HopsworksClient()
    project = hopsworks_client.get_project()  
    ds_api = project.get_dataset_api()

    # Replace by a 
    size = int(1*(1024*1024*1024)) # 1GB
    file = "random.dat"

    with open("random.dat", "wb") as output:
        output.write(np.random.bytes(size))

    # Upload the file
    hw_path = ds_api.upload(file, "Resources", simultaneous_uploads=10)
    assert ds_api.exists(hw_path)

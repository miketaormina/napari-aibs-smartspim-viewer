import numpy as np
from napari_aibs_smartspim_viewer import napari_get_reader
from dask import array as da
import json


# tmp_path is a pytest fixture
def test_reader(tmp_path):
    """An example of how you might test your plugin."""

    # write some fake data using your supported file format
    #my_test_file = str(tmp_path / "myfile.npy")
    original_data = da.random.randint(0, 255, (20,20),)
    #np.save(my_test_file, original_data)
    
    my_test_file_zarr = str(tmp_path / "zdata.zr")
    my_test_file = str(tmp_path / "myfile.json")
    da.to_zarr(original_data, my_test_file_zarr, component='0')
    json_dict = {
        "zdata": {
        "zarr_file": "zdata.zr",
        "nlevels": 1,
        "color": "green",
        "contrast": [
            0.0,
            100.0
        ],
        "excitation": 488
    }
    }
    with open(my_test_file, 'w') as f:
        json.dump(json_dict, f)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None

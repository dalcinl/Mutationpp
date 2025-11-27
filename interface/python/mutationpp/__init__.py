from ._mutationpp import *  # noqa: F403 # ty: ignore[unresolved-import]

import os

if "MPP_DATA_DIRECTORY" not in os.environ:
    mpp_directory = os.path.dirname(__file__)
    mpp_data_directory = os.path.join(mpp_directory, "data")
    os.environ["MPP_DATA_DIRECTORY"] = mpp_data_directory
    del mpp_directory, mpp_data_directory

del os

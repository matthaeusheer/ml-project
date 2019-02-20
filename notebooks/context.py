import os
import sys

"""
This file basically makes sure that we can import ml_project and its subpackages correctly from notebooks
which are stored in the notebooks directory as

    from context import ml_project
    
From this point on we can import anything from ml_project as we wish.
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ml_project
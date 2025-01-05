import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

inp1 =  get_input( part=1,
    day=1, 
    year=2024,
)



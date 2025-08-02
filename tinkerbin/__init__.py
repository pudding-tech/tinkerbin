#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tinkerbin - A collection of utility tools for scientific computing and data analysis.

This package provides tools for:
- Numpy array manipulation and collection classes
- Numerical integration and Fourier transforms
- I/O operations and file management
- Logging and printing utilities
- Timer functions
- Parameter storage and management
- Dictionary utilities
- Function evaluation helpers
- IPython integration
"""

# Import all public functions and classes from each module
from .numpy_tools import *
from .numerics_tools import *
from .utils import *
from .io import *
from .logging import *
from .timers import *
from .timer_utils import *
from .printing import *
from .printing_utils import *
from .parameter_store import *
from .dictionaries import *
from .function_evaluation import *
from .ipython import *

# Version info
__version__: str = "1.0.0"
__author__: str = "Jan Gulla"

"""
The flask application package.
"""
import sys

from flask import Flask

app = Flask(__name__)

import Pollock.views

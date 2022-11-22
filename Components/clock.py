import math
import datetime
import threading
import time

from config import eventForClock, event
from hand_detect import run_until_hand_detected
from utils import debugShow, clearPorts
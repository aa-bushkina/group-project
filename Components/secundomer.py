import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import debugShow, clearPorts

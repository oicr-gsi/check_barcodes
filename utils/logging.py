import sys
import logging

log = logging.getLogger('')
logging.basicConfig(
    level=logging.getLevelName(logging.INFO),
    format="[%(asctime)s] %(levelname)s %(message)s",
    datefmt="%H:%M:%S", stream=sys.stdout)
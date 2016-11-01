import logging

import data
import speech

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

data.flat_data('/home/nhanh/work/raw')

speech.diarize_workflow()

from time import sleep

import pyttsx3

from source.logging_utils import get_logger

logger = get_logger()
engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# engine.setProperty('rate', 300)
#
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# engine.setProperty('voice', 'english+f2')
# engine.setProperty('rate', 185)


sample_text = "Quote 71. “I wandered through the streets thinking of all the things I might have said and might have done had I been other than I was.” ― Erich Maria Remarque, Three Comrades"
output = "200_sound_using_pyttsx3_output.mp3"

try:

    engine.save_to_file(sample_text, output)
    engine.runAndWait()

    sleep(10)
except Exception as err:
    logger.error(f"Get exception. Sleep and retry: {err}")
    logger.info("we need to wait about 1-2 h and continue.")
    sleep(60 * 60 * 1)

from time import sleep
from source.logging_utils import get_logger
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

logger = get_logger()

models = [
    "tts_models/en/ek1/tacotron2",
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/ljspeech/tacotron2-DDC_ph",
    "tts_models/en/ljspeech/glow-tts",
    "tts_models/en/ljspeech/speedy-speech",
    "tts_models/en/ljspeech/tacotron2-DCA",
    "tts_models/en/ljspeech/vits",
    "tts_models/en/ljspeech/vits--neon",
    "tts_models/en/ljspeech/fast_pitch",
    "tts_models/en/ljspeech/overflow",
    "tts_models/en/ljspeech/neural_hmm",
    "tts_models/en/vctk/vits",
    "tts_models/en/vctk/fast_pitch",
    "tts_models/en/sam/tacotron-DDC",
    "tts_models/en/blizzard2013/capacitron-t2-c50",
    "tts_models/en/blizzard2013/capacitron-t2-c150_v2",
    "tts_models/en/multi-dataset/tortoise-v2",
    "tts_models/en/jenny/jenny"
]

sample_text = "Quote 71. “I wandered through the streets thinking of all the things I might have said and might have done had I been other than I was.” ― Erich Maria Remarque, Three Comrades"
output = "sound_using_tts_output.wav"

# tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", gpu=False)


# print(TTS().list_models())

print()
# logger = get_logger()
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
#
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# engine.setProperty('voice', 'english+f2')
# engine.setProperty('rate', 185)


try:
    path = r"C:\Users\Valentinas\AppData\Local\Programs\Python\Python311\Lib\site-packages\TTS\.models.json"

    model_manager = ModelManager(path)

    # for model in models:
    model = "tts_models/en/ljspeech/tacotron2-DDC"
    model_path, config_path, model_item = model_manager.download_model(model)

    voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )

    outputs = syn.tts(sample_text)
    syn.save_wav(outputs, f"{model.replace('tts_models/en/', '').replace('/', '_')}___{output}")

    # tts.tts_to_file(
    #     text=sample_text,
    #     speaker_wav="",
    #     file_path=output,
    #     language="en")

    sleep(10)
except Exception as err:
    logger.error(f"Get exception. Sleep and retry: {err}")
    logger.info("we need to wait about 1-2 h and continue.")
    # sleep(60 * 60 * 1)

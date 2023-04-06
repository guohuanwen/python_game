import base64
import gzip
import os
import wave


def pcm2wav(pcm_data, out_path, channel, sample_rate):
    with wave.open(out_path, 'wb') as wav_file:
        ## 不解之处， 16 // 8， 第4个参数0为何有效
        wav_file.setparams((channel, 16 // 8, sample_rate, 0, 'NONE', 'NONE'))
        wav_file.writeframes(pcm_data)
        wav_file.close()

pcmfile = 'data.gz'
with open(pcmfile, 'rb') as pcm_file:
    data = pcm_file.read()
    pcm_file.close()
if data:
    pcm = gzip.decompress(base64.b64decode(data))
    pcm2wav(pcm, "voice.wav", 1, 16000)


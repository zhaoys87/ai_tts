'''
实现tts功能
author: zhaoys@whu.edu.cn
date: 2024-05-24
'''
from timer import timer
import pyttsx3
from gtts import gTTS


@timer
def text_to_speech_ttsx3(text, outfile="", lang=""):
    '''
    使用pyttsx3实现tts功能
    有点：支持多种语音引擎，支持多种语音格式，支持离线且能快速上手
    不足：合成的语音有点生硬，不够自然, 速度5s
    '''
    engine = pyttsx3.init()
    if len(lang) > 0:
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'zh_CN' in voice.languages:
                engine.setProperty('voice', voice.id)
                # print(voice.id, voice.languages)
                break
    # engine.say('中文测试语音')
    # engine.runAndWait()
    if len(outfile) > 0:
        engine.save_to_file(text, outfile)
        engine.runAndWait()


@timer
def text_to_speech_gtts(text, outfile, lang='en'):
    '''
    使用gtts实现tts功能
    优点：简单易用、支持多种语言、合成效果良好，能进行Tokenization（可不限长度）
    不足：合成效果不够自然，速度较慢43s
    google有cloud版本，基于深度学习做的效果较好，但是需要收费
    '''
    text = text.replace('\n', ' ')
    tts = gTTS(text=text, lang=lang)
    tts.save(outfile)



if __name__ == "__main__":

    txt = '''黄帝，是少典氏的后代，姓公孙，名叫轩辕。生下来就显出神灵，
    在一般人还不会说话的时候就能说话，幼小的时候就很机智，长大后聪慧敏捷,
    二十岁时就见识广博善于明辨了轩辕所生活的时代，神农氏的子孙后代道德衰薄,
    各路诸侯互相侵犯攻伐，欺压百姓，但是神农氏无力征讨他们。
    在这种情况下轩辕就多次动用武力征讨诸侯中不来朝拜神农氏的人，因而诸侯们都来归顺轩辕。
    在作乱的诸侯中蚩尤最为暴虐，没有人能征讨他。炎帝想侵犯欺凌诸侯，诸侯们都来归顺轩辕。
    轩辕于是修治德政，整肃军旅，顺应四季气象，种植黍、稷、豆、麦、稻等作物，抚慰民众，丈量四方的土地，
    训练以熊、貔、貅、躯、虎为圃腾的氏族，来和炎帝在阪泉的郊野作战。双方多次交战，然后黄帝实现了战胜炎帝的愿望。
    蚩尤发动叛乱，不服从黄帝的命令。于是黄帝就征召四方诸侯的军队，和蚩尤在涿鹿的郊野交战，很快就捕获并杀死了蚩尤。
    四方诸侯都尊轩辕为天子，取代神农氏，这就是黄帝。天下有不顺从的，黄帝就去讨伐他们，平定了一个地方后就离开这个地方。
    黄帝披斩山林草木开通道路，从来没有安宁地居住在什么地方。
    黄帝往东到达过海滨，登上丸山，并到过泰山；往西到达过空桐，登上鸡头山；
    往南到达了长江，登上了熊山、湘山；往北驱逐过荤粥族，和诸侯们在釜山验合符契信物，并在涿鹿山下的平地上构筑城邑。
    黄帝奔波往来不断搬迁，没有固定的居住地点，住在哪裹，就以军队按环形驻扎在自己周围。
    官职都用“云”来命名，设立以“云”命名的军队。设立左右大监，监察众多诸侯国。
    诸国和谐，对鬼神山川I封禅祭祀的事情，在历来帝王中被称为规模最大的。获得了实鼎，运用神蓍草来推算历法预知节气日辰。
    推举风后、力牧、常先、大鸿来治理民众。顺应天地四季的规律，阴阳五行的征兆，关于死生的礼仪，国家安危存亡的道理。
    按照季节播种百谷草木，驯化各种鸟兽昆虫。黄帝的德政广泛传布，旁及曰月星辰和水土石金玉，黄帝劳心劳力，
    有节制地利用江湖山林的资源。由于有“土德”的祥瑞，所以就号称黄帝。
    黄帝有二十五个儿子，他们中得到姓氏的有十四人。'''

    text_to_speech_ttsx3(txt, "hello_ttsx3.mp3", lang='zh_CN')
    # text_to_speech_ttsx3("hello world", "hello.mp3")

    # text_to_speech_gtts(txt, "hello_gtts.mp3", lang='zh-cn')

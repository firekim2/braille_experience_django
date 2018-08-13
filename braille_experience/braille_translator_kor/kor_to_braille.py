import map_kor_to_braille
import re


UNRECOGNIZED = '?'

open_quotes = True

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ',
                'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ',
                'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ',
                'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ',
                'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ',
                'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',
                'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ',
                'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def extract_words(string):
    words = string.split(" ")
    result = []
    for word in words:
        temp = word.split("\n")
        for item in temp:
            result.append(item)
    return result


def numbers_handler(word):
    if word == "":
        return word
    result = word[0]
    if word[0].isdigit():
        result = map_kor_to_braille.number_start + map_kor_to_braille.numbers.get(word[0])
    for i in range(1, len(word)):
        if word[i].isdigit() and word[i-1].isdigit():
            result += map_kor_to_braille.numbers.get(word[i])
        elif word[i].isdigit():
            result += map_kor_to_braille.number_start + map_kor_to_braille.numbers.get(word[i])
        else:
            result += word[i]
    return result


def punctuation_handler(word):
    if word == "":
        return word
    result = ""
    for char in word:
        try:
            result += map_kor_to_braille.punctuation.get(char)
        except Exception:
            result += char
    return result


def contractions_handler(word):
    for key, value in map_kor_to_braille.contractions.items():
        word = word.replace(key, value)
    return word

def char_handler(word):
    split_text = list(word)
    for key in split_text:
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', key) is not None:
            char = ord(key) - BASE_CODE
            char1 = int(char / CHOSUNG)
            char2 = int((char - (CHOSUNG * char1)) / JUNGSUNG)
            char3 = int((char - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result = map_kor_to_braille.CHOSUNG_letters.get(CHOSUNG_LIST[char1])\
                    + map_kor_to_braille.JUNGSUNG_letters.get(JUNGSUNG_LIST[char2])
            if char3 is not 0:
                result += map_kor_to_braille.JONGSUNG_letters.get(JONGSUNG_LIST[char3])
            word = word.replace(key, result)
    return word


def translate(string):
    words = extract_words(string)
    braille = ""
    for word in words:
        word = numbers_handler(word)
        word = punctuation_handler(word)
        word = contractions_handler(word)
        word = char_handler(word)
        word += " "
        braille += word
    print(braille[:-1])
    return braille[:-1]  # Remove the final space that was added.

if __name__ == "__main__":
    translate("우리는 서로 더 많은 것을 꿈꾸었다.")

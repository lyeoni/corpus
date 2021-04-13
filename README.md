# Corpus

## Overivew
|Corpus|Size|Content|Source|
|:-:|:-:|:-:|:-:|
|문어 말뭉치|10.31GB|책 등 저작물 문서 20,188개|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|구어 말뭉치|7.22GB|방송, 강연 등의 공적 구어, 드라마 대본 등의 준구어 총 25,696건|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|일상 대화 말뭉치 2020|0.32GB|일상 대화 총 2,232건|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|한국어-영어 번역(병렬) 말뭉치|0.28GB|문어체 110만, 구어체 50만 문장(한영 번역)|[AI Hub](https://aihub.or.kr/aidata/87)|


## Details

### 구어 말뭉치 (CorpusSpokenKo)
방송, 강연 등의 공적 구어 자료, 드라마 대본 등의 준구어 자료로 구성한 구어 말뭉치
- 공적 독백 2,490건
- 공적 대화 19,104건
- 준구어-대본 4,102건(드라마 4,102회 분량)

#### Parameters
- `complete_conversation` : noise가 될 수 있는 들리지 않는 음절, 전혀 들리지 않는 부분, ­불완전 발화, 비식별화 기호들을 제거한 완전한 대화 셋만 보존. Default: `True`.
    - `complete_conversation==True`: 64M / 대화 4,289건 / 855,385 발화 턴(set of sentences)
    - `complete_conversation==False`: 996M / 대화 25,550건 / 14,173,010 발화 턴

<br>
<hr>
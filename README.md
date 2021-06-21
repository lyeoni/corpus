# Corpus

## Overivew
|Corpus|Size|#Sentences|Content|Source|
|:-:|:-:|:-:|:-:|:-:|
|문어 말뭉치|6.96GB (10.31GB)|27,355,222|책 등 저작물 문서 20,188개|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|구어 말뭉치|68MB (7.22GB)|856,932|방송, 강연 등의 공적 구어, 드라마 대본 등의 준구어 총 25,696건|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|일상 대화 말뭉치 2020|1.6MB (0.32GB)||일상 대화 총 2,232건|[국립국어원 - 모두의 말뭉치](https://corpus.korean.go.kr/main.do)|
|한국어-영어 번역(병렬) 말뭉치|0.28GB||문어체 110만, 구어체 50만 문장(한영 번역)|[AI Hub](https://aihub.or.kr/aidata/87)|

\* Size열의 괄호는 코퍼스 원본 파일 크기를 의미

<br>

## Usage
```python
from corpus import *
corpus = CorpusWrittenKo(root='NIKL_WRITTEN(v1.0)')
corpus.save() # Save corpus to root directory.
```

## Details
### 문어 말뭉치 (CorpusWrittenKo)
**책**, 잡지, 보고서 등 저작물 20,188종의 문어 원시 말뭉치
- 책 : 상상 4,946종 (24.50%) / 정보 14,757종 (73.10)
- 잡지 73종 (0.36%) / 보고서 등 412종 (2.04%)

#### Content
- 문서는 `'\n\n'`, 문장은 `'\n'` 으로 구분
    ```
    [문서1_문장1]
    ...
    [문서1_문장N]
    
    [문서2_문장1]
    ...
    ```


<hr>


### 구어 말뭉치 (CorpusSpokenKo)
방송, 강연 등의 공적 구어 자료, 드라마 대본 등의 준구어 자료로 구성한 구어 말뭉치
- 공적 독백 2,490건 / 공적 대화 19,104건
- 준구어-대본 4,102건(드라마 4,102회 분량)

#### Content
- 대화는 `'\n\n'`, 대화 내 발화는 `'\n'` 으로 구분
    ```
    [대화1_화자1_발화]
    [대화1_화자2_발화]
    ...
    [대화1_화자3_발화]

    [대화2_화자1_발화]
    ...
    ```

#### Parameters
noise가 될 수 있는 들리지 않는 음절, 전혀 들리지 않는 부분, ­불완전 발화, 비식별화 기호들을 제거하기 위한 parameter 제공

- `complete_sentence`: 기호들을 제거한 완전한 문장만을 보존. Default: `True`.
    - `complete_sentnece==False`: 1.05GB / 대화 25,696 건 / 14,286,065 발화 턴 
- `complete_conversation`: 기호들을 제거한 완전한 대화만을 보존. Default: `True` (`complete_sentence==True`).
    - `complete_conversation==True`: 68MB / 대화 4,292 건 / 856,932 발화 턴
    - `complete_conversation==False`: 985MB / 대화 25,696 건 / 13,660,968 발화 턴


<hr>


### 일상 대화 말뭉치 2020 (CorpusDialogueKo)
15개 주제, 13개의 제시 자료(국립국어원 신문 말뭉치(버전 1.0)에서 선정한 신문 기사)를 대상
으로 두 명의 화자가 자유롭게 대화를 나눈 일상 대화(총 2,739명 화자, 대화당 약 15분 분량,
총 500시간 분량) 자료를 전사하여 구성한 말뭉치

일상 대화 총 2,232건
- 15개 주제 대화 1,818건
- 13개 제시 자료 대화 414건

#### Content
- 자세한 파일 내용은 아래의 `Parameters` 참고
- 대화는 `'\n\n'`, 대화 내 발화는 `'\n'` 으로 구분
- example
```
[대화1_화자1_발화]
[대화1_화자2_발화]
...
[대화1_화자3_발화]

[대화2_화자1_발화]
...
```

#### Parameters
구어 말뭉치(CorpusSpokenKo)와 동일한 parameter 제공
- `complete_sentence`: 기호들을 제거한 완전한 문장만을 보존. Default: `True`.
    - `complete_sentnece==False`: 27MB / 대화 2,232 건 / 30,555 발화 턴 
- `complete_conversation`: 기호들을 제거한 완전한 대화만을 보존. Default: `True` (`complete_sentence==True`).
    - `complete_conversation==True`: 2MB / 대화 146건 / 2,125 발화 턴
    - `complete_conversation==False`: 27MB / 대화 2,232 건 / 30,488 발화 턴

<hr>

### 서울말 낭독체 발화 말뭉치
말뭉치 파일 사이즈의 많은 부분을 음성 파일이 차지하고 있음. 때문에 텍스트는 상당히 적어 활용 하지 않음.
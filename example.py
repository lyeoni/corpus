from corpus import *

if __name__=='__main__':
    
    corpus = CorpusSpokenKo(root='국립국어원 구어 말뭉치(버전 1.1)')
    # corpus = CorpusWrittenKo(root='국립국어원 문어 말뭉치(버전 1.0)')
    # corpus = CorpusDialogueKo(root='국립국어원 일상 대화 말뭉치 2020(버전 1.0)')
    
    corpus.save()

    print(corpus[0], corpus[-1], sep='\n')
    print(len(corpus))
    print(corpus)
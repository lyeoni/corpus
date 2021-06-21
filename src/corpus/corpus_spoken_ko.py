import json
from pathlib import Path

from .corpus import Corpus

class CorpusSpokenKo(Corpus):
    """ 구어 말뭉치 (국립국어원 모두의 말뭉치)
        Args:
            :complete_conversation: 완전한 문장만을 보존
            :complete_conversation: 완전한 대화만을 보존
    """
    def __init__(self, root=None, name='nikl_spoken', complete_sentence=True, complete_conversation=False):
        super().__init__(name)
        self.root = root
        self.complete_sentence = complete_sentence
        self.complete_conversation = complete_conversation
        
        if not self.root:
            raise ValueError('Set the corpus directory path to `root`')


        self.corpus = self.load(self.root)
    
    def load(self, root):
        file_paths = sorted(list(Path(root).glob('*.json')))
        corpus = []

        for path in file_paths:
            try:
                with open(path, 'r') as f:
                    example = json.load(f)

                document = example['document'][0]
                
                sid, buffer = None, None
                conversation = []

                for ut in document['utterance']:
                    original_form = ut['original_form'].strip()
                    form = ut['form'].strip()

                    # 불완전한 문장 포함하는 utterance 사용 X
                    if '&' in original_form or '-' in original_form or '(())' in original_form or '((xx' in original_form:
                        # & : 비식별화 기호(이름, 주민등록번호, 카드번호, 주소, 전화번호)
                        # - : 불완전 발화
                        # (()) : 전혀 들리지 않는 부분
                        # ((xx)) : 들리지 않는 음절
                        if self.complete_sentence:
                            if self.complete_conversation:
                                break
                            else:
                                continue
                    
                    # 비어있는 문장
                    if form == '':
                        continue
                    
                    # buffer를 conversation에 추가
                    if sid != ut['speaker_id']:
                        if buffer:
                            conversation.append(buffer)

                        sid = ut['speaker_id']
                        buffer = form
                    else:    
                        buffer += ' ' + form
                    
                else:
                    # conversation을 데이터셋에 추가
                    conversation.append(buffer)
                    corpus.append(conversation)
            except:
                print(f'[Erorr] in {path}, skip it.')
                continue

        return corpus

    def save(self, fname=None):
        fname = f'{self.name}.txt' if fname is None else fname
        path = Path(self.root).parent / fname

        with open(path, 'w') as writer:
            for conversation in self.corpus:
                try:
                    for ut in conversation:
                        writer.write(ut.strip()+'\n')
                    writer.write('\n')
                except:
                    continue
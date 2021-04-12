import json
from pathlib import Path

class CorpusSpokenKo:
    """ 구어 말뭉치 (국립국어원 모두의 말뭉치)
        Args:
            :complete_conversation: 완전한 대화 데이터만 보존
    """
    def __init__(self, root_dir=None, complete_conversation=True):
        self.complete_conversation = complete_conversation

        self.text = self.load(root_dir)

    def __len__(self):
        return len(self.text)

    def __getitem__(self, i):
        return self.text[i]

    def load(self, root_dir):
        file_paths = sorted(list(Path(root_dir).glob('*.json')))
        text = []

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
                    if self.complete_conversation:
                        # & : 비식별화 기호(이름, 주민등록번호, 카드번호, 주소, 전화번호)
                        # - : 불완전 발화
                        # (()) : 전혀 들리지 않는 부분
                        # ((xx)) : 들리지 않는 음절
                        if '&' in original_form or '-' in original_form or '(())' in original_form or '((xx' in original_form:  
                            break
                    
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
                    text.append(conversation)
            except:
                print(f'[Erorr] in {path}, skip it.')
                continue

        return text
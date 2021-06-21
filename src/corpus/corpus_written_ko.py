import json
from pathlib import Path

from .corpus import Corpus

class CorpusWrittenKo(Corpus):
    def __init__(self, root=None, name='nikl_written'):
        super().__init__(name)
        self.root = root
        
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
                paragraph = []

                for pa in document['paragraph']:
                    form = pa['form'].strip()

                    # 비어있는 문장
                    if form == '':
                        continue

                    # paragraph에 추가
                    paragraph.append(form)

                else:
                    # paragraph를 데이터셋에 추가
                    corpus.append(paragraph)

            except:
                print(f'[Erorr] in {path}, skip it.')
                continue

        return corpus

    def save(self, fname=None):
        fname = f'{self.name}.txt' if fname is None else fname
        path = Path(self.root).parent / fname

        with open(path, 'w') as writer:
            for paragraph in self.corpus:
                try:
                    for para in paragraph:
                        writer.write(para.strip()+'\n')
                    writer.write('\n')
                except:
                    continue
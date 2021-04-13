import json
from pathlib import Path

from .corpus_spoken_ko import CorpusSpokenKo

class CorpusDialogueKo(CorpusSpokenKo):
    def __init__(self, root=None, name='nikl_dialogue', complete_conversation=True):
        super().__init__(root, name, complete_conversation)
        
        if not self.root:
            raise ValueError('Set the corpus directory path to `root`')
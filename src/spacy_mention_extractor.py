"""
Written by Ari Bornstein
"""

import spacy
from spacy.symbols import nsubj, VERB
from mention_extractor import MentionExtractor, Mentions
from doc_collection import DocumentCollection
from tqdm import tqdm

class SpacyMentionExtractor(MentionExtractor):
        """
        A spacy implementaion of the mention extractor
        """

        def __init__(self):
                super().__init__()
                self.nlp = spacy.load('en_core_web_md', disable=['ner'])
        
        def extract_mentions(self, collections, event=True, entity=True):
                """
                Extracts all cross document entity mentions from a 
                document collection. 
                """
                mentions = Mentions()
                for col in tqdm(collections):
                        for doc in col.documents:
                                doc_text = self.nlp(doc.text) # this is a hack to prevent running the spacy parser twice
                                if doc.text:
                                        if entity:
                                                mentions.entity_mentions += self._extract_enitiy_mentions(col.collection_id,
                                                                                        doc.doc_id, doc_text)
                                        if event:
                                                mentions.event_mentions += self._extract_event_mentions(col.collection_id,
                                                                                doc.doc_id, doc_text)
                return mentions

        def _extract_enitiy_mentions(self, collection_id, doc_id, doc_text):
                """
                Extracts entity mentions using spacy entites note this doesn't handle pronouns
                """
                mentions = []
                for chunk in doc_text.noun_chunks:
                        # extract entity 
                        mention = {\
                                "topic_id": collection_id, #Required (a topic is a set of multiple documents that share the same subject)
                                "doc_id": doc_id, #Required (the article or document id this mention belong to)
                                "tokens_number": [i+1 for i in range(chunk.start, chunk.end)],  #Optional (the token number in sentence, will be required when using Within doc entities)
                                "tokens_str": chunk.text, #Required (the mention text)
                        }
                        mentions.append(mention)
                return mentions

        def _extract_event_mentions(self, collection_id, doc_id, doc_text):
                """
                Extracts event mentions from document using spacy verbs
                """
                mentions = []
                for sent in doc_text.sents:
                    for possible_subject in sent:
                        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                                mention = {\
                                "topic_id": collection_id, #Required (a topic is a set of multiple documents that share the same subject)
                                "doc_id": doc_id, #Required (the article or document id this mention belong to)
                                "tokens_number": [i+1 for i in range(possible_subject.head.i, possible_subject.head.i - (sent.start + 1))],  #Optional (the token number in sentence, will be required when using Within doc entities)
                                "tokens_str": possible_subject.head.text, #Required (the mention text)
                                }
                                mentions.append(mention)
                return mentions


if __name__ == "__main__":
        pass


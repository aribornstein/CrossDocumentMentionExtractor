"""
Written by Ari Bornstein
"""

import spacy
from spacy.symbols import nsubj, VERB
from mention_extractor import MentionExtractor, Mentions
from doc_collection import Collection, DocumentCollection

class SpacyMentionExtractor(MentionExtractor):
        """
        A spacy implementaion of the mention extractor
        """

        def __init__(self):
                super().__init__()
                nlp = spacy.load('en_core_web_sm')
                pass
        
        def extract_mentions(self, collections, event=True, entity=True):
                """
                Extracts all cross document entity mentions from a 
                document collection. 
                """
                mentions = Mentions()
                for col in collections:
                        for doc in col.documents:
                                doc_text = nlp(doc.text) # this is a hack to prevent running the spacy parser twice
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
                for entity in doc.ents:
                    # extract entity 
                    mention = {\
                        "topic_id": "2_ecb", #Required (a topic is a set of multiple documents that share the same subject)
                        "doc_id": "1_10.xml", #Required (the article or document id this mention belong to)
                        "tokens_number": [13],  #Optional (the token number in sentence, will be required when using Within doc entities)
                        "tokens_str": "Josh", #Required (the mention text)
                    }
                    print(entity.text, entity.label_)

        def _extract_event_mentions(self, collection_id, doc_id, doc_text):
                """
                Extracts event mentions from document using spacy verbs
                """
                verbs = set()

                for sent in doc_text.sents:
                    for possible_subject in sent:
                        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                            verbs.add(possible_subject.head)
                            print(possible_subject.head.i,  possible_subject.head.i - sent.start)
                            mention = {\
                                "topic_id": "2_ecb", #Required (a topic is a set of multiple documents that share the same subject)
                                "doc_id": "1_10.xml", #Required (the article or document id this mention belong to)
                                "tokens_number": [13],  #Optional (the token number in sentence, will be required when using Within doc entities)
                                "tokens_str": "Josh", #Required (the mention text)
                            }

                print(verbs)

if __name__ == "__main__":
        pass


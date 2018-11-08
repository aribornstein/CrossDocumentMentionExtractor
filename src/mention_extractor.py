"""
"""

from doc_collection import Collection, DocumentCollection

class Mentions:
        """
        Contains all entity and event mentions
        """
        def __init__(self):
                self.entity_mentions = []
                self.event_mentions = []

class MentionExtractor:
        """
        A base class for implementing mention extraction
        """

        def __init__(self):
                pass

        def extract_mentions(self, collections, event=True, entity=True):
                """
                Extracts all cross document entity mentions from a 
                document collection. 
                """
                mentions = Mentions()
                for col in collections:
                        for doc in col.documents:
                                if entity:
                                        mentions.entity_mentions += self._extract_enitiy_mentions(col.collection_id,
                                                                                  doc.doc_id, doc.text)
                                if event:
                                        mentions.event_mentions += self._extract_event_mentions(col.collection_id,
                                                                                doc.doc_id, doc.text)

                return mentions
        
        def _extract_enitiy_mentions(self, collection_id, doc_id, doc_text):
                """
                Extracts entity mentions from document implemented by user 
                must return entites in following format see http://nlp_architect.nervanasys.com/cross_doc_coref.html
                {
                        "topic_id": "2_ecb", #Required (a topic is a set of multiple documents that share the same subject)
                        "doc_id": "1_10.xml", #Required (the article or document id this mention belong to)
                        "mention_head": "Josh", #Optional
                        "mention_head_lemma": "josh", #Optional
                        "mention_head_pos": "NOUN", #Optional (part of speech)
                        "mention_ner": null, #Optional (named entity recognition)
                        "mention_type": "HUM", #Optional (for debugging)
                        "sent_id": 0, #Optional (mention sentence number in document)
                        "tokens_number": [ #Optional (the token number in sentence, will be required when using Within doc entities)
                        13
                        ],
                        "tokens_str": "Josh", #Required (the mention text)
                }
                """
                raise Exception("Not yet implemented")

        def _extract_event_mentions(self, collection_id, doc_id, doc_text):
                """
                Extracts event mentions from document implemented by user 
                must return entites in following format 
                Extracts entity mentions from document implemented by user 
                must return entites in following format see http://nlp_architect.nervanasys.com/cross_doc_coref.html
                {
                        "topic_id": "2_ecb", #Required (a topic is a set of multiple documents that share the same subject)
                        "doc_id": "1_10.xml", #Required (the article or document id this mention belong to)
                        "mention_head": "Josh", #Optional
                        "mention_head_lemma": "josh", #Optional
                        "mention_head_pos": "NOUN", #Optional (part of speech)
                        "mention_ner": null, #Optional (named entity recognition)
                        "mention_type": "HUM", #Optional (for debugging)
                        "sent_id": 0, #Optional (mention sentence number in document)
                        "tokens_number": [ #Optional (the token number in sentence, will be required when using Within doc entities)
                        13
                        ],
                        "tokens_str": "Josh", #Required (the mention text)
                }
                """
                raise Exception("Not yet implemented")



if __name__ == "__main__":
        pass
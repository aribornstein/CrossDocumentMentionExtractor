"""
Written by Ari Bornstein 
"""
class Document:
        """
        A Document is a base class that text string and a document_id
        """
        def __init__(self, doc_id, text):
                self.doc_id = doc_id
                self.text = text

class DocumentCollection:
        """
        A DocumentCollection is a base class that contains a list 
        of documents and a unique collection_id
        """
        def __init__(self, collection_id, documents):
                self.collection_id = collection_id
                self.documents = documents

        def add_doc(document):
                """
                Add document to collection
                """
                self.documents.append(document)

        def remove_doc(doc_id):
                """
                Removes document with a given id from collection
                """
                for d in self.documents:
                    if d.doc_id == doc_id:
                        self.documents.remove(d)


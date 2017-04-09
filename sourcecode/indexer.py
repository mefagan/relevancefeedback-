import sys
import lucene
import os
from tidylib import tidy_document
from htmlparser import parsehtml

from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexWriter,  IndexWriterConfig, Version

def createIndex():
    #initialize lucene and jvm
    print("started indexer")
    lucene.initVM()
    indexDir = "/Tmp/REMOVEME.index-dir"

    
    #get the analyzer
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    
    #get index storage
    dir = lucene.SimpleFSDirectory(lucene.File(indexDir))
   
    writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))

    src_dir = 'html_files'
    i = 0
    for l in os.listdir(src_dir):
        l = os.path.join(src_dir, l)
        with open(l, 'r') as myfile:
            data=myfile.read()
        i += 1
        document, errors = parsehtml(data)
        doc = Document()
        doc.add(Field("text", document, Field.Store.YES, Field.Index.ANALYZED))
        writer.addDocument(doc)
    writer.optimize()
    writer.close()

def main():
    createIndex()
if __name__ == '__main__':
    main()



import sys
import lucene
import os


from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexWriter,  IndexWriterConfig, Version

if __name__ == "__main__":
    #initialize lucene and jvm

    lucene.initVM()
    
    indexDir = "/Tmp/REMOVEME.index-dir"

    print ("lucene version is:", lucene.VERSION)
    
    #get the analyzer
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    
    #get index storage
    dir = lucene.SimpleFSDirectory(lucene.File(indexDir))
   
    writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))
    
    print ("%d docs in index", writer.numDocs())


    path = '/Users/maryeileenfagan/wse/test'
    i = 0
    for l in sys.stdin:
        #for l in os.listdir(path):
        i += 1
        doc = Document()
        doc.add(Field("text", l, Field.Store.YES, Field.Index.ANALYZED))
        writer.addDocument(doc)
    writer.optimize()
    writer.close()

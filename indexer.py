import sys
import lucene

from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexWriter,  IndexWriterConfig, Version

if __name__ == "__main__":
    #initialize lucene and jvm

    lucene.initVM()
    
    indexDir = "/Tmp/REMOVEME.index-dir"

    print "lucene version is:", lucene.VERSION
    
    #get the analyzer
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    
    #get index storage
    dir = lucene.SimpleFSDirectory(lucene.File(indexDir))
   
    writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))
    
    print "%d docs in index" % writer.numDocs()
    print "Reading lines from sys.stdin..."

    i = 0
    print >> sys.stderr, "Reading lines from sys.stdin..."
    for l in sys.stdin:
        i += 1
        doc = Document()
        doc.add(Field("text", l, Field.Store.YES, Field.Index.ANALYZED))
        writer.addDocument(doc)
        
        if i % 10000 == 0:
            print >> sys.stderr, "Read %d lines from stdin (%d documents in index)..." % (i, writer.numDocs())
    print >> sys.stderr, "Indexed a total of %d lines from stdin (%d documents in index)" % (i, writer.numDocs())
    print >> sys.stderr, "About to optimize index of %d documents..." % writer.numDocs()
    writer.optimize()
    print >> sys.stderr, "...done optimizing index of %d documents" % writer.numDocs()
    print >> sys.stderr, "Closing index of %d documents..." % writer.numDocs()
    writer.close()
    print >> sys.stderr, "...done closing index of %d documents" % writer.numDocs()

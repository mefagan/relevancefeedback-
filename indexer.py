import sys
import lucene

from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexWriter,  IndexWriterConfig, Version

if __name__ == "__main__":
    lucene.initVM()
    dir = SimpleFSDirectory(File("index/"))
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))
    
    print "%d docs in index" % writer.numDocs()
    print "Reading lines from sys.stdin..."

    for n, l in enumerate(sys.stdin):
        doc = Document()
        doc.add(Field("text", l, Field.Store.YES, Field.Index.ANALYZED))
        writer.addDocument(doc)
    print "Indexed %d lines from stdin (%d documents in index)" % (n, writer.numDocs())
    print "Closing index of %d docs..." % writer.numDocs()
    writer.close()

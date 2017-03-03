import subprocess
from crawler import spider

def BuildSearchEngine(url, number, domain):
    p1 = subprocess.Popen(["python3", "crawler.py", url, number, domain])
    p2 = subprocess.Popen(["python2.6", "indexer.py"])
    # 90 is the timeout in seconds
    try:
        out_1, errs_1 = p1.communicate(timeout=90)
    
    except subprocess.TimeoutExpired:
        p1.kill()
        out_1, errs_1 = p1.communicate()
    
    try:
        out_2, errs_2 = p2.communicate(timeout=90)
    except subprocess.TimeoutExpired:
        p2.kill()
        out_2, errs_2 = p2.communicate()


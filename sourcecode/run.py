import subprocess

def BuildSearchEngine(url, number, domain):
    p1 = subprocess.Popen(["python3", "crawler.py", url, str(number), domain])
    p1.wait()
    p2 = subprocess.Popen(["python2.6", "indexTest.py"])
    p2.wait()
    p3 = subprocess.Popen(["python2.7", "removeStopWords.py"])
    p3.wait()
    # 90 is the timeout in seconds
    try:
        out_1, errs_1 = p1.communicate(timeout=500)
    
    except subprocess.TimeoutExpired:
        p1.kill()
        out_1, errs_1 = p1.communicate()
    
    try:
        out_2, errs_2 = p2.communicate(timeout=180)
    except subprocess.TimeoutExpired:
        p2.kill()
        out_2, errs_2 = p2.communicate()

    try:
        out_3, errs_3 = p3.communicate(timeout=180)
    except subprocess.TimeoutExpired:
        p3.kill()
        out_3, errs_3 = p3.communicate()

def main():
    BuildSearchEngine("https://en.wikipedia.org/", 25, "wikipedia.org")
if __name__ == '__main__':
    main()

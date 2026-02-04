# import threading

# threads = []

# for url in urls:
#     t = threading.Thread(target=download_file, args=(url,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()


from multiprocessing import process

def process(line):
    print(line.strip())
    with open('file.txt','r') as f:
        
        
        
    
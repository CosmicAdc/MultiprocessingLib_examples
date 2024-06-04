
import multiprocessing
from myfunc import myFunc

if __name__ == 'main':
    for i in range(6):
        process= multiprocessing.Process(target=myFunc(), args= (i,))
        process.start()
        process.join()
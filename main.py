
import src.libs.schedule as sc
import src.libs.schedulev1 as sc1
import config as cg
import  time
import  os
from multiprocessing import Pool

def jobfunc(nam=''):
    print(nam)

def demo(inp):
    # sc.every(10).seconds.do(jobfunc)
    sc.every(10).seconds.do(jobfunc, nam=inp)
    # sc.run_pending()
    sc.run_continuously()
    time.sleep(1)
    print(os.getppid())

def main():
    while True:
        print(" Enter Catiop To Start Process")
        text =  input(sc.jobs)
        if text == '1':
            sc.clear()
            sc.cancel_job(sc.jobs)
            print("TErminated")
            return
        demo(text)




if __name__ == "__main__":
    main()

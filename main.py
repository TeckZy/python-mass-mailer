
import src.libs.schedule as sc
import  time
import  os

def jobfunc():
    print("Job Done ")

def demo():
    sc.every(1).seconds.do(jobfunc)
    while True:
        sc.run_pending()
        time.sleep(1)
        print(os.getppid())

def main():
    demo()


if __name__ == "__main__":
    main()

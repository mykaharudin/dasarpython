import os, py_compile

def main():
    os.chdir("E:\tes")
    py_compile.compile("hello.py")
    print("file hello.pyc telah dibuat...")
    os.system("pause");

if __name__ == "__name__":
    main()
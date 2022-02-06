def main():
    d={'satu':1,'dua':2,'tiga':3 }

    print("data yang ada :")
    print(d)

    d['empat']=4
    d['lima']=5

    print("\ndata yang ada ditambah :")
    print(d)

    d['satu']=60
    d['dua']=40

    print("\ndata yang ada ubah :")
    print(d)

    del d['lima']
    print("\ndata yang ada dihapus :")
    print(d)
if __name__ == "__main__":
    main()
from app import App

if __name__=="__main__":
    try:
        App()
    except Exception as e:
        print("Something went wrong.")
        exit(1)
        
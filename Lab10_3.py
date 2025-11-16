def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print("All information done")

if __name__ == "__main__":
    data(1,2, "Hello", "I", "try", "to", "Crash", "your", "Site", 38)
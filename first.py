

def aritmatika():
    input_a = int(input("masukan angka A : "))
    input_b = int(input("masukan angka B : "))

    check_a = isinstance(input_a, int)
    check_b = isinstance(input_b, int)

    if check_a == True and check_b == True:

        Result1 = int(input_a + input_b)
        Result2 = int(input_a - input_b)
        Result3 = int(input_a * input_b)
        Result4 = float(input_a / input_b)

        print("(value a + value b) = ",Result1)
        print("(value a - value b) = ",Result2)
        print("(value a * value b) = ",Result3)
        print("(value a / value b) = ",Result4)



    else:

        print("masukan angka dengan benar")
        exit()


    


def main():
    aritmatika()

if __name__ == "__main__":
    main()
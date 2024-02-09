def safe_print_list(my_list=[], x=0):
    for i in my_list:
        try:  
            print(i, end=" ")
        except:
            print("error")

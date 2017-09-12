import os
def rename_files():
    file_list=os.listdir("/home/deepak/Documents/basic-python-projects/secret-message/message1")
    print(file_list)
    os.chdir("/home/deepak/Documents/basic-python-projects/secret-message/message1")
    for f_name in file_list:
        os.rename(f_name , f_name.translate(None, "0123456789"))
        print(f_name)

rename_files()

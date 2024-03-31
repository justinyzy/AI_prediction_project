import os

def check_file(path, raise_b = True):
    """
        This function is used to check if file exist or not.

        Input:
            path: File path for checking.
            raise_b: Once the file not exist raise an error or not.
        Return:
            True if exist, False if not exist.
    """

    """
        Check file exist or not with os module.
    """
    if os.path.isfile(path):
        print("File: {}  ==> exist.\n".format(path))
        return True
    else:
        if raise_b:
            raise(ValueError("Can't find file: ", path))
        else:
            return False
    
def check_dir_exist(dir, create_bool=False, over_protect=False):
    """
        This function is use to check if the dir is exist or not
        while setting the create bool to true it will create the 
        dir for you without raising an error to interrupt the code.

        Input: 
            dir: dir you want to check.
            create_bool: Wheather to create the dir if not exist.
                default value will be false.
        Return: None
    """

    """
        Check the dir exist or not with os module.
    """
    if os.path.isdir(dir):
        if over_protect:
            check = input("Dir {} exist, Enter 1 to overwrite: \t".format(dir))
            if check == str(1):

                return True
            else:
                raise(ValueError("Stop for protection data.\n"))
    else:
        if create_bool:
            """
                Once create_bool is true while the dir not exist create one with the
                os module.
            """
            os.mkdir(dir)
            return False
        else:

            """
                Raise an error if dir not exist and user don't allow to create one.
            """
            raise(ValueError("Can't find dir: ", dir))
    
"""
    Checking if there miss some parameter.

    Input args:
        tar_arg: arg going to check
        tar_list: dict key going to check in the tar arg.
        name: This is only for showing.
        raise_b: Wheather find out any key not exist in dict raise an error or not.
    Return:
        res: Check result. If all the key exist in dict res is true.
"""
def check_key_in_dict(tar_arg, tar_list, name="none", raise_b=True):

    """
        Create checking result as true.
    """
    res = True

    """
        Check all the tar key one by one.
    """
    for i in tar_list:

        """
            Once key exist in dict, show specific information on the command window.
        """
        if i in tar_arg:
            ("Got {} in {}.\n".format(i, name))
        else:
            """
                Once find out key not in the dict raise an error or set res to False.
            """
            if raise_b:
                raise(ValueError("Missing {} in {}", i, name))
            else:
                res = False

    return res


def file_name_finder(tar_path, assign_type="", show_res=False):
    """
        This function is use to get the list of file in the directory
        with user set type

        Input:
            dir: Path of directory you want to check.
            type: File type you are interested in. (EX: ".jpg")

        Return:
            file_name_list: The file math what you want.
    """

    """
        First check target directory exist or not.
    """
    check_dir_exist(tar_path)

    """
        Create a list to store the result.
    """
    res_list = []

    """
        Check all the file name in the directory having file type 
        user want or not. Once the file name have type match the 
        target, add the file name to the store list.
    """
    for file_member in os.listdir(tar_path):
        if file_member.endswith(assign_type):
            res_list.append(file_member)

    """
        If show res is true. Show the result on the command window.
    """
    if show_res:
        print("Got_res: \n{}".format(res_list))

    return res_list

def file_name_filter(name_list, keyword, show_res=False):
    """
        This function is use to filter out some file name with 
        specific key in the result of function "file_name_finder"

        Input:
            name_list: The list result of function "file_name_finder".
            key_word: File with keyword which you don't want.
        
        Return:
            filt_out_res:   File list without key in name.
            key_res:        File list with keyword
    """

    """
        Create the list to store teh result.
    """
    filt_res = []
    key_res  = []

    """
        Check the file in the name_list one by one.
    """
    for i in name_list:
        """
            Check the keyword in the file name or not.
        """
        find_res = i.find(keyword)

        """
            Once the keyword in the file name add that file name 
            into the key_res otherwise add into the filt_res.
        """
        if find_res == -1:
            filt_res.append(i)
        else:
            key_res.append(i)

    """
        Show the result once the show_res is true.
    """
    if show_res:
        print("Filt_res: \n{}".format(filt_res))
        print("Key_res: \n{}".format(key_res))

    return filt_res, key_res
# Mohammad Murad
# vdr4jr
# A library that aids students and instructions in finding information about classes

import urllib.request

def instructor_lectures(department, instructor):
    '''
    Takes in a department name and instructor name and returns a list of classes the instructor teaches in that department

    :param department (str): String indicating what the department is
    :param instructor (str): String indicating what instructors name
    :return classes (list): List of string class names
    '''
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department
    s = urllib.request.urlopen(url)
    classes = []
    for row in s:
        row = row.decode('utf-8')
        aclass = row.strip("\n").split("|")
        if aclass[5] == "Lecture":
            if '+' in aclass[4]:
                professor = aclass[4][0:aclass[4].index("+")]
                if professor == instructor:
                    if aclass[3] not in classes:
                        classes.append(aclass[3])
            else:
                if instructor == aclass[4]:
                    if aclass[3] not in classes:
                        classes.append(aclass[3])
    return classes

def compatible_classes(first_class, second_class, needs_open_space=False):
    '''
    Takes in a str name of two classes and checks if those classes are compatible, with an optional argument to check if those classes are open

    :param first_class (str): name of the first class
    :param second_class (str): name of the second class
    :param needs_open_space (bool): boolean of if the classes need to be open
    :return (bool): a boolean if the classes are compatible/open
    '''
    first_class_department = first_class[0:first_class.index(" ")]
    second_class_department = second_class[0:second_class.index(" ")]
    first_class_info = get_class_info(first_class, first_class_department)
    second_class_info = get_class_info(second_class, second_class_department)
    if needs_open_space:
        if first_class_info[15] >= first_class_info[16] or second_class_info[15] >= second_class_info[16]:
            return False
        else:
            for i in range(7, 12):
                if first_class_info[i] == second_class_info[i]:
                    if first_class_info[12] == second_class_info[12] or first_class_info[12] == second_class_info[13] or first_class_info[13] == second_class_info[12] or second_class_info[13] == first_class_info[13]:
                        return False
    else:
        for i in range(7,12):
            if first_class_info[i] == second_class_info[i]:
                if first_class_info[12] == second_class_info[12] or first_class_info[12] == second_class_info[13] or first_class_info[13] == second_class_info[12] or second_class_info[13] == first_class_info[13]:
                    return False
    return True


def get_class_info(class_name, department):
    '''
    Helper function to get a list of the class information

    :param class_name (str): name of class
    :param department (str): name of department class is in
    :return (list): list of the class's information
    '''
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department
    s = urllib.request.urlopen(url)
    for row in s:
        row = row.decode('utf-8')
        aclass = row.strip().split("|")
        aclass_name = aclass[0] + " " + aclass[1] + "-" + aclass[2]
        if aclass_name == class_name:
            return aclass

from io import open
import sys


def read_people_cvs_exercise():
    list_of_keys = ['id', 'name', 'last_name', 'date_of_birth']

    try:
        file = open("people.csv", "r", encoding="utf8")
        lines = file.readlines()
        person_list = []
        for line in lines:
            person_values = line.replace("\n", "").split(",")
            person_dictionary = {}
            for index, value in enumerate(person_values):
                person_dictionary[list_of_keys[index]] = value
            person_list.append(person_dictionary)
        for person in person_list:
            print("[id]={} {} {} => {}".format(person['id'], person['name'], person['last_name'],
                                               person['date_of_birth']))
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)
    finally:
        file.close()
        del file


def counter_exercise():
    try:
        file = open("counter.txt", "a+", encoding="utf8")
        file.seek(0)
        content = file.readline()
        if len(content) <= 0:
            content = "0"
            file.write(content)
        file.close()

        counter = int(content)
        if len(sys.argv) == 2:
            if sys.argv[1] == "inc":
                counter += 1
            elif sys.argv[1] == "dec" and counter > 0:
                counter -= 1
        print(counter)

        file = open("counter.txt", "w", encoding="utf8")
        file.write(str(counter))
        file.close()
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)
    finally:
        file.close()
        del file


read_people_cvs_exercise()
counter_exercise()

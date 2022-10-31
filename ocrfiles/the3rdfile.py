import csv

# text= """
# Name Presha Class 10th
# ‘Age 15 Section B Roll_No. 32 Adm_Ns. 4330
#
# Father's_Name Sameer Occupation Engineer
# Mother’s_Name Bharti Occupation Doctor
# Address 1155A
#
# """

def textsplit(text):

    data = text.split()

    name = data[1]
    class1 = data[3]
    age = data[5]
    section = data[7]
    roll = data[9]
    adm = data[11]
    fname = data[13]
    focc = data[15]
    mname = data[17]
    mocc = data[19]
    add = data[21]

    print(name)
    print(class1)
    print(age)
    print(section)
    print(roll)
    print(adm)
    print(fname)
    print(focc)
    print(mname)
    print(mocc)
    print(add)

    with open("data.csv", "a") as pasta:
        writer = csv.writer(pasta)
        writer.writerow((name, class1, section, roll, adm, fname, focc, mname, mocc, add))
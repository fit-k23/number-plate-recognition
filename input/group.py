from glob import glob

import os
import shutil
from lxml import etree

annotations = dict()
annotations['foreign'] = "images-20231210T151305Z-001/images"
annotations['native'] = "voc_plate_dataset/Annotations"

images = dict()
images['foreign'] = "images-20231210T151305Z-001/images"
images['native'] = "voc_plate_dataset/JPEGImages"

output = "dataset"

def deleteFolderContents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    print("Deleted \"" + folder_path + "\"'s contents")

def fixPath(path):
    return os.path.abspath(path).replace("\\", "/")

def fileExists(path):
    return os.path.isfile(path)

def folderExists(path):
    return os.path.exists(path)

def fileBasename(path):
    """Filename with extension"""
    return os.path.basename(path)

def fileName(path):
    path = os.path.basename(path)
    return os.path.splitext(path)[0]

def fileExtension(path):
    return os.path.splitext(path)[1]

def copyFile(source, destination):
    return shutil.copyfile(source, destination)

def saveImage(source, destination):
    if not fileExists(source):
        return False
    copyFile(source, destination)
    return True

def createDirectory(path):
    if not folderExists(path):
        os.makedirs(path)
        print("Created directory: \"" + output + "\"")

subgroups = {
    'nhanuoc': 'government',
    'boderngoaigiao': 'diploma-border',
    'rotatengoaigiao': 'diploma-rotate',
    'brightnessngoaigiao': 'diploma-brightness',
    'cropngoaigiao': 'diploma-crop',
    'ngoaigiao': 'diploma',
    'boderquandoi': 'military-border',
    'brightnessquandoi': 'military-brightness',
    'cropquandoi': 'military-crop',
    'rotatequandoi': 'military-rotate',
    'quandoi': 'military',
    'kinhdoanh': 'business',
    'kd': 'business',
    'CarLongPlate': 'citizen-long',
    'xemayBigPlate': 'citizen-big',
    'xemay': 'citizen-big',
    '*': 'unknown'
}

groupName = {
    'diploma-border': 'diploma-plate',
    'diploma-rotate': 'diploma-plate',
    'diploma-brightness': 'diploma-plate',
    'diploma-crop': 'diploma-plate',
    'diploma': 'diploma-plate',
    'military-border': 'military-plate',
    'military-rotate': 'military-plate',
    'military-brightness': 'military-plate',
    'military-crop': 'military-plate',
    'military': 'military-plate',
    'government': 'gov-plate',
    'business': 'business-plate',
    'citizen-big': 'plate',
    'citizen-long': 'plate',
    'foreign': 'plate',
    'unknown': 'plate'
}

amount = {
    'diploma-border': 10,
    'diploma-rotate': 10,
    'diploma-brightness': 10,
    'diploma-crop': 10,
    'diploma': 10,
    'military-border': 10,
    'military-rotate': 10,
    'military-brightness': 10,
    'military-crop': 10,
    'military': 10,
    'government': 10,
    'business': 20,
    'citizen-big': 250,
    'citizen-long': 200,
    'foreign': 200,
    'unknown': 10
}

def countConstruct(dict):
    newDict = {}
    for key, value in dict.items():
        newDict[key] = 0
    return newDict

countAmount = countConstruct(amount)
# print(countAmount)

# if group type was set in here, they will be picked randomly, not supported!
random = [
    'citizen-big',
    'citizen-long',
    'foreign'
]

createDirectory(output)
createDirectory(output + "/annotations")
deleteFolderContents(output + "/annotations")
createDirectory(output + "/images")
deleteFolderContents(output + "/images")

def getGroupType(name, file):
    if name == "foreign":
        return "foreign"
    for pattern, t in subgroups.items():
        if pattern in file:
            return t
    return "unknown"

def getGroupTypeAmount(t):
    if t in amount:
        return amount[t]
    else:
        return amount['unknown']

def getGroupTypeCount(t):
    if t in countAmount:
        return countAmount[t]
    else:
        return countAmount['unknown']

def addGroupTypeCount(t):
    if t in countAmount:
        countAmount[t] += 1
    else:
        countAmount['unknown'] += 1

def getGroupName(t):
    if t in groupName:
        return groupName[t]
    else:
        return groupName['unknown']

total = 0
for name, annotation in annotations.items():
    excludedList = []
    files = glob(annotation + "/*.xml")
    for file in files:
        grouptype = getGroupType(name, file)
        typeAmount = getGroupTypeCount(grouptype)
        if typeAmount > getGroupTypeAmount(grouptype):
            continue
        tree = etree.parse(file)
        root = tree.getroot()
        path = root.find("filename").text
        if fileExists(path):
            if not fileExtension(path) == "jpg":
                continue
            realfilepath = path
        else:
            realfilepath = images[name] + "/" + fileName(file) + ".jpeg"
            if not fileExists(realfilepath):
                realfilepath = images[name] + "/" + fileName(file) + ".jpg"
                if not fileExists(realfilepath):
                    continue
        destination = output + "/images/" + grouptype + str(typeAmount) + ".jpg"
        if grouptype == "unknown":
            print("Unknown file: " + file)
            continue
        if not fileExists(destination):
            copyFile(realfilepath, destination)
        root.find("filename").text = grouptype + str(typeAmount) + ".jpg"
        root.find("path").text = "../" + "images/" + grouptype + str(typeAmount) + ".jpg"
        member_object2 = root.findall("object")
        if len(member_object2) > 1:
            print ("Multiple objects case: " + file + " -> " + grouptype + str(typeAmount))
        for member in member_object2:
            member.find('name').text = getGroupName(grouptype)
        tree = etree.ElementTree(root)
        addGroupTypeCount(grouptype)
        total += 1
        tree.write(output + "/annotations/" + grouptype + str(typeAmount) + ".xml", pretty_print=True)
print("Total of " + str(total) + " images were selected!")
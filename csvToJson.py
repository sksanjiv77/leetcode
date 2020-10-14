import csv, json
import random
import string
# def csvToJson(csv_file_path, json_File_path)

def csvToJson2(csvFilePath, jsonFilePath):
    data = []
    _attributes = ["first_name", "last_name", "email"]
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            #id = csvRow["id"]
            print generate_user_name(csvRow)
            if not manager_filter(csvRow):
                continue
            entry = {}
            for attr in _attributes:
                if attr in csvRow:
                    entry[attr] = csvRow[attr]
                else:
                    print "Could not find attribute '%s' " %(attr)
            data.append(entry)

    with open(jsonFilePath, "w") as jsonFile:
        return jsonFile.write(json.dumps(data, indent=5))

def csvToJson(csvFilePath, jsonFilePath):
    records = []
    _attributes = ["first_name", "last_name", "x", 'y']
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            #print generate_user_name(csvRow)
            
            if manager_filter(csvRow):
                user_name = generate_user_name(csvRow)
                csvRow["user_name"] = user_name
                password = generate_password(10)
                csvRow["password"] = password
                message = '''
                Dear %s %s,

                Please use the below information to login:
                User name : %s
                Password :%s

                Thanks
                Admin 
                ''' %(csvRow["first_name"], csvRow["last_name"], user_name, password)
                csvRow["message"] = message
                records.append(csvRow)

    with open(jsonFilePath, "w") as jsonFile:
        return jsonFile.write(json.dumps(records, indent=5))

def generate_password(n):
    return ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '@$#%&*') for i in range(n) ])

def female_filter(row):
    return row["gender"] == 'Female'

def manager_filter(row):
    return int(row["id"]) > 5

def generate_user_name(row):
    user_name = row["first_name"][0] + row["last_name"]
    return user_name.lower()


if __name__ == "__main__":
    csvFilePath = "F:\software\softwares\MOCK_DATA.csv"
    jsonFilePath = "F:\software\softwares\MOCK_DATA_JSON.json"
    print csvToJson(csvFilePath, jsonFilePath)
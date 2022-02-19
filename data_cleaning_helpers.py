import json
import math

def convertToJson(employmentTypeSeries):
    try:
        return json.loads(employmentTypeSeries)
    except:
        return ''

def getMinSalary(employmentTypeSeries):
    
    jsonObj = convertToJson(employmentTypeSeries)
    minSalary = math.nan
    
    for elem in jsonObj:
        if not elem['salary'] == 'None':
            minSalary = min(elem['salary']['from'], minSalary)
    return minSalary

def getMaxSalary(employmentTypeSeries):
    
    jsonObj = convertToJson(employmentTypeSeries)
    minSalary = math.nan
    
    for elem in jsonObj:
        if not elem['salary'] == 'None':
            #in this day (19.02) there were only two currencies
            #the usd currency is taken approximately
            #asthere is only a few usd salary
            
            currency = 4 if elem['salary']['currency'] == 'usd' else 1
            minSalary = min(elem['salary']['to'], minSalary)*currency
    return minSalary

def DoesContractTypeExists(employmentTypeSeries, typeOfContract):
    jsonArr = convertToJson(employmentTypeSeries)
    
    for elem in jsonArr:
        if elem['type'].lower() == typeOfContract.lower():
            return 1
    return 0
        
def isTechnologyRequired(title, skillsSeries,  techName):
    isNameInTitle = techName in title.lower()
    
    if isNameInTitle:
        return 1
    
    jsonSkillsArr = convertToJson(skillsSeries)
    
    for elem in jsonSkillsArr:
        if techName in elem['name'].lower():
            return 1
    return 0    

def sumLevelsOfSkills(skills):
    jsonSkillsArr = convertToJson(skills)
    sum = 0
    
    for elem in jsonSkillsArr:
        sum += elem['level']
    return sum
        
        
        
        
        
        
        
        
        
        
        
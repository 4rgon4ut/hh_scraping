import csv
from operator import itemgetter
import pandas as pd
import re

skills_count = 0
stats = {}
salary_list = []
with open('data.csv', newline='') as data:
    reader = csv.reader(data, delimiter='"')
    for row in reader:
        if len(row) > 2:
            skills = row[0]
            salary = re.findall(r'\d+.\d+', row[1])
            salary = [int(re.sub(r'\xa0', '', item)) for item in salary]
            salary_list.extend(salary)
            for element in skills.split(','):
                if len(element) > 1:
                    skills_count += 1
                    if element in stats:
                        stats[element] += 1
                    else:
                        stats[element] = 1


mean_salary = sum(salary_list) / len(salary_list)
stats = sorted(stats.items(), key=itemgetter(1), reverse=True)
persent_list = [((k[1] / skills_count) * 100).__round__() for k in stats]
skills_tablet = pd.DataFrame(list(zip(stats, persent_list)), columns=['Skills', '%'])

print(skills_tablet.head(10))
print('-------------------------------')
print('Mean salary(rub) : ', mean_salary.__round__())

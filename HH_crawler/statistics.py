# This module is for calculating and analysing scraped data.

import csv
import re
import collections

import pandas as pd


def analyse_data(filename):
    with open(filename, newline='') as data:
        reader = csv.reader(data, delimiter='"')
        for row in reader:
            if len(row) > 2:
                salary_items = re.findall(r'\d+.\d+', row[1])
                salary = [int(re.sub(r'\xa0', '', i)) for i in salary_items]
                salary_list.extend(salary)
                skills = row[0].split(',')
                skills.remove('')
                yield skills
        return salary_list


salary_list = []
file_name = 'data.csv'
skills_list = []
for ele in analyse_data(file_name):
    skills_list.extend(ele)

skills_numbers = collections.Counter(skills_list)
skills_sum = sum(skills_numbers.values())
top_skills = skills_numbers.most_common(10)
persent_list = [(k[1] / skills_sum * 100).__round__() for k in top_skills]
mean_salary = (sum(salary_list) / len(salary_list)).__round__()
stats_table = pd.DataFrame({'Skills, amount': top_skills, '%': persent_list})

print(stats_table)
print('------------------------------')
print('Mean salary(rub) : ', mean_salary)

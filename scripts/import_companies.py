import csv
import sys
from internships.models import Company, Link

if __name__ == '__main__':
    with open(sys.argv[0], 'r') as company_list:
        company_reader = csv.reader(company_list, delimiter=',')
        for name, url in company_reader:
            c = Company(name=name)
            c.save()
            l = Link(url_type='internship', url=url, company=c)
            l.save()

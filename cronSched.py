from crontab import CronTab

crn = CronTab()

job = crn.new(command = 'python buster.py')
for job in crn:
	print(job)
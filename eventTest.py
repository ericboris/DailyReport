from testEvent import event

event = event["items"][0]

name = event.get("id")
tasks = event.get("description")
location = event.get("location")
start = event.get("start")
end = event.get("end")

tasks = [name, tasks, location, start, end]	
for i in tasks:
	print i, "\n"

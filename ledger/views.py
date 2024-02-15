from django.shortcuts import render
# Create your views here.
	
def task_list(request):
	ctx = {
		"tasks": [
			"Task 1",
			"Task 2",
			"Task 3",
			"Task 4"
		]
	}
	return render(request, 'task_list.html', ctx)
# Create your views here.

from django.shortcuts import render

def test(request):
	context = {}
	template = "test.html"
	return render(request, template, context)
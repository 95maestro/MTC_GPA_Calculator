from django.shortcuts import render, redirect
from .models import Course
def index(request):
    courses = Course.objects.all()
    total_points = sum(c.credits * float(c.grade_point) for c in courses)
    total_credits = sum(c.credits for c in courses)
    gpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0
    if request.method == "POST":
        if 'clear' in request.POST:
            Course.objects.all().delete()
            return redirect('index')
        Course.objects.create(
            name=request.POST['name'],
            credits=int(request.POST['credits']),
            grade_point=request.POST['grade']
        )
        return redirect('index')
    return render(request, 'calculator/index.html', {'courses': courses, 'gpa': gpa})
from .models import Issue
obj= Issue.objects.all();
for ob in obj:
    print (ob.student_id);
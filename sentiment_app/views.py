from django.shortcuts import render
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == "POST":
        print("POST request received")
        form = FeedbackForm(request.POST)
        print("Form data:", form.data)
        if form.is_valid():
            print("Form is valid. Saving...")
            feedback = form.save()
            print("Saved Feedback:", feedback.text, feedback.sentiment)
            return render(request, 'feedback.html', {'feedback': feedback})
        else:
            print("Form is invalid:", form.errors)
    else:
        form = FeedbackForm() 
        print('hey')
        print('back')
        print("GET request — showing blank form")
    return render(request, 'feedback_form.html', {'form': form})
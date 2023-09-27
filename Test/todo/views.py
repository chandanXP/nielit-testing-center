from django.shortcuts import render, redirect
# from .models import Todo
from .forms import CSVUploadForm
from .models import Question
import csv
from .forms import SubjectForm
from .forms import TestForm
from .models import Test
from .models import Response


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            for row in csv_data:
                Question.objects.create(sub_code=row[0], test_code=row[1], question=row[2],
                                        img_link=row[3], option_1=row[4], option_2=row[5],
                                        option_3=row[6], option_4=row[7], answer=row[8]
                                        )
            return redirect('/')  # Redirect to a success page
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/')  # Redirect to a success page
    else:
        form = SubjectForm()

    return render(request, 'add_subject.html', {'form': form})


def fetch_subject_detail(request, subject_code):
    # Retrieve data from the Question and Test models based on subject_code
    questions = Question.objects.filter(sub_code=subject_code)
    test_info = Test.objects.filter(subject_code=subject_code).first()

    context = {
        'questions': questions,
        'test_info': test_info,
    }

    return render(request, 'test_page.html', context)


def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the home page or any other page you prefer
    else:
        form = TestForm()

    return render(request, 'create_test.html', {'form': form})


def running_test(request):
    # Retrieve data from the Test model
    test_data = Test.objects.all()  # You can use filter() or other query methods if needed

    # Pass the data to the template
    return render(request, 'running_tests.html', {'test_data': test_data})


def evaluate_responses():
    # Get all responses from the Response model
    responses = Response.objects.all()

    # Create a dictionary to store the results
    evaluation_dict = {}

    for response in responses:
        # Get the corresponding question for each response
        try:
            question = Question.objects.get(id=response.question_id)
        except Question.DoesNotExist:
            # Handle the case where the question doesn't exist (question_id is not valid)
            continue

        # Check if the selected option matches the correct answer
        is_correct = response.selected_option == question.answer

        # Store "True" or "False" in the evaluation dictionary based on correctness
        evaluation_dict[response.id] = is_correct

    return evaluation_dict


def submit_test(request):
    if request.method == 'POST':
        response_dict = {}
        for key, value in request.POST.items():
            if key.startswith('options_'):
                question_id = key.split('_')[1]  # Extract the question ID from the field name
                response_dict[question_id] = value

                # Create a Response instance and save it to the database
                response = Response(question_id=question_id, selected_option=value)
                response.save()

        # Call the evaluate_responses function to get the evaluation dictionary
        evaluation_dict = evaluate_responses()

        # Pass both the response and evaluation dictionaries to the HTML page
        context = {
            'response_dict': response_dict,
            'evaluation_dict': evaluation_dict,
        }

        return render(request, 'dump.html', context)

    # Handle GET request (displaying the form)
    questions = [...]  # Fetch questions from your data source
    return render(request, 'dump.html', {'questions': questions})





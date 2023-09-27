from djongo import models


class Subject(models.Model):
    sub_code = models.IntegerField(unique=True)
    sub_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sub_name


class Question(models.Model):
    sub_code = models.IntegerField()
    test_code = models.IntegerField()
    question = models.CharField(max_length=255)
    img_link = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=1,
                              choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')]
                              )

    def __str__(self):
        return self.question


class Test(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=100)
    num_questions = models.IntegerField()
    test_duration = models.DateTimeField()
    start_time = models.DateTimeField()

    def __str__(self):
        return self.subject_name


class Response(models.Model):
    question_id = models.IntegerField(default=-1)  # Set a default value like -1 for cases with no specific question
    selected_option = models.CharField(max_length=255)

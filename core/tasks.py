from celery.task import task

@task
def test_multiply(x, y):
        multiplication = x * y
        return "The result is " + str(multiplication)
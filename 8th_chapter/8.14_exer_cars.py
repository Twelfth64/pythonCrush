
def make_car(producer, model, **kwargs):

    kwargs['producer'] = producer
    kwargs['model'] = model
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
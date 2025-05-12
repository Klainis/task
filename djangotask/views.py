from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


@csrf_exempt
def add_user(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_user(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def authorise(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_vacancy(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_vacancy(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_vacancy(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_skill(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_skill(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill_to_vacancy(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def remove_skill_from_vacancy(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill_to_user(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def remove_skill_from_user(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_response(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_response(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_response(request):
    try:
        raise NotImplementedError
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


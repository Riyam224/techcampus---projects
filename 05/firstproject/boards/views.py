from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.


# ! show info from database on the page
def index(request):
    boards = Board.objects.all()

    # boards_names = list()
    # for board in boards:
    #     boards_names.append(board.name)
    # res_response = '<br>'.join(boards_names)
    # return HttpResponse(res_response)

    # ! for render the html page
    return render(request, 'home.html', {'boards': boards})


def boards_topic(request, id):
    board = Board.objects.get(pk=id)

    return render(request, 'topics.html', {'board': board})

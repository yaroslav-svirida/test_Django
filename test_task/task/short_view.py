from rest_framework.response import Response
from rest_framework.views import APIView

from .models import  *
from .serializers import ShortSerializer

import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox
import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox


class ShortView(APIView):

    def get(self, request):
        user_id = request.user.id
        users_short_url = Url.objects.filter(user_id=user_id)
        users_short_url_serialized = ShortSerializer(users_short_url,many=True).data
        return Response(users_short_url_serialized)




def short():
    s = pyshorteners.Shortener()
    shor = beforeLink.get()
    afterLink.delete(0, END)
    k = s.tinyurl.short(shor)

    Url.objects.create(long_url=shor, user_id=3, short_url=k)
    afterLink.insert(0, k)




root = Tk()
root.title('Сократитель ссылок')
root.geometry('400x150')
root.resizable(width=False, height=False)

beforeLinkLabel = Label(root, text='Оставьте сылку')
beforeLinkLabel.place(x=10, y=10)

beforeLink = ttk.Entry(root, width=40, font='Arial 13')
beforeLink.place(x=10, y=30)

btn = ttk.Button(root, text='Сократить', command=short)
btn.place(relx=0.5, y=80, anchor=CENTER)

afterLinkLabel = Label(root, text='Результат')
afterLinkLabel.place(x=10, y=105)

afterLink = ttk.Entry(root, width=40, font='Arial 13')
afterLink.place(x=10, y=105)

root.mainloop()



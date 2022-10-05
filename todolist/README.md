 # Tugas 4 PBP
 - Nama   : Rizka Nisrina Nabila
 - NPM    : 2106653344
 - Kelas  : PBP - B
 
 # Link: https://tugas2rizka.herokuapp.com/todolist/
 
 ## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} berguna untuk (menangani threats berupa CSRF) menjamin keamanan user dan site agar tidak terkena serangan dari pihak eksternal. Selain itu Django mengharuskan adanya token tersebut pada pembuatan form. Kode Ini dibuat untuk memberikan proteksi form yang ada di database. Apabila potongan code ini tidak ada, maka saat ada form eksternal masuk yang mana form ini bukan seharusnya. Saat kita run aplikasi, akan muncul verification failed dan request tidak bisa diproses. Melalui code ini token akan dicek oleh fungsi views yang menangani action. Apabila valid, maka akan dikirim ke server, jika tidak, maka tidak akan diproses. 
 
 ## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
 Ya. Jika membuat form sebagai object kemudian mengisi input fields secara manual pada HTML, maka form dapat dibuat. form dapat dibuat secara manual tanpa menggunakan built-in methods, yaitu dengan mengedit konten html menggunakan CSS. Sehingga, untuk mengakses atribut di models satu-satu dengan form pada section masing-masing. Seperti pada atribut di todolist, maka akan diakses form.title, form.description, dst.

 ## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
  User melakukan request pada browser. Lalu, browser akan meresponse dengan mengirm POST ke server saat user membuat request dengan cara menekan button login, register, create task. Kemudian akan terdapat perubahan pada server dengan adanya event POST. Setelah itu views.py akan merespon dengan mereturn atau mengupdate data dengan melakukan user redirect ke views sebelumnya sehingga tampilan akan mengupdate data baru.

 ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  - Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya. Dengan menjalankan perintah python manage.py startapp todolist

  - Mendaftarkan aplikasi ke dalam INSTALLED_APPS di file settings.py
INSTALLED_APPS = [
.....,
.....,
'todolist',
]

- Buat model dalam file models.py pada folder todolist dengan variabel:
from django.db import models
from django.contrib.auth.models import User

class todolistItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    done = models.BooleanField(default=False)

- Menjalankan perintah
python manage.py makemigrations
python manage.py migrate

- Membuat fungsi-fungsi yang dibutuhkan pada views.py:
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    ......
def register(request):
    ......
def login_user(request):
    ......
def logout_user(request):
    ......
def create_task(request):
    ......
def delete(request, title):
    ......
def done(request, id):
    ......

- Membuat folder template di dalam folder todolist berisi file-file html yang dibutuhkan menampilkan data
createtask.html
login.html
register.html
todolist.html

- Tambahkan path url dengan membuat file urls.py di dalam folder todolist dan isi dengan path untuk melakukan routing ke fungsi-fungsi yang ada fi views.py

from django.urls import path
from todolist.views import delete, register, login_user, logout_user, create_task, delete, done

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),
    path('delete/<int:id>/', delete, name='delete'),
    path('done/<int:id>/', done, name='done'),
    
]

- Daftarkan app todolist ke dalam url pattern pada file urls.py di folder project_django

urlpatterns = [
.........,
path('todolist/', include('todolist.urls')),
.........,
]

- Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat

- Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

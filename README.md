# Nama  : Rizka Nisrina Nabila
# NPM   : 2106653344
# Kelas : PBP - B


# Link git hub : https://tugas2rizka.herokuapp.com/katalog/

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![PBP](https://user-images.githubusercontent.com/101660408/190176972-d1740021-16dc-45f6-b930-5bf73afcc001.png)

# Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment memiliki kegunaan untuk memisahkan pengaturan dan *package* yang diinstal pada setiap proyek supaya terisolasi. Hal ini dilakukan agar kita tetap dapat mengerjakan beberapa proyek dengan modul yang sama namun dengan versi berbeda. Sebagai contoh, misalnya kita membuat proyek Django dengan versi 1.1 dan proyek aplikasi kita dapat berjalan dengan baik pada modul versi 1.1 ini. Lalu, selang beberapa waktu kemudian, Django merilis versi baru yang dimana versi baru ini dibutuhkan untuk membuat proyek yang lain. Setelah upgrade ke versi yang baru, proyek kita sebelumnya yang menggunakan versi lama ternyata tidak dapat berjalan pada versi baru ini. Untuk itu, kita membutuhkan *virtual environment* agar setiap aplikasi mempunyai modulnya masing-masing.

Lalu, apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? Ya bisa, tetapi hal ini menyebabkan modul-modulnya dapat diakses dari luar sehingga semua aplikasi bisa mengakses dan menggunakannya.

# Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]

Bagian urls yang berada pada folder katalog tersebut, digunakan untuk melakukan routing terhadap fungsi views yang telah dibuat, nantinya akan dirender untuk mapping melalui file HTML di templates sehingga dapat ditampilkan lewat browser.

from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_catalog,
        'nama': 'Nabila',
        'npm' : '2106653344'
    }
    print(data_catalog)
    return render(request, "katalog.html", context)

Pada bagian fungsi views diatas berfungsi untuk memanggil query melalui models ke database. Ketika data telah diperoleh akan dirender di views dengan fungsi di atas.

from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()

Pada models tersebut terdapat CatalogItem isinya merupakan nama-nama, ataupun harga, stok, deskripsi, dan lain-lain yang nantinya akan dipakai pada saat html untuk dipanggil beserta isinya. Data ini di akses dari database.

    {% for data in list_katalog %}
    <tr>
        <th>{{data.item_name}}</th>
        <th>{{data.item_price}}</th>
        <th>{{data.item_stock}}</th>
        <th>{{data.rating}}</th>
        <th>{{data.description}}</th>
        <th>{{data.item_url}}</th>
    </tr>
{% endfor %}

Pada html ini melakukan mapping, iterasi terjadi terhadap variabel list_katalog yang telah dibuat pada views didalam CatalogItem dan juga melakukan pemanggilan nama ataupun variabel spesifik dari objek yang dibuat untuk mendapatkan data dari objek tersebut. Iterasi ini adalah untuk menampilkan di web HTMLnya nanti.

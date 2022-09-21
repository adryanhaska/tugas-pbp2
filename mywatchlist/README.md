---
sidebar_label: Tugas 3
---

# Tugas 2: Pengimplementasian Data Delivery Menggunakan Django

Nama : Muhammad Adryan Haska Putra

NPM  : 2106750641

aplikasi heroku  : 
[mywatchlist HTML](https://tugas2-pbp-adryan.herokuapp.com/mywatchlist/html)
[mywatchlist XML](https://tugas2-pbp-adryan.herokuapp.com/mywatchlist/XML/)
[mywatchlist JSON](https://tugas2-pbp-adryan.herokuapp.com/mywatchlist/JSON)
---

## Checklist

### Jelaskan perbedaan antara JSON, XML, dan HTML!
#### HTML
HTML atau HyperText Markup Language merupakan sebuah markup languange yang digunakan untuk membuat halaman web, bahasa markup membuat teks lebih interaktif dan dinamis. Hypertext mendefinisikan link antar halaman web. Bahasa markup digunakan untuk mendefinisikan dokumen teks di dalam tag yang mendefinisikan struktur halaman web.

### XML
XML atau eXtensible Markup Language. merupakan sebuah markup languange yang juga digunakan untuk membuat halama web, namun bahasa ini adalah bahasa dinamis yang digunakan untuk mengangkut data bukan untuk menampilkan data. Tujuan desain XML berfokus pada kesederhaan, Desain XML biasanya berfokus pada dokumen.

### JSON
JSON atau JavaScript Object Notation merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Biasanya, file JSON berisikan teks dan file berekstensi .json. JSON ini berbeda dengan XML namun keduanya memiliki fungsi yang serupa.

### Perbedaan
- Elemen, JSON menyimpan elemen secara efisien, namun tidak rapi untuk dilihat. sedangkan XML menyimpan elemen secara tidak efisien namun lebih mudah dibaca
- Ekstensi, JSON memiliki ekstensi `.JSON`, XML memiliki ekstensi `.XML`, HTML memiliki ekstensi `.HTML`
- Penerapan, JSON mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam mengembangkan sebuah aplikasi berbasis platform, terkadang kita memerlukan pengiriman dari stack satu ke stack lainnya, maka diperlukan sebuah data delivery untuk menghubungkan stack stack tersebut dan bermanfaat pengorganisasian data, kolaborasi dan lainnya. beberapa contoh data delevery yang umum digunakan adalah HTML, XML, JSON

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 3 di atas.
1.  membuat aplikasi baru bernama `mywatchlist` dengan menjalankan perintah `python manage.py startapp mywatchlist`

2. membuat sebuah routing di `urls.py` untuk memetakan fungsi yang telah dibuat pada `views.py`, import `show_mywatchlist` dari `views` kemudian buat variabel `app_name` dengan value `mywatchlist`, dan buat list `urlpatterns` yang berisikan `path`
mywatchlist/urls.py
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]
```

mywatchlist/views.py
```
...
def show_mywatchlist(request):
    return render(request, "mywatchlist.html")
...
```

project_django/settings.py
```
INSTALLED_APPS = [
    ...
    'mywatchlist',
]

```

prodject_django/urls.py
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

3. Buat sebuah model MyWatchList yang atributnya sesuai
```
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=120)
    rating = models.FloatField()
    release_date = models.CharField(max_length=120)
    review = models.TextField()
```

## Screenshot Postman
### HTML
[![Screen-Shot-html.png](https://i.postimg.cc/wvKCJn4D/Screen-Shot-2022-09-21-at-22-20-29.png)](https://postimg.cc/Ny4CvCc0)

### XML
[![Screen-Shot-xml.png](https://i.postimg.cc/QNKqvHtN/Screen-Shot-2022-09-21-at-22-21-26.png)](https://postimg.cc/G9rYy3G6)

### JSON
[![Screen-Shot-json.png](https://i.postimg.cc/br1krSDQ/Screen-Shot-2022-09-21-at-22-21-37.png)](https://postimg.cc/8fPjn5b5)

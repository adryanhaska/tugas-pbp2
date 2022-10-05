---
sidebar_label: Tugas 4
---

# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama : Muhammad Adryan Haska Putra

NPM  : 2106750641

aplikasi heroku  : 

[todolist](https://tes-tugas-pbp.herokuapp.com/todolist)

[todolist login](https://tes-tugas-pbp.herokuapp.com/todolist/login)

[todolist register](https://tes-tugas-pbp.herokuapp.com/todolist/register)

---


## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF (Cross-Site Request Forgery) merupakan sebuah serangan yang umum dilakukan untuk melakukan subuah tindakan yang tidak diinginkan pada halaman yang telah terauntentifikasi, dengan menggunakan csrf token, maka HTTP request akan di validasi terlebih dahulu. apabila request tersebut memiliki token yang valid, maka request tersebut baru akan diproses.

apabila potongan kode tersebut tidak ada pada elemen `<form>` , request yang dikirimkan akan dianggap sebagai request yang tidak valid dengan mengirimkan error 403 Forbidden.
---

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Ya, kita tetap dapat membuat elemen `<form>` secara manual tanpa menggunaka generator, namun kita perlu menambhakan inputnya secara manual.

untuk membuat `<form>` secara manual, kita bisa menggunakan tag `<form>` pada `template.html` , gunakan method `POST`, lalu tambahkan input, contohnya seperti berikut :
```
...
<form action = "" method = "post">
    {% csrf_token %}
    {{form }}
    <input type="submit" value=Submit">
</form>
...
```
setelah itu, buat views dari input yang didapat
---

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
data yang di input akan diterima oleh `<fomr>`. kemudian setelah user melakukan trigger dengan tombol atau cara yang lain, client akan mengirimkan POST request, setelah request itu diterima maka views yang sesuai akan melakukan handle. setelah itu, views akan melakukan render terhadap data yang telah di handle.

---

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django dengan menjalankan `python manage.py startapp todolist`

2. Menambahkan path `todolist` sehingga dapat diakses dengan menambahkannya di `settings.py` dan `urls.py` pada folder `prodject_django`
    ```
    INSTALLED_APPS = [
        ...
        'todolist',
    ]
    ```
    ```
    urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
    ```

3. implementasi model `Task` sesuai spesifikasi yang diinginkan
    ```
    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now_add=True)
        title = models.TextField(max_length=100)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```

4. Jalankan `python manage.py makemigrations` dan `python manage.py migrate`

5. Buat `forms.py` untuk membuat form yang akan digunakan
    ```
    from django import forms

    class TaskForm(forms.Form):
        title = forms.CharField()
        description = forms.CharField()
    ```

6. buat template yang berisikan `html` yang diperlukan serta tambahkan juga fungsi fusngi yang sesuai pada `views.py` terhadap tempalat tersebut. beberapa fungsi yang diperlukan:
- show_todolist : mengambil data pada `Task` lalu menampilkannya dalam bentuk tabel
- register : mendaftar user melalui form
- login_user : melakukan auntentifikasi dengan username dan password yang telah di register
- logout_user : melakukan logout user , membuatnya tidak dapat mengakses halaman yang membutuhkan auntentifikasi
- create_task : menampilkan form untuk membuat task baru
- done_task : mengubah status dari `belum selesai` menjadi `selesai`
- not_done_task : mengubah status dair `selesa`i menjadi `belum selesai`
- delete : menghapus task yang ada

7. buat routing yang dibutuhkan pada `urls.py`
    ```
    from django.urls import path
    from todolist.views import *

    app_name = "todolist"

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('login/', login_user, name='login'),
        path('register/', register, name="register"),
        path('create-task/', create_task, name="create_task"),
        path('logout/', logout_user, name="logout"),
        path('done/<int:id>', done_task, name='done_task'),
        path('not_done/<int:id>', not_done_task, name='not_done_task'),
        path('delete/<int:id>', delete_task, name='delete_task'),
    ]
    ```

8. lakukan `add`, `commit`, dan `push` untuk mendeploy ke heroku.

9. tambahkan dua akun pengguna dan tiga dummy data menggunakan model `Task` pada akun masing-masing di situs web Heroku.



---
---
---


# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
<br>

### __1. Inline CSS__
merupakan cara penulisan langsung kode css pada pada atribut elemen HTML, contohnya sebagai berikut:

```
...
<p style="color:white;">lorem impsum</p>
...
```
__kelebihan__ : penggunaan sangat cepat dan mudah sehingga sangat baik digunakan ketika ingin melakukan pengujian terhadap kode css yang akan digunakan.

__kekurangan__ : penggunaannya tidak efisie karena hanya diterpkan pada satu elemen, dan membuat strukstur HTML berantakan
<br>

### __2. Internal CSS__
merupakan cara penulisan CSS dengan menulisnya pada tag  `< style>` dituliskan di bagian header pada file HTML. contoh implementasinya:
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: red;
}
h1 {
    color: black;
    padding: 50px;
} 
</style>
</head>
<body>

<h1>lorem ipsum</h1>
<p>lorem ipsum.</p>

</body>
</html>
```

__kelebihan__ : perubahan yang terjadi hanya berdampak pada satu halaman saja, kita juga tidak perlu melakukan upload file CSS karena kode CSS sudah ada pada file HTML. dapat menggunakan selektor ID dan CLASS
__kekurangan__ : tidak efisien apabila ingin menggunakan style yang sama di file yang berbeda, selain itu panambahan CSS langsung di file HTML dapat memperlambat performa website.
<br>

### __3. Eksternal CSS__
merupakan cara penulisan CSS pada file terpisah dari file HTML. kode CSS di tulis pada file khusus berekstensi `.css`.
referensi file dituliskan pada bagian header di file HTML. contoh penggunaanya sebagai berikut:
<br>

`.css` file
```
.classA {
   float: left;
   width: 40%;
   background:#347545;
}
.classB {
   float: left;
   width: 20%;
   background:#c47cb5;
}
```

`.html` file
```
...
<head>
    <link rel="stylesheet" type="text/css" href="style.css" />
</head>
...
```

__kelebihan__ : ukuran file HTML lebih kecil sehingga waktu loading menjadi cepat. kode pada file HTML juga terlihat lebih rapih. file CSS dapat digunakan pada beberapa file sekaligus.
__kekurangan__ : halaman mungkin akan menjadi berantakan ketika file CSS belum di-load secara sempurna. uploading file CSS bisa memperlambat waktu pengaksesan halaman.
<br>
 
--- 
## Jelaskan tag HTML5 yang kamu ketahui.
`<a>` : tag untuk mendefinisikan hyperlink \
`<b>` : menampilkan teks dengan format bold \
`<body>` : mendefinisikan body atau isi dari html \
`<button>` : membuat button yang dapat melakukan suatu tindakajn tertetu \
`<div>` : membagi sekumpulan kode pada file html \
`<form>` : html tag untuk menerima form atau masukan dari user\
`<head>` : merupakan bagian awal file html, biasanya tempat dimasukan file file pendukung seperti css\
`<h1>` - `<h6>` : html heading teks\
`<i>` : meampilkan teks dengan format italic\
`<img>` : menampilkan image di html\
`<input>` : tag untuk meminta input dari user\
`<li>` : list item\
`<p>` : menampilkan paragraf di html\
`<script>` : memasukan script yang akan digunakan pada file html\
`<styke>` : menambahkan style atau design di file hmtl\
`<table>` : tag untuk membuat table di hmtl\
`<td>` : cell di table html\
`<th>` : heade cell di table html\
`<tr>` : row di table html\
`<u>` : menampilkan teks dengan format underline\
`<ul>`: menampilkan unordered list



---
## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. element selector : selector yang menunjuk salah satu elemen tertentu, contoh
```
p {
  text-align: center;
  color: black;
}
```

2. class selector : selector yang menunjuk salah satu class tertentu, contoh
```
.class-name {
  text-align: center;
  color: red;
}
```
3. id selector : selector yang menunjuk salah satu id tertentu, contoh
```
#id1 {
  text-align: center;
  color: blue;
}
```
4. universal selector : selector yang menunjuk seluruh elemen di html, contoh
```
* {
  text-align: center;
  color: grey;
}
```

5. gruping selector : selector yang menunjuk beberapa elemen,class, atau id tertentu, contoh
```
h1, h2, p {
  text-align: center;
  color: black;
}
```
---
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. kustomisasi halaman login, register, dan create-task menggunakan bootstrap. untuk menggunakannya kita harus manambahkan bootstrap di tamplate.
`base.html`
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  {% block meta %}
  {% endblock meta %}
</head>

<body>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js" integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous"></script>
  {% block content %}
  {% endblock content %}
</body>

</html>
```

2. kustomisasi halaman todolist menggunakan card yang ada di bootstrap tambahkan juga navbar di halaman tersebut.
navbar
```
<nav class="navbar bg-light title">
  <form class="container-fluid form-inline">
    <a class="navbar-brand">{{user}}</a>
    <button class="btn btn-danger" type="button">
      <a href="{% url 'todolist:logout' %}" class="link">Logout</a>
    </button>
  </form>
  <br />
</nav>
```

card
```
...
<div class="card" style="width: 50%">
    <div class="card-body">
      <h5 class="card-title">{{task.title}}</h5>
      <p class="card-text">{{task.description}}</p>
...
```

3. buat halaman menjadi responsive dengan Media Query
```
@media screen and (max-width: 845px) {
    .column {
      width: 100%;
      text-align: center;
    }
}
```
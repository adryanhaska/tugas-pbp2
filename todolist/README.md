---
sidebar_label: Tugas 4
---

# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama : Muhammad Adryan Haska Putra

NPM  : 2106750641

aplikasi heroku  : 

[todolist](https://tugas2-pbp-adryan.herokuapp.com/todolist)

[todolist login](https://tugas2-pbp-adryan.herokuapp.com/todolist/login)

[todolist register](https://tugas2-pbp-adryan.herokuapp.com/todolist/register)

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
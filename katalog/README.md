---
sidebar_label: Tugas 2
---

# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Nama : Muhammad Adryan Haska Putra
NPM  : 2106750641

aplikasi heroku  : https://tugas2-pbp-adryan.herokuapp.com/katalog/
---

## Pertanyaan

### Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`; 
![bagan](https://i.postimg.cc/Bn2QRR9P/Screen-Shot-2022-09-14-at-23-12-59.png)

### Jelaskan kenapa menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Virtual environment (Linkungan virtual) adalah environment yang digunakan oleh Django untuk menjalankan aplikasi, Virtual environment memungkinkan kita untuk memisahkan atau mengisolasi pengaturan dan package yang diinstall pada setiap projek Django sehingga perubahan yang dilakukan pada satu projek tidak akan memengaruhi projek lainnya, sehingga penggunaan virtual environment sangan disarankan.

Kita tetep dapat membuat aplikasi web berbasi Django tanpa menggunakan virtual environment, namun penggunaan virtual environtment lebih disarakan oleh Django, selain itu tanpa menggunakan virtual environtment kita mungkin akan menemukan masalah baru seperti perizinan saat melakukan install suatu software.

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1.  membuat fungsi `show-katalog` yang meng-import `CatalogItem` dari models, lalu buat dictionary `context` berisikan pasangan key dan value dari `list_katalog`, dan mengemabalikan `render(request, "katalog.html", context)`
```
def show_katalog(request):

    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Muhammad Adryan Haska Putra',
    'npm': '2106750641',
    }

    return render(request, "katalog.html", context)
```

2. membuat sebuah routing di `urls.py` untuk memetakan fungsi yang telah dibuat pada `views.py`, import `show_katalog` dari `views` kemudian buat variabel `app_name` dengan value `katalog`, dan buat list `urlpatterns` yang berisikan `path`
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template, gunakan syntax Django `{{}}` untuk melakukan mapping, ubah `Fill me!` pada tamplate, 
```
...
<h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{npm}}</p>
...
```
kemudian lakukan render dengan loop setiap katalog di `list_kalaog`
```
...
   {% for katalog in list_katalog %}
    <tr>
        <td>{{katalog.item_name}}</td>
        <td>{{katalog.item_price}}</td>
        <td>{{katalog.item_stock}}</td>
        <td>{{katalog.rating}}</td>
        <td>{{katalog.description}}</td>
        <td>{{katalog.item_url}}</td>
    </tr>
    {% endfor %}
...
```

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- lakukan `add` , `commit`, dan `push` ke GitHub
- buat aplikasi di heroku lalu sambungkan dengan GitHub
- tambahkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` di `repository secret` pada repositori GitHub
- simpan variabel - variabel tersebut
- buka GitHub actions dan jalankan workflow, lalu akses aplikasi heroku di browser.


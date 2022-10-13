---
sidebar_label: Tugas 6
---

# Tugas 6: Javascript dan AJAX

Nama : Muhammad Adryan Haska Putra

NPM  : 2106750641

---

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
asynchronous  | synchronous
------------- | -------------
program berjalan secara parallel  | Program berjalan pada satu waktu
Dapat mengirim banyak request sekaligus  | Hanya mengirim satu request pada satu waktu
mengingkatkan performa karena program berjalan bersamaan | lebih lambat karena program haris dijalankan satu satu

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah salah satu teknik pemgrograman untuk melakukan suatu respon dari tindakan yang dilakukan user atau system.
Contoh penerapannya dalama tugas ini misalnya ketika user menekan tombol tambah taska, maka modal untuk mengisi task baru akan keluar. begitu juga tombol tombol yang lain,

## Jelaskan penerapan asynchronous programming pada AJAX.
Dalam menerapkan asynchronous programming, AJAX memungkinkan untuk menjalankan atau menerima request tanpa memengaruhi halaman web yang dijalankan. artinya browser tidak perlu me-load ulang keseluruhan isi halamannya. hal ini dapat dilakukan karena AJAX dapat melakukan eksekusi langsung tanpa menunggu balasan dari server terlebih dahulu. dimana konsep tersebut sesuai dengan penerapan asynchronous programming

 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. buat path `todolist/json` dan views yang sesuai untuk mengakses data dengan format json untuk ditampilkan dalam halaman utama.
```
  $(document).ready(function () {
    $(".modal").hide();
    $(".backdrop").hide();
    $.get("/todolist/json/", function (data, status) {
      show(data);
    });
  });
```
2. lakukan pengambilan data dengan AJAX get
3. buat tombol `add task`, dan buat fungsi yang menhandlenya
```
$(document).ready(function () {
    $(".add-task").click(function () {
      $(".modal").toggle();
      $(".backdrop").toggle();
    });
  });
```
4. tambahkan view baru untuk menambhakan task
5. buat path `todolist/add` mengarahkan view yang sebelumnya dibuat
```
urlpatterns = [
    ...
    path('add/', add_todolist_item, name='add_todolist_item')
]
```
6. tutup modal saat tas berhasil ditambahkan
```
// saat berhasil
  ...
        function () {
          $(".modal").hide();
          $(".backdrop").hide();
          $.get("/todolist/json/", function (data, status) {
            show(data);
          });
 ...
```
7. refresh page tanpa mereload keseluruhan page 


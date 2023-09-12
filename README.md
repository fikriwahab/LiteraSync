# Tugas 2 PBP
# Deskripsi LiteraSync
LiteraSync merupakan sebuah portal online yang menyediakan database untuk pencarian buku pada sebuah perpustakaan ataupun toko buku. Melalui aplikasi ini, baik customer dan seller dapat mencari buku dengan rincian stock, deskripsi, serta pengelolaan inventaris buku.

## Link Akses Adaptable.io:
https://literasync.adaptable.app/main/

## Implementasi checklist secara step-by-step:
### 1. Membuat sebuah proyek Django baru
Sebelum saya membuat proyek Django baru, saya perlu melakukan beberapa hal, seperti membuat direktori yang saya inginkan, menambahkan inisiasi git pada repositori tersebut. Kemudian saya lanjutkan dengan membuka Command Prompt dalam direktori yang sebelumnya saya namai LiteraSync, kemudian saya membuat virtual environtment dengan mengetik "python -m venv env" dan mengaktivkannya dengan mengetik "env\Scripts\activate.bat". Setelah itu, barulah saya tambahkan requirements.txt beserta beberapa dependencies. Setelah dependencies terpasang, maka saya lakukan perintah "pip install -r requirements.txt" dan membuat proyek Django bernama LiteraSync dengan "django-admin startproject LiteraSync .".
### 2.  Pembuatan Aplikasi main
Terlebih dahulu saya jalankan perintah "python manage.py startapp main", dan memastikan bahwa env tetap aktif, kemudian pada file settings.py ditambahkan 'main' pada Variabel INSTALLED_APPS, kemudian membentuk sebuah direktori dalam LiteraSync yang dinamai templates. Di dalamnya, saya tambahkan file main.html yang memuat representasi visual yang terdiri atas tabel yang menampilkan setiap item dari Item yang kita definisikan yang mencakup atribut name, amount, dan description. Selain itu saya juga menambahkan fitur search item (yang seharusnya dapat diintegrasikan dengan sebuah database), namun di sini saya membuat database temporer pada variabel 'books'. Variabel tersebut mencakup array dari berbagai judul buku. Saat pengguna mengetikkan sebuah judul pada serach bar, maka fungsi 'showSuggestions(str) dipanggil. Untuk kedepannya mungkin dapat saya manfaatkan pengintegrasian dengan API yang mengambil data dari database yang real-time.
### 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Beberapa fungsi dan modul perlu diimpor untuk proses routing di urls.py, kemudian rute baru ditambahkan pada variabel 'url patterns' yang langsung meredirect ke aplikasi 'main' yang telah dibuat. Dan pada akhirnya pengguna akan mengakses nedpoint'/items/'.
### 4. Membuat model Item
Dengan memanfaatkan pola desain MVT, "model" merepresentasikan struktur atau susunan data. Hal ini memungkinkan kita untuk menyimpan data, mendefinisikan data, serta melakukan operasi database seperti Query. Model ini diinterpretasikan menjadi sebuah tabel di database yang mencakup kode berikut:

    from django.db import models
    class Item(models.Model):
        name = models.CharField(max_length=200, verbose_name="Nama Buku")
        amount = models.IntegerField(verbose_name="Jumlah")
        description = models.TextField(verbose_name="Deskripsi")
    
        def __str__(self):
            return self.name
name adalah atribut yang akan menyimpan nama item, dengan tipe data karakter dan panjang maksimum 200 karakter.
amount adalah atribut dengan tipe data integer, yang menyimpan jumlah item.
description adalah sebuah teks area yang bisa digunakan untuk menyimpan deskripsi lebih panjang tentang item.
Fungsi __str__() sederhana yang didefinisikan di bawahnya digunakan untuk merepresentasikan objek model saat ditampilkan, dalam hal ini kita memilih untuk menampilkan nama item.
### 5. Membuat model Item
#### Mendefinisikan Fungsi Tampilan:
Di dalam file views.py aplikasi main, saya mendefinisikan sebuah fungsi dengan nama display_items.

#### Integrasi dengan Model Item:
Di dalam fungsi tersebut, saya menggunakan perintah Django untuk mengambil semua entri yang ada di model Item. Ini memungkinkan kita untuk mengakses setiap item yang ada di dalam database kita.

#### Mengirim Data ke Template:
Kemudian, saya mengirimkan data item tersebut ke sebuah template HTML dengan menggunakan konteks. Konteks ini akan memudahkan kita dalam menampilkan setiap entri item pada halaman web kita.

### 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
#### Menambahkan URL Baru:
Di dalam file urls.py yang berada di aplikasi main, saya menambahkan sebuah path baru yang nantinya akan merespons permintaan dari pengguna untuk menampilkan daftar item.

#### Menghubungkan dengan Fungsi di views.py:
Path baru ini mengacu pada fungsi display_items yang telah saya buat sebelumnya di views.py. Ini berarti saat URL tersebut diakses, Django akan langsung memanggil fungsi tersebut untuk mendapatkan respons yang tepat.

### 7. Proses Deployment di Adaptable
Untuk proses deployment saya melakukan prosedur berdasarkan guideline dari Tutorial 0 dan melakukan setting pada perintah python manage.py migrate && gunicorn LiteraSync.wsgi

## Bagan request-response client Django 
![Flowchart Django](https://github.com/fikriwahab/LiteraSync/assets/124673453/1e11369b-6631-4b94-a528-b0357046b99e)

## Penggunaan Virtual Environment
Adanya virtual environment memungkinkan kita untuk membentuk space kerja yang terisolir untuk setiap project. Hal ini bertujuan untuk memastikan seluruh dependensi untuk Django terinstal pada versi yang tepat dan menjaga agar project tersebut tidak mempengaruhi atau dipengaruhi oleh proyek lain meskipun sudah ter-install dalam sistem yang sama.
Berikut beberapa keuntungan penggunaan Virtual Environment
### Isolasi Dependensi Proyek
Melalui virtual environment, pengguna dapat membuat proyek-proyek dalam versi Django yang berbeda, sehingga berbagai versi Django dapat di-install pada sistem yang sama. 
### Fleksibilitas Versi Python
Virtual environment juga memungkinkan kita menggunakan versi Python yang berbeda untuk proyek yang berbeda, sehingga tergantung kebutuhan spesifik dari pengguna.

Meskipun demikian, kita dapat mengembangkan aplikasi web berbasis Django tanpa virtual environment sekalipun. Tetapi risiko dalam inkompabilitas juga menjadi isu mengingat bahwa kita harus melakukan instalasi Django dan dependensi secara global. Hal ini menjadikan versi Django, versi Python, dependensi, serta project saling tumpang tindih. Untuk memastikan keteraturan dan fleksibilitas, sangat dianjurkan untuk mengaktivkan virtual environment saat hendak mengawali project tertentu.

##  MVC, MVT, MVVM dan perbedaannya
### 1. MVC (Model-View-Controller)
MVC merupakan pattern yang paling banyak digunakan untuk Web Development. Sebagai contoh adalah framework Ruby on Rails, Spring (Java), dan ASP.NET MVC.
#### Model: Bagian ini mirip dengan kerangka kerja di balik layar. Ini adalah tempat data disimpan dan dikelola.
#### View: Ini adalah apa yang kita lihat; antarmuka aplikasi. Jadi, ini mengambil data dari Model dan menampilkannya ke pengguna.
#### Controller: Ini adalah manajer yang mengatur apa yang harus dilakukan ketika Anda melakukan sesuatu di aplikasi, seperti mengklik tombol.

### 2. MVT (Model-View-Template)
MVT merupakan pattern yang kita gunakan dalam development menggunakan Django. MVT mencakup:
#### Model: Sama seperti di MVC, ini adalah kerangka kerja di balik layar tempat data disimpan.
#### View: Di sini, View bukanlah tampilan visual, tetapi lebih pada data apa yang ingin Anda tunjukkan dari Model.
#### Template: Ini adalah desain atau cara data ditampilkan. Jadi, ini lebih seperti "View" di MVC.

### 3. MVT (Model-View-ViewModel)
Merupakan pattern yang digunakan khusus untuk aplikasi dengan variasi interface yang cukup banyak, seperti desktop app maupun aplikasi berbasis XAML (contoh Windows Presentation Foundation, Xamarin).
#### Model: Sama seperti dalam MVC dan MVT, model MVVM menghandle data dan logika bisnis.
#### View: Merupakan representasi visual dari data, seperti tampilan GUI atau komponen antarmuka pengguna lainnya.
#### ViewModel: Bertindak sebagai penghubung antara Model dan View. ViewModel memproses tindakan atau perintah dari tampilan, memanipulasi data jika diperlukan, dan mengembalikan hasil ke tampilan.

## Note
### Selain melakukan testing yang diajarkan ditutorial, saya juga menambahkan fitur autentikasi bagi user untuk login dan mengakses database. Poin utamanya adalah dengan memanfaatkan fitur:
    # settings.py [MIDDLEWARE]
        django.contrib.auth.middleware.AuthenticationMiddleware
    # settings.py [INSTALLED_APPS]
        django.contrib.auth && django.contrib.contenttypes

=== LiteraSync ===
LiteraSync merupakan sebuah portal online yang menyediakan database untuk pencarian buku pada sebuah perpustakaan ataupun toko buku. Melalui aplikasi ini, baik customer dan seller dapat mencari buku dengan rincian stock, deskripsi, serta pengelolaan inventaris buku.

Link Akses Adaptable.io:
https://literasync.adaptable.app/main/

Implementasi checklist secara step-by-step:
1. Membuat sebuah proyek Django baru:
Sebelum saya membuat proyek Django baru, saya perlu melakukan beberapa hal, seperti membuat direktori yang saya inginkan, menambahkan inisiasi git pada repositori tersebut. Kemudian saya lanjutkan dengan membuka Command Prompt dalam direktori yang sebelumnya saya namai LiteraSync, kemudian saya membuat virtual environtment dengan mengetik "python -m venv env" dan mengaktivkannya dengan mengetik "env\Scripts\activate.bat". Setelah itu, barulah saya tambahkan requirements.txt beserta beberapa dependencies. Setelah dependencies terpasang, maka saya lakukan perintah "pip install -r requirements.txt" dan membuat proyek Django bernama LiteraSync dengan "django-admin startproject LiteraSync .".
2.  Pembuatan Aplikasi main:
Terlebih dahulu saya jalankan perintah "python manage.py startapp main", dan memastikan bahwa env tetap aktif, kemudian pada file settings.py ditambahkan 'main' pada Variabel INSTALLED_APPS, kemudian membentuk sebuah direktori dalam LiteraSync yang dinamai templates. Di dalamnya, saya tambahkan file main.html yang memuat representasi visual yang terdiri atas tabel yang menampilkan setiap item dari Item yang kita definisikan yang mencakup atribut name, amount, dan description. Selain itu saya juga menambahkan fitur search item (yang seharusnya dapat diintegrasikan dengan sebuah database), namun di sini saya membuat database temporer pada variabel 'books'. Variabel tersebut mencakup array dari berbagai judul buku. Saat pengguna mengetikkan sebuah judul pada serach bar, maka fungsi 'showSuggestions(str) dipanggil. Untuk kedepannya mungkin dapat saya manfaatkan pengintegrasian dengan API yang mengambil data dari database yang real-time.
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Beberapa fungsi dan modul perlu diimpor untuk proses routing di urls.py, kemudian rute baru ditambahkan pada variabel 'url patterns' yang langsung meredirect ke aplikasi 'main' yang telah dibuat. Dan pada akhirnya pengguna akan mengakses nedpoint'/items/'.
4. 
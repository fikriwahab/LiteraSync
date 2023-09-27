# Tugas 4 PBP
## Kelebihan dan Kekurangan Django UserCreationForm
### Kelebihan
- Efisiensi: Menggunakan UserCreationForm memungkinkan Developer untuk menghemat banyak waktu. Mereka tidak perlu merancang, mengimplementasikan, dan menguji formulir pendaftaran dari awal.
- Security: Django dikenal dengan keamanannya yang strict. Dengan menggunakan form bawaan, kita mendapatkan keuntungan dari berbagai fitur keamanan yang sudah diintegrasikan, seperti validasi password dan pencegahan serangan umum.
- Maintenance: Karena merupakan bagian dari framework Django, UserCreationForm mendapatkan pembaruan dan perbaikan keamanan dari komunitas Django.
### Kekurangan
- Kurangnya Fleksibilitas: Meskipun form ini sangat berguna untuk implementasi umum, mungkin ada skenario seperti saat kita memerlukan validasi khusus atau kolom tambahan. Dalam kasus seperti itu, kita mungkin perlu mengextend atau menggantinya dengan solusi kustom.
- Estetika: Tampilan bawaannya mungkin tidak sesuai dengan desain UI/UX yang diinginkan developer, sehingga memerlukan adjusment lebih lanjut.
## Perbedaan autentikasi dan otorisasi dalam Django
- Autentikasi merujuk pada proses validasi identitas pengguna. Ini adalah langkah pertama dalam mengakses sistem: "siapakah Anda?" Biasanya, autentikasi melibatkan pemeriksaan username dan password.

- Otorisasi merupakan proses yang dijalankan setelah autentikasi. Setelah sistem tahu siapa kita, otorisasi adalah tentang apa yang diizinkan untuk lakukan. Misalnya, seorang user mungkin memiliki akses untuk membaca konten tetapi tidak untuk mengeditnya.
### Pentingnya Autentikasi dan Otorisasi
- Mengamankan Aplikasi: Dengan kedua proses ini, kita dapat memastikan bahwa hanya pengguna yang sah yang mengakses aplikasi, dan mereka hanya dapat melakukan apa saja yang diizinkan.
- Mencegah Akses Tidak Sah: Otorisasi khususnya mencegah pengguna dari mengakses konten atau melakukan tindakan yang mereka tidak seharusnya lakukan, menjaga integritas data dan fungsionalitas sistem.

## Cookies pada Web App dan Pengelolaan data sesi pengguna dengan Cookies pada Django
Cookies adalah proses yang memungkinkan server untuk menyimpan informasi pada browser pengguna dan kemudian mengambilnya kembali saat diperlukan. Di banyak kasus, cookies digunakan untuk menyimpan preferensi pengguna, melacak informasi sesi, atau bahkan autentikasi.

Dalam konteks Django, framework ini menggunakan cookies, khususnya untuk mengelola sesi pengguna. Ketika pengguna masuk, Django menciptakan ID sesi unik, menyimpannya di cookie, dan mengasosiasikannya dengan data sesi pengguna di server.

## Penggunaan Cookies secara Default dan Risiko Potensial
Terlepas dari efisiensi dan kebermanfaatan dalam penggunaan cookies, masih ada beberapa aspek yang menjadi celah keamanan data, yaitu:
### Risiko:

- Intersepsi: Jika situs kita tidak menggunakan HTTPS, seorang peretas dapat meng-intercept traffic dan membaca atau memodifikasi cookies.
- Man-in-the-middle Attacks: Tanpa HTTPS, peretas dapat mengubah data yang dikirimkan antara klien dan server, termasuk cookies.
### Pencegahan:

- Gunakan HTTPS: Selalu gunakan HTTPS untuk mengenkripsi traffic antara klien dan server, termasuk cookies.
- Pasang Flag pada Cookies: Gunakan flags seperti Secure (untuk memastikan cookies hanya dikirim melalui HTTPS) dan HttpOnly (untuk mencegah akses cookies melalui JavaScript).

## Implementasi Checklist
### 1. Mengimplementasikan fungsi registrasi, login, dan logout


# Tugas 3 PBP
## Perbedaan antara form POST dan form GET dalam Django
Dalam penggunaan web form, ada dua method HTTP utama yang digunakan, yaitu method POST dan method GET. Keduanya memiliki fungsi yang sama, yaitu untuk mengirimkan informasi dari browser client ke server, namun ada beberapa perbedaan dari keduanya, yaitu:
### POST
Metode ini digunakan untuk mengirimkan data dengan dipack di dalam request body, bukan URL. Ini cocok untuk pengiriman data yang mengubah keadaan sistem, seperti pengubahan data di database. POST lebih aman dibandingkan GET, terutama saat mengirimkan informasi sensitif, karena data tidak ditampilkan di URL dan tidak mudah disimulasi oleh peretas. Dalam Django, formulir login dikembalikan menggunakan metode POST.
### GET
Metode ini menggabungkan data yang dikirimkan menjadi bagian dari URL. Sebagai contoh, jika kita melakukan pencarian di dokumentasi Django, akan menghasilkan URL seperti https://docs.djangoproject.com/search/?q=forms&release=1. Keuntungan dari GET adalah URL-nya dapat dibookmark, dibagikan, atau dikirim ulang dengan mudah. Namun, GET tidak sesuai untuk mengirimkan data pribadi seperti password (karena akan muncul di URL) atau data dalam jumlah besar.
#### Dengan demikian, setiap permintaan yang digunakan untuk mengubah keadaan sistem harus menggunakan method POST. Jika penggunaan hanya untuk request yang tidak mempengaruhi sistem maka gunakan method GET.

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data
### XML (eXtensible Markup Language) dan JSON (JavaScript Object Notation) 
Merupakan metode alternatif untuk menyimpan dan transfer data. Keduanya berfungsi sebagai format data exchange tetapi memiliki karakteristik yang berbeda:
- XML lebih fleksibel dan mendukung proses untuk validasi, namun cenderung verbose.
- JSON lebih mudah dibaca dan kurang verbose, sehingga mudah ditulis oleh pengguna maupun mesin. JSON juga asli untuk JavaScript, menjadikan JSON menjadi pilihan populer untuk web app modern.

### HTML (HyperText Markup Language)
Merupakan markup language yang digunakan untuk merepresentasikan bagaimana data harus ditampilkan pada perangkat pengguna atau client. HTML bukan format pertukaran data, melainkan lebih fokus pada representasi visual dari data.

## JSON dan Popularitasnya dalam Pertukaran Data Web App Modern
Ada beberapa faktor yang menjadikan JSON mendominasi dalam pertukaran data web app modern, seperti:
- Readability: JSON dirancang dengan estetika yang memprioritaskan readability. Format berbasis teksnya memastikan bahwa baik pengguna maupun mesin dapat memahami dan memproses informasi yang tertera. Ini tidak hanya memudahkan proses debugging bagi developer, tetapi juga mempermudah pemahaman dan modifikasi data, khususnya bagi mereka yang mungkin tidak memiliki latar belakang teknis yang mendalam.
- Simpel dan Ringkas: Sebelumnya, format seperti XML menjadi pilihan utama pertukaran data. Namun lain halnya dengan XML, JSON hadir dengan struktur yang lebih sederhana dan tidak memerlukan banyak markup tambahan. Dengan demikian, JSON menjadi lebih efisien dalam hal ukuran file dan kecepatan pemrosesan (lightweight). Ini membuatnya menjadi pilihan yang ideal, terutama dalam aplikasi web modern yang memerlukan respons cepat dan pertukaran data yang efisien.
- Integrasi dengan JavaScript: Integrasi yang erat dengan JavaScript merupakan salah satu daya tarik penggunaan JSON. JSON sendiri merupakan singkatan dari "JavaScript Object Notation. Ini berarti JSON tidak hanya merupakan bagian dari ekosistem JavaScript, tetapi juga diadopsi dengan sempurna di dalamnya. Ketika developer bekerja dengan aplikasi web yang memanfaatkan JavaScript, menggunakan JSON menjadi alami. Meskipun begitu, kehebatan JSON tidak terbatas pada JavaScript saja. Banyak bahasa pemrograman lainnya sekarang memiliki dukungan untuk JSON, yang memungkinkannya untuk berfungsi sebagai jembatan komunikasi antar berbagai sistem dan platform.
## Implementasi checklist secara step-by-step:
### 1. Membuat input form untuk menambahkan objek model pada app sebelumnya
- Dimulai dengan mengaktivkan environment.
- Membuat 'forms.py' pada direktori 'main' dan mendefinisikan 'ItemForm' berdasarkan model 'Item' dengan fields: "name", "amount", "description".
- Membuat view baru yang dinamai 'create_item' yang akan menghandle request dari form untuk menambahkan item ke database inventaris library.
- Menambahkan url untuk view baru pada 'urls.py' dalam direktori 'main'. Dengan code sebagai berikut:    

        app_name = 'main'
        urlpatterns = [
            path('', display_items, name='display_items'),
            path('create-item', create_item, name='create_item'),
- Membuat template 'create_item.html' untuk menampilkan form input ke pengguna. Template:

        {% extends 'base.html' %} 
        
        {% block content %}
        <h1>Add New Book</h1>
        
        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Book"/>
                    </td>
                </tr>
            </table>
        </form>
        
        {% endblock %}

- Menambahkan link ke form dari halaman utama.

### 2. Menambahkan 5 fungsi views.
- HTML View: Berdasarkan dari tugas 2, kita sudah membuat fungsi 'display_items' yang menjadi representasi visual seluruh data dalam format HTML.
- XML View: Membuat fungsi view 'show_xml' yang akan mengembalikan data item dalam format XML.
- JSON View: Membuat fungsi view 'show_json' yang akan mengembalikan data item dalam format JSON.
- XML by ID: Membuat fungsi view `show_xml_by_id' yang menerima parameter id dan mengembalikan data item tertentu dalam format XML.
- JSON by ID: Buat fungsi view `show_json_by_id yang menerima parameter id dan mengembalikan data produk tertentu dalam format JSON.

Dengan demikian, code nya adalah sebagai berikut:

        def display_items(request):
            items = Item.objects.all()
            return render(request, 'main.html', {'items': items})

        def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
        def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        
        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
### 3. Membuat routing URL untuk masing-masing views
- Menambahkan URL routing untuk masing-masing fungsi view yang sudah dibuat. Terdapat pula fungsi view yang menampilkan item berdasarkan ID dengan '<int:id>' sebagai parameter URL. Dengan demikian, code nya akan menjadi begini:

        app_name = 'main'
        
        urlpatterns = [
            path('', display_items, name='display_items'),
            path('create-item', create_item, name='create_item'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            ]
### 4. [BONUS] Menambahkan fitur yang menghitung jumlah data item yang tersimpan pada aplikasi
Setelah mengimplementasikan fitur input dan menampilkan data dalam berbagai format, kita juga dapat menambahkan fitur yang memungkinkan user mengetahui berapa jumlah item yang sudah ada pada database. Dalam konteks ini saya menambahkan 'total_items' untuk menghitung berapa jumlah jenis item yang sudah dimiliki oleh user. Dengan code:

        def display_items(request):
            items = Item.objects.all()
            total_items = items.count()
            return render(request, 'main.html', {'items': items, 'total_items': total_items})

Kemudian memperbarui main.html untuk menampilkannya secara visual, dengan memasukkan code berikut:
    
    <h2>LiteraSync (Portal Pencarian Buku Online)</h2>
    <p>Anda memiliki total {{ items.count }} jenis item yang tersimpan pada library.</p>

    <!-- Kolom Pencarian -->

## Screenshot hasil akses URL pada Postman 
# Akses HTML
![image](https://github.com/fikriwahab/LiteraSync/assets/124673453/43ab1362-2181-4e19-9d79-03c161c349ca)
# Akses XML
![image](https://github.com/fikriwahab/LiteraSync/assets/124673453/d46084b8-85ad-46b6-8363-9a1961b65827)
# Akses JSON
![image](https://github.com/fikriwahab/LiteraSync/assets/124673453/62c5a2c8-5e68-48f0-a09d-33f2d546bf55)
# Akses XML per ID
![image](https://github.com/fikriwahab/LiteraSync/assets/124673453/df3866fb-e823-4065-bd20-01af094e49f4)
# Akses JSON per ID
![image](https://github.com/fikriwahab/LiteraSync/assets/124673453/3d1e66d4-e63e-40e8-a928-12502ecec015)

## References
##### https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=Fundamentally%2C%20JSON%20and%20XML%20are,is%20more%20flexible%20and%20secure.
##### https://aws.amazon.com/compare/the-difference-between-json-xml/#:~:text=As%20a%20markup%20language%2C%20XML,size%20for%20faster%20data%20transfer.
##### https://www.geeksforgeeks.org/render-html-forms-get-post-in-django/
##### https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST&text=Django's%20login%20form%20is%20returned,this%20to%20compose%20a%20URL.

# Tugas 2 PBP
## Deskripsi LiteraSync
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
## References
##### https://docs.djangoproject.com/en/4.2/topics/http/views/#mapping-urls-to-views
##### https://learnbatta.com/blog/understanding-request-response-lifecycle-in-django-29/
##### https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/
##### https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/
##### https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment
##### https://www.w3schools.com/django/django_create_virtual_environment.php
##### https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0
##### https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-1

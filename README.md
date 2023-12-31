# Tugas 6 PBP
## Perbedaan antara Asynchronous Programming dengan Synchronous Programming
Referensi: https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/#:~:text=The%20differences%20between%20asynchronous%20and,multiple%20requests%20to%20a%20server.
### 1. Dasar Operasional
- Asynchronous programming memungkinkan tugas-tugas untuk berjalan secara independen tanpa harus menunggu penyelesaian tugas lain. Ini adalah pendekatan non-blocking, yang berarti eksekusi satu tugas tidak bergantung pada yang lain. Dengan demikian, tugas dapat berjalan secara simultan.
- Synchronous programming memerlukan setiap operasi untuk menyelesaikan sebelum operasi selanjutnya dapat dimulai. Ini adalah pendekatan blocking, di mana eksekusi setiap operasi bergantung pada penyelesaian operasi sebelumnya. Setiap tugas memerlukan respons sebelum berlanjut ke iterasi berikutnya.
### 2. Thread & Interaksi Server
- Asynchronous programming bersifat multi-thread, yang memungkinkan berbagai operasi atau program berjalan secara paralel. Kemudian dengan sifat non-blocking, memungkinkan proses pengirimkan beberapa Request ke server secara bersamaan.
- Synchronous programming bersifat single-thread, yang berarti hanya satu operasi atau program yang akan berjalan pada satu waktu. Synchronous programming bersifat blocking, sehingga hanya akan mengirim satu request ke server pada satu waktu dan menunggu request tersebut direspons oleh server.
### 3. Pengembangan
- Asynchronous programming meningkatkan pengalaman pengguna dengan memuat layar aplikasi lebih cepat.
- Synchronous programming lebih mudah untuk dikodekan oleh pengembang. Ini didukung dengan baik di semua bahasa pemrograman dan sebagai metode pemrograman default, pengembang tidak perlu menghabiskan waktu untuk belajar sesuatu yang baru.
### 4. Dalam Konteks AJAX
- Dengan AJAX, panggilan asynchronous ke server dapat dilakukan. Artinya, ketika browser mengirim request ke server melalui AJAX, pengguna masih dapat berinteraksi dengan halaman web dan halaman tersebut tidak terblokir saat menunggu respons dari server. Hal ini meningkatkan user experience karena halaman web tetap responsif. Misalnya, saat pengguna mengisi formulir dan mengklik tombol untuk mengirimkan, sementara data dikirim ke server, pengguna mungkin melihat animasi pemuatan tetapi tetap dapat berinteraksi dengan bagian lain dari situs.
- Jika AJAX diatur untuk berfungsi secara synchronous, browser akan menunggu respons dari server sebelum melanjutkan. Selama waktu tunggu ini, halaman web mungkin menjadi tidak responsif, yang dapat mengganggu pengalaman pengguna. Penggunaan AJAX secara synchronous jarang ditemui karena dapat mengurangi keuntungan utama dari menggunakan AJAX, yaitu menjaga halaman web tetap responsif saat berkomunikasi dengan server.
## Paradigma event-driven programming dalam penerapan JavaScript dan AJAX
Event-driven programming adalah paradigma pemrograman di mana alur eksekusi program ditentukan oleh berbagai peristiwa, seperti input pengguna, sensor output, atau pesan dari program lain. Pada dasarnya, program menunggu dan merespons peristiwa tertentu untuk dieksekusi. Ini berbeda dengan pemrograman prosedural tradisional di mana alur eksekusi ditentukan oleh urutan perintah yang telah ditentukan sebelumnya.

Dalam konteks aplikasi web yang menggunakan JavaScript dan AJAX, paradigma event-driven memungkinkan halaman web untuk merespons tindakan pengguna tanpa perlu memuat ulang halaman. Event bisa berupa klik tombol, penekanan tombol, gerakan mouse, dll. Ketika event tertentu terjadi, fungsi tertentu dapat dipanggil.

Contoh penerapannya pada tugas 6:
### 1. AJAX GET
Saat page dimuat, sebuah event dapat memico fungsi AJAX GET untuk mengambil data item dari server dan menampilkannya dalam bentuk cards pada halaman.
### 2. AJAX POST
- Tombol yang membuka modal adalah pemicu event. Ketika pengguna menekan tombol tersebut, sebuah modal dengan form muncul.
- Saat pengguna mengisi form dan mengklik tombol submit di dalam modal, event lain (misalnya, event click pada tombol submit) dipicu. Fungsi AJAX POST akan dijalankan untuk mengirim data yang dimasukkan oleh pengguna ke server tanpa harus memuat ulang seluruh halaman.
- Setelah data berhasil disimpan ke database melalui /create-ajax/, respons dari server dapat memicu event lain di sisi klien untuk menutup modal, membersihkan form, dan memperbarui tampilan halaman dengan data baru tanpa perlu refresh total. Dapat dilakukan misalnya dengan menambahkan card baru ke daftar atau memperbarui bagian tertentu dari halaman.
Melalui approach event-driven ini, user experience berlangsung responsif dan smooth, hal ini dikarenakan mereka tidak perlu menunggu page refresh setiap mereka melakukan tindakan. Sebaliknya, hanya beberapa bagian terkait dari halaman yang di-refresh berdasarkan event yang terjadi.
## Penerapan Asynchronous Programming pada AJAX
AJAX secara general memanfaatkan konsep asynchronous programming untuk memungkinkan pertukaran data dengan Web Server tanpa harus memuat ulang keseluruhan Web Page. Adapun beberapa penerapannya, antara lain:
### 1. Non-blocking call AJAX
Salah satu fitur utama asynchronous programming adalah kemampuan untuk melanjutkan eksekusi kode tanpa harus menunggu proses (misalnya request ke server) selesai. Dalam konteks AJAX, ketika sebuah request dikirim ke server, user masih dapat berinteraksi atau menggunakan web page. Web page tetap mempertahankan responsivenessnya.
### 2. XMLHttpRequest
Saat membuat instance dari XMLHttpRequest dan mengirim request, developer dapat menentukan bahwa request harus dilakukan secara asynchronous. Hal ini menunjukkan bahwa setelah request dikirim, kode JavaScript dapat terus berjalan tanpa menunggu respons.
### 3. Event Handlers:
Karena bawaan sifat asyncrhonous pada AJAX, developer menggunakan event handlers untuk menangani respons. Misalnya ketika respons dari server diterima, sebuah fungsi callback dari XMLHttpRequest dipanggil. Fungsi tersebut akan memproses repsons dan me-refresh halaman web sesuai kebutuhan.
### 4. Dynamic Response
Dengan AJAX, beberapa bagian pada Web Page dapat diupdate secara dinamis berdasarkan data yang diterima dari server. Semisal pada fitur komentar atau forum, kita dapat melakukan refresh tanpa harus memuat ulang seluruh halaman.

Secara umum, penerapan asynchronous programming pada AJAX memungkinkan Web Page yang lebih responsif bagi penggunanya dan mengurangi beban pada server ataupun bandwith, karena data yang diterima ataupun dikirim hanya data yang dibutuhkan, bukan seluruh Web Page.
## Perbandingan Fetch API dan Library jQuery
### 1. Fetch API
Fetch API merupakan API modern yang menawarkan JavaScript interface yang lebih smooth dan robust untuk mengakses maupun manipulasi HTTP pipeline, seperti request dan response. Penggunaan sintaks Fetch API juga tergolong simpel dan serupa dengan JavaScript. Dependencies pada Fetch API juga sudah menjadi fitur bawaan pada sebagian besar aplikasi browser sekarang, jadi tidak memerlukan external library. Dengan demikian, Fetch API di-support oleh browser versi terbaru dan tidak bisa dijalankan pada browser versi lama.

### 2. jQuery AJAX
jQuery merupakan approach AJAX yang cukup lama/tua untuk AJAX. Pada jQuery juga disediakan library JavaScript yang menyediakan beberapa method, seperti $.ajax(), $.get(), dan $.post() untuk mempermudah penggunaan AJAX. Penggunaan sintaks pada jQuery juga sedikit kompleks dan membutuhkan library jQuery untuk menjalankan fungsionalitasnya. Dengan demikian developer perlu menyediakan library jQuery ke projectnya, dan hal ini berimplikasi pada peningkatan ukuran file. Walaupun cukup reliable dan sudah digunakan cukup lama, jQuery tertinggal dari Fetch dalam hal penyediaan fitur-fitur yang lebih modern. Namun, jQuery masih memiliki aksesibilitas yang luas yang mana baik browser versi baru atau lama sekalipun masih meng-support jQuery.

Baik Fetch API dan jQuery memiliki kelebihan dan kekurangannya masing-masing. Jika mempertimbangkan kompabilitas dan integrasi dengan Bootstrap, jQuery mungkin menjadi pilihan yang tepat. Namun, untuk proyek yang harus menyesuaikan dengan modernitas Web Development, Fetch API lebih cocok karena fiturnya yang lebih canggih dan tidak memerlukan konfigurasi external dependencies. Oleh karena itu, ketika berbicara Web Development yang menetapkan standar modern, Fetch API memberikan manfaat yang lebih banyak bagi developer dengan fleksibilitas dan kontrol yang lebih accessible, dan lebih simpel dalam hal konfigurasinya.

## Implementasi checklist secara step-by-step
### AJAX GET
#### 1. Mengubah kode cards data item agar dapat mendukung AJAX GET
- Menambahkan fungsi baru untuk mengirimkan data dalam format JSON pada file views.py dan menambahkan path baru pada urls.py

        # views.py
        from django.http import JsonResponse
        
        @login_required(login_url='/login')
        def get_items_json(request):
            items = Item.objects.filter(user=request.user).values('id', 'name', 'description', 'amount')
            return JsonResponse(list(items), safe=False)

        # urls.py
        path('get-items/', get_items_json, name='get_items_json'),

- Menambahkan code JavaScript untuk memanggil AJAX

        # main.html
        ...
        <script>
        function fetchItems() {
            fetch("{% url 'main:get_items_json' %}")
            .then(response => response.json())
            .then(data => {
                let itemsContainer = document.querySelector(".grid");
                itemsContainer.innerHTML = ""; // Clear the container
                data.forEach(item => {
                    let itemDiv = document.createElement("div");
                    itemDiv.className = "bg-white shadow-md rounded-md p-4";
                    itemDiv.innerHTML = `
                        <h3 class="text-xl font-bold mb-2">${item.name}</h3>
                        <p><strong>Jumlah:</strong> ${item.amount}</p>
                        <p class="mb-4"><strong>Deskripsi:</strong> ${item.description}</p>
                        <div>
                            <a href="{% url 'main:increment_item' item.id %}" class="text-blue-500 hover:text-blue-700 mr-2">Tambah</a>
                            <a href="{% url 'main:decrement_item' item.id %}" class="text-yellow-500 hover:text-yellow-700 mr-2">Kurangi</a>
                            <a href="{% url 'main:delete_item' item.id %}" class="text-red-500 hover:text-red-700">Hapus</a>
                        </div>
                    `;
                    itemsContainer.appendChild(itemDiv);
                });
            })
            .catch(error => {
                console.error('Error fetching items:', error);
            });
        }
        
        // Call fetchItems on page load
        window.onload = fetchItems;
        </script>
#### 2. Mengubah kode cards data item agar dapat mendukung AJAX GET
- Melakukan sedikit perubahan agar memastikan endpoint mengambil semua Item dan mengembalikannya dalam format JSON. Agar lebih spesifik ke user yang sedang login, maka fungsi get_items_json(request) dimodifikasi menjadi:

        # views.py
        @login_required(login_url='/login')
        def get_items_json(request):
            items = Item.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", items), content_type="application/json")
        # urls.py
        path('get-items-json/', get_items_json, name='get_items_json'),
### AJAX GET
#### 1. Membuat tombol yang membuka sebuah modal dengan form untuk menambahkan item
- Menambahkan code untuk modal di main.html

        <!-- Modal untuk menambahkan item -->
        <div id="addItemModal" class="fixed z-10 inset-0 overflow-y-auto hidden" aria-labelledby="modal-title" role="dialog" aria-modal="true">
            <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75" aria-hidden="true"></div>
                
                <!-- Modal box -->
                <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                    <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                            Tambahkan Item Baru
                        </h3>
                        <!-- Form di sini -->
                        <form id="addItemForm">
                            <div>
                                <label>Nama Item:</label>
                                <input type="text" id="itemName" required>
                            </div>
                            <div>
                                <label>Jumlah:</label>
                                <input type="number" id="itemAmount" required>
                            </div>
                            <div>
                                <label>Deskripsi:</label>
                                <textarea id="itemDescription" required></textarea>
                            </div>
                            <button type="submit">Simpan</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

- Menambahkan tombol yang men-trigger modal

        <button onclick="openModal()" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
            Tambah Item (Modal)
        </button>
- Menambahkan JavaScript untuk menampilkan dan menyembunyikan modal

        function openModal() {
            document.getElementById('addItemModal').classList.remove('hidden');
        }
        
        function closeModal() {
            document.getElementById('addItemModal').classList.add('hidden');
        }
        
        // Handle the form submission
        document.getElementById('addItemForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Ambil data dari form
            const itemName = document.getElementById('itemName').value;
            const itemAmount = document.getElementById('itemAmount').value;
            const itemDescription = document.getElementById('itemDescription').value;
        
            // TODO: Kirim data ini menggunakan AJAX POST ke server
        
            // Setelah selesai, tutup modal
            closeModal();
        });
#### 2. Membuat fungsi view baru untuk menambahkan item baru ke dalam basis data
- Menambahkan fungsi view pada views.py yang akan menerima data yang dikirim melalui AJAX POST dari form modal yang telah dibuat sebelumnya.

        from django.views.decorators.csrf import csrf_exempt
        from django.utils import timezone
        
                # views.py
                @csrf_exempt
                @login_required(login_url='/login')
                def add_item(request):
                    if request.method == 'POST':
                        # Menerima data dari POST request
                        item_name = request.POST.get('name')
                        item_amount = request.POST.get('amount')
                        item_description = request.POST.get('description')
                
                        # Membuat objek baru dan menyimpannya
                        new_item = Item(name=item_name, amount=item_amount, description=item_description, created_at=timezone.now(), user=request.user)
                        new_item.save()
                
                        return JsonResponse({'message': 'Item successfully added!'}, status=201)
                    else:
                        return JsonResponse({'error': 'Invalid method'}, status=400)
                # urls.py
                path('add-item/', add_item, name='add_item'),
Melalui dekorator @csrf_exempt POST request di-approve tanpa CSRF token. Kemudian memeriksa apakah request adalah metode POST dan mengambil data dari request POST. Objek baru dengan model Item dibuat dan disimpan ke dalam database. Sebagai respons, pesan JSON dikembalikan untuk menginformasikan bahwa item berhasil ditambahkan.
#### 3. Membuat path /create-ajax/ yang mengarah ke fungsi view yang sudah dibuat
- Menambahkan kode berikut pada urls.py

        path('create-ajax/', add_item, name='create_ajax_item'),
Dengan demikian, kita memiliki path /create-ajax/ yang mengarah ke fungsi add_item. Sehingga, setiap saat AJAX POST request dikirim ke /create-ajax/, fungsi add_item akan dipanggil dan item baru akan ditambahkan ke database.
#### 4. Menghubungkan form yang telah dibuat di dalam modal menuju path /create-ajax/
- Mengubah cara pengambilan data dari form agar sesuai dengan pengiriman data ke server melalui AJAX
- Menggunakan AJAX untuk mengirim data ke /create-ajax/ saat form disubmit
- Menambahkan kode untuk mendapatkan CSRF token (jika dibutuhkan)
Berikut beberapa perubahan dan tambahan pada kode:

        <form id="addItemForm" action="/create-ajax/" method="post">
        ...
        function getCookie(name) {
            let value = "; " + document.cookie;
            let parts = value.split("; " + name + "=");
            if (parts.length == 2) return parts.pop().split(";").shift();
        } //Penambahan function getCookie untuk mendapatkan nilai CSRF token jika dibutuhkan
        ...
        document.getElementById('addItemForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Ambil data dari form
            const itemName = document.getElementById('itemName').value;
            const itemAmount = document.getElementById('itemAmount').value;
            const itemDescription = document.getElementById('itemDescription').value;
        
            // Kirim data ini menggunakan AJAX POST ke server
            fetch('/create-ajax/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    name: itemName,
                    amount: itemAmount,
                    description: itemDescription
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Item berhasil ditambahkan!');
                    closeModal();
                    fetchItems();
                } else {
                    alert('Terjadi kesalahan saat menambahkan item. Silakan coba lagi.');
                }
            });
        
            // Setelah selesai, tutup modal
            closeModal();
        });
#### 5. Refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan
#### 6. Melakukan perintah collectstatic
- Memastikan konfigurasi STATIC_ROOT pada file settings.py

        # settings.py
        ...
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/4.2/howto/static-files/
        
        STATIC_URL = 'static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- Menjalankan perintah collectstatic pada command prompt

        python manage.py collectstatic

#### Checklist Bonus (Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE)
- Menambahkan pada urls.py dan views.py untuk membuat view yang dapat menghandle AJAX DELETE

        # urls.py
        path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax'),

        # views.py
        from django.http import JsonResponse
        
        def delete_item_ajax(request, item_id):
            if request.method == "DELETE":
                try:
                    item = Item.objects.get(id=item_id)
                    item.delete()
                    return JsonResponse({'status': 'success'}, status=200)
                except Item.DoesNotExist:
                    return JsonResponse({'status': 'failed', 'message': 'Item not found'}, status=404)
            return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=400)
- Mengupdate JavaScript untuk handle delete dengan AJAX

        function deleteItem(itemId) {
            fetch(`/delete-item-ajax/${itemId}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Item berhasil dihapus!');
                    fetchItems();  // Update tampilan item
                } else {
                    alert('Gagal menghapus item: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error deleting item:', error);
            });
        }
        
- Menghubungkan fungsi Delete ke tombol hapus

        <a href="javascript:void(0);" onclick="deleteItem({{ item.id }})" class="text-red-500 hover:text-red-700">Hapus</a>

# Tugas 5 PBP
## Manfaat Element Selector dan Kapan Waktu Penggunaanya
### 1. Universal Selector (*)
Universal Selector sering digunakan dalam 'CSS Reset', di mana tujuannya adalah untuk menghilangkan perbedaan tampilan standar antara berbagai browser. Selector bekerja dengan memilih seluruh elemen dalam sebuah page dan berguna untuk mengatur margin atau padding. Penggunaan Universal Selector dilakukaan saat kita hendak menerapkan styling yang sama pada seluruh elemen di halaman, seperti mengatur margin dan padding menjadi nol untuk menghapus default dari browser.
### 2. Type Selector (E)
Dalam memahami konsep dasar Styling, kita perlu memahami Type Selector. Type Selector bekerja dengan memilih seluruh elemen dari jenis tertentu dan memungkinkan kita untuk mengimplementasikan penerapan styling pada elemen dasar tanpa memerlukan pemilihan yang rumit. Digunakan pada kasus seperti ketika kita hendak mengatur styling untuk seluruh elemen dengan jenis yang sama, contohnya seluruh elemen "h2".
### 3. Descendant Selector (E F)
Berguna untuk mengatur hierarki dan struktur desain web kita. Selain itu Descendant Selector memungkinkan styling yang lebih spesifik tanpa harus memberikan kelas atau id pada tiap elemen. Dengan ini, kita dapat memilih elemen F yang merupakan turunan dari E, sehingga kita dapat mengatur styling pada elemen tertentu yang berada di dalam elemen lain. Selain itu, contohnya dapat berupa 'li a'.
### 4. Class Selector (.classname)
Salah satu selector yang paling umum digunakan dalam CSS karena memungkinkan kita untuk mengelompokkan elemen berdasarkan fungsi atau gaya, bukan hanya jenis. Sehingga Class Selector dapat memilih semua elemen dengan kelas tertentu. Saat kita memiliki sekelompok elemen yang ingin kita beri styling yang sama, tapi tidak semuanya memiliki jenis yang sama, maka dapat menggunakan Class Selector. 
### 5. ID Selector (#idname)
Dengan ID Selector, kita dapat memilih elemen dengan ID tertentu. Cocok digunakan saat kita ingin memberi styling khusus pada satu elemen yang unik di page.
### 6. Attribute Selector
Berfungsi untuk memilih elemen berdasarkan atributnya. Cocok jika kita ingin melakukan styling berdasarkan atribut tertentu dari elemennya. Contoh '[type="text"]'.
## HTML5 Tag
HTML5 (Hyper Text Markup Language Versi 5) merupakan update dan teknologi penerus versi sebelumnya yang dikeluarkan oleh W3C (World Wide Wen Consortium) dan WHATWG (Web Hypertext Application Technology Working Group) yang mencakup tambahan feature-feature baru untuk memperbaiki dan melengkapi dari HTML versi sebelumnya.
### Fitur baru HTML5
- New Semantic Elements: Beberapa elemen semantik baru, seperti pada elemen header, footer, section, article, section, aside, nav, figure, figcaption, dan time.
- Forms 2.0: Perbaikan form web HTML yang mana atribut baru telah diperkenalkan tag "input" dengan tipe baru seperti "color", "date", "email", dll. Selain itu juga tambahan seperti output, progress, meter, datalist.
- Persistent Local Storage: Mengurangi kebutuhan untuk mengandalkan plugin dari pihak ketiga.
- WebSocket: Teknologi komunikasi dua arah terkini untuk aplikasi web.
- Server-Sent Events : Membawa fitur yang memfasilitasi aliran event dari server web ke peramban, dikenal sebagai SSE.
- Canvas : Menawarkan permukaan gambar dua dimensi yang bisa diprogram menggunakan JavaScript. Mencakup canvas dan svg.
- Audio & Video : Memungkinkan penanaman audio atau video di halaman web tanpa kebutuhan plugin eksternal. Seperti tag audio, video, source.
- Geolocation : Para pengunjung memiliki opsi untuk membagikan lokasi geografis mereka ke aplikasi web Anda.
- Microdata : Memberikan kemampuan untuk menciptakan kosakata kustom di luar HTML5 dan menambahkan semantik tambahan pada halaman web Anda.
- Drag and drop : Memindahkan objek dengan metode tarik dan lepas di dalam satu halaman web.
### Fitur yang dihapus pada HTML5
- Acronym : Menjelaskan suatu akronim, fungsinya mirip dengan tag abbr.
- Applet : Memungkinkan penyertaan file Java dalam dokumen HTML.
- Basefont : Menetapkan atribut teks dasar, seperti warna, ukuran, dan jenis huruf untuk seluruh konten teks dokumen.
- Big : Meningkatkan ukuran teks satu tingkat dari ukuran standarnya.
- Center : Mengatur teks atau gambar agar berada di tengah.
- Dir : Menampilkan daftar sebagai direktori.
- Font : Menentukan jenis huruf, warna, dan ukuran teks.
- Frame : Menentukan suatu frame dalam suatu rangkaian frame.
- Frameset : Menyusun kelompok dari beberapa frame.
- Noframes : Digunakan ketika peramban pengguna tidak mendukung frame.
- Strike : Menambahkan garis melintang pada teks, memiliki fungsi serupa dengan tag <del>.
- Tt : Menampilkan teks dengan gaya teletype.
## Perbedaan Framework CSS Tailwind dan Bootstrap
### Bootstrap:
Bootstrap adalah framework CSS open-source gratis yang digunakan untuk membuat aplikasi web dan mobile yang responsif. Mencakup template HTML, CSS, dan JavaScript untuk berbagai komponen Web Development. Kelebihannya antara lain:
- Menawarkan tema dan template siap pakai yang mempercepat development.
- Mengusung ide mobile-first dengan sistem grid 12 kolom yang memastikan kompatibilitas cross-browser.
- Menyediakan gaya dasar untuk elemen HTML seperti tombol, gambar, tabel, form, dll.
- Bisa dikustomisasi sesuai kebutuhan proyek.
- Sangat populer dan banyak digunakan oleh perusahaan seperti Twitter, LinkedIn, dan Spotify.
Dengan demikian, Bootstrap cocok digunakan ketika kita hendak mengerjakan project dengan cepat dan memerlukan komponen atau template yang sudah siap dengan sedikit perubahan atau kustomisasi. Selain itu juga cocok digunakan saat project lebih berfokus pada pekerjaan backend dan memerlukan tata letak yang umum.
### Tailwind CSS:
Tailwind CSS adalah framework CSS utility-first yang memungkinkan developer untuk membuat user interface yang disesuaikan dengan cepat. Kelebihannya antara lain:
- Menawarkan class utility unik yang memungkinkan desain kustom cepat.
- Menyediakan fleksibilitas besar dalam desain, memungkinkan pembuatan UI yang unik.
- Ukuran file yang lebih kecil karena pendekatan utilitas-first.
- Populer dan banyak digunakan oleh perusahaan seperti MAKE IT dan Hashnode.
Tailwind CSS hendaknya digunakan ketika kita ingin memiliki kontrol penuh atas desain kita tanpa mengandalkan template yang sudah pre-styled, sehingga approach pemrogramannya lebih modular dan custom. Dan untuk project yang lebih kompleks juga cocok dikerjakan dengan Tailwind CSS.
### Kesimpulan
Bootstrap dan Tailwind CSS keduanya memiliki kelebihan masing-masing. Pilihan antara keduanya bergantung pada kebutuhan spesifik project kita. Bootstrap lebih cocok untuk aplikasi yang memerlukan responsivitas dan kecepatan pengembangan dengan tema dan template siap pakai. Sementara Tailwind CSS lebih cocok jika kita ingin kebebasan dalam desain dan fokus pada approach utility-first.
## Implementasi Checklist

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
#### Register
Membuat form bawaan dari Django yang dikhususkan untuk pendaftaran user, yaitu dengan UserCreationForm

        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  

        def register(request):
            form = UserCreationForm()
        
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
Kemudian buat file khusus register yang dinamai register.html, serta mengisinya dengan template berikut:

        {% extends 'base.html' %}
        
        {% block meta %}
            <title>Register</title>
        {% endblock meta %}
        
        {% block content %}  
        
        <div class = "login">
            
            <h1>Register</h1>  
        
                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>
        
            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}
        
        </div>  
        
        {% endblock content %}

Setelah itu jangan lupa untuk menambah view register di urls.py

    from main.views import register
    path('register/', register, name='register'),

#### Login
Mempersiapkan form login dengan menggunakan form bawaan Django, yaitu:

        from django.contrib.auth import authenticate, login
Kemudian menambahkan fungsi login_user untuk menjalankan proses authentikasi bagi user yang ingin melakukan login:

        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:display_items")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)

Kemudian membuat berkas html baru dengan nama login.html, dengan template berikut:

        {% extends 'base.html' %}
        
        {% block meta %}
            <title>Login</title>
        {% endblock meta %}
        
        {% block content %}
        
        <div class = "login">
        
            <h1>Login</h1>
        
            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>
        
                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>
        
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        
        </div>
        
        {% endblock content %}

Dan pada urls.py tambahkan path url dan impor fungsi login_user:

        from main.views import login_user
        path('login/', login_user, name='login'),

#### Logout
Pada file views.py tambahkan terlebih dahulu dan membuat fungsi logout_user

        from django.contrib.auth import logout

        def logout_user(request):
            logout(request)
            return redirect('main:login')

Kemudian tambahkan template pada main.html dan diposisikan setelah bagian "Sesi terakhir login"

        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>

Jangan lupa untuk menambahkan impor fungsi dan path url pada urls.py

        from main.views import logout_user
        path('logout/', logout_user, name='logout'),

#### Restriksi Akses Halaman Main
Setelah menambahkan fitur atau form Register hingga logout, kita pisahkan akses halaman main page agar hanya user yang sudah mendaftar yang mendapat akses main pada website tersebut. Pada file viws.py kita impor @login_required untuk mengharuskan pengguna login sebelum dapat mengakses web.

        from django.contrib.auth.decorators import login_required
        ...
        @login_required(login_url='/login')
        def display_items(request):
        ...
### 2. Membuat 2 akun dummy dengan 3 dummy data       
### 3. Menghubungkan model Item dengan User
Agar tampilan atau data terkait produk hanya mencakup produk yang dibuat oleh masing-masing user, maka kita harus menghubungkannya agar data yang diperoleh menjadi paralel. Jika mengacu pada pengerjaan sebelumnya, data Item masih mengacu pada data Item secara global, sehingga setiap user akan melihat inventaris Item yang sama. Oleh karenanya, kita buat hal tersebut menjadi bagian yang terpisah berdasarkan akun. 

tambahkan Foreignkey dan import User

        from django.contrib.auth.models import User
        class Item(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            ...
Kemudian tambahkan pada views.py:

        def create_item(request):
            form = ItemForm(request.POST or None)
        
            if form.is_valid() and request.method == "POST":
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return HttpResponseRedirect(reverse('main:display_items'))
        
            context = {'form': form}
            return render(request, "create_item.html", context)
Setelah itu, lakukan sedikit perubahan kode pada bagian fungsi display_items

        def display_items(request):
            items = Item.objects.filter(user=request.user)
            return render(request, 'main.html', {'name': request.user.username, ...
            ...

Dengan menambahkan beberapa bagian kode, kita dapat menampilkan objek Product yang berdasarkan masing-masing pengguna yang sudah login. Saat user sudah login, maka kode 'request.user.username' akan menampilkan username pengguna terkait pada bagian halaman main.

Untuk menyimpan perubahan, kita lakukan migrasi model dengan:

        python manage.py makemigrations
Jika terdapat error saat migrasi model, maka pilihlah atau masukkan input '1' untuk memastikan default value untuk field user pada semua row yang sudah dibuat dalam basis data.

Kemudian aplikasikan migrasi tersebut dengan:

        python manage.py migrate
        
### 4. Penerapan Cookies dan informasi last login
Tambahkan beberapa import di file views.py dan merubah susunan kode pada fungsi create_items

        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
Pada fungsi login_user tambahkan cookie yang bernama last_login untuk menginformasikan kapan terakhir kali user melakukan login.

        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:display_items")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')

Kemudian pada fungsi display_items kita tambahkan 'last_login': request.COOKIES['last_login'], sehingga kodenya akan menjadi:

        @login_required(login_url='/login')
        def display_items(request):
            items = Item.objects.filter(user=request.user)
            total_items = items.count()
            return render(request, 'main.html', {'name': request.user.username,'items': items, 'total_items': total_items, 'last_login': request.COOKIES.get('last_login', 'Not available')})
Dengan penambahan berikut memungkinkan user untuk melihat informasi last_login pada website. Setelah itu, dengan penambahan cookie ini kita juga memberi sedikit perubahan pada fungsi logout_user. Perubahan tersebut bertujuan untuk menghapus cookie last_login saat pengguna sudah melakukan logout.

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response

Untuk menampilkan secara visual, jangan lupa untuk menambahkan pada main.html agar sesi terakhir login dapat dilihat pada website.

        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
Untuk memastikan bahwa data cookie sudah ada, kita dapat melakukan cek pada fitur inspect element, dan kemudian membuka bagian Application/Storange. Pada bagian 'Cookies' kita akan melihat 3 data cookies, yaitu last_login, csrftoken, dan sessionid. Dengan demikian, berarti kita telah berhasil untuk mengintegrasikan form register, login, dan logout dengan implementasi yang sesuai di website kita.

####
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

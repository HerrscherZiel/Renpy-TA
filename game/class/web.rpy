
default a_webA = 0
default a_webT = 0
default a_webC = 0
default a_webTS = 0
default a_webAS = 0
default a_webN = 0

label web_1:

    scene bg campus class with dissolve

    pa normal "Selamat siang teman-teman, bertemu lagi kita pada siang hari ini…"

    "[pa] memasuki ruang kelas, suasana kelas yang semula ramai menjadi sepi."

    pa "Hmm tampaknya masih ada beberapa yang belum hadir ya? Mungkin kita mulai kelasnya 15 menit lagi sambil menunggu yang belum hadir."

    t normal "Baik pak…"

    scene bg campus class with fade
    pause 1.5

    "Kemudian setelah 15 menit menunggu dan jumlah mahasiswa yang hadir sudah bertambah kelas akhirnya dimulai."

    pa normal "Yak jadi pada siang hari ini, kita akan mempelajari mengenai Pemrograman Web I."

    pa "Tentu saja pada pertemuan pertama kita hanya akan membahas mengenai pengertian dasar, jenis dan kategori web."

    # hide screen web_1_1

    show screen web_1_1 with fade

    pa "Sebenarnya apa sih web itu? World Wide Web(WWW) atau yang lebih dikenal dengan Web merupakan salah satu layanan yang dapat kita akses melalui sebuah koneksi internet. 
    Layanan ini menyediakan berbagai macam informasi yang dapat kita akses. "

    pa "Kumpulan dari halaman-halaman yang menampilkan informasi dengan berbagai macam bentuk tersebut dihubungkan menggunakan jaringan halaman atau hyperlink. 
    Hal ini biasa kita sebut dengan Websites atau situs."

    pa "Kemudian bagaimana cara kerja web itu sendiri?"

    pa "Informasi web terdapat pada suatu halaman web yang disediakan oleh sisi Server sebagai penyedia layanan."

    pa "Untuk mengaksesnya kita sebagai sisi Client memerlukan sebuah Web Browser untuk dapat menavigasi kita pada suatu halaman Web."

    pa "Sewaktu mengakses sebuah halaman Web menggunakan Web Browser kita memerlukan sebuah protokol dan alamat untuk halaman Web tersebut."

    hide screen web_1_1

    show screen web_1_2 with fade

    pa "HTTP atau Hypertext Transfer Protocol merupakan sebuah protokol yang menyediakan aturan dalam proses pengaksesan sebuah halaman Web. Protokol ini merupakan sebuah protokol standard yang digunakan untuk mengakses sebuah dokumen HTML."

    pa "URL atau Uniform Resource Locator digunakan untuk menentukan sebuah lokasi atau alamat dari suatu halaman Web. Pada URL biasanya terdiri dari Protokol, Nama domain, dan path pada suatu halaman."

    pa "Lalu kita akan berlanjut pada jenis web berdasarkan teknologinya. Terdapat dua jenis web yaitu Statis dan Dinamis."

    pa "Web Statis merupakan sebuah Web dimana penggunanya tidak dapat mengubah isi atau konten suatu Web tersebut langsung menggunkan browser. Jadi yang interaksinya cuma mengakses dan melihat informasi yang ada."

    pa "Web Dinamis merupakan sebuah web yang memiliki interaksi secara kompleks. Pengguna atau client mampu mengubah isi atau konten suatu web dengan mengirim request pada sisi server, 
    lalu server akan menampilkan isi yang berbeda sesuai dengan alur program yang ada."

    "Kemudian pembelajaran diteruskan dengan praktek pengaksesan halaman web secara langsung dan penjelasan masing-masing."

    hide screen web_1_2

    scene bg campus class with fade

    "Sebelum perkuliahan ditutup, [pa] meninggalkan sebuah tugas untuk mata kuliah Pemorgaman Web."

    pa normal "Ini bapak siapkan tugas, nanti kalian kerjakan dan kumpulkan jadi satu sebelum dikirim ke saya ya…"

    $ my_task.addTask(task_web_1)

    pa "Ya sudah kalau begitu, bapak tutup pertemuan kali ini, terimakasih dan sampai jumpa di pertemuan berikutnya."

    t normal "Terimakasih…."

    t "Terimakasih…."

    "Pengajar meninggalkan ruang kelas, dan perkuliahan hari ini berakhir."

    "Kamu mengemas barang-barangmu dan pergi meninggalkan ruang kelas."

    "Dengan berakhirnya kuliah untuk hari ini, tidak ada tujuan lain selain pulang ke kos."

    "Sesampainya di tempat parkir, kamu langsung mengendarai motormu untuk pulang."

    call attend_web
    call attend_class

    call change_timephase
    call screen mapUI with dissolve

label web_2:

    "Web 2"

    call screen mapUI with dissolve

label web_3:

    "Web 3"

    call screen mapUI with dissolve

label web_4:

    "Web 4"

    call screen mapUI with dissolve

label attend_web:

    $ a_webA +=1
    $ a_webN +=8

    return


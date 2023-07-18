
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

    scene bg campus class with dissolve

    call awal_kelas

    scene bg campus class with fade

    pa normal "Selamat siang teman-teman, bertemu lagi kita pada siang hari ini…"

    "[pa] memasuki ruang kelas, suasana kelas yang semula ramai menjadi sepi."

    pa "Pada pertemuan siang hari ini kita akan membahas mengenai teknologi-teknologi yang digunakan pada pemrograman web."

    show screen web_2_1 with fade

    pa "Pertama yang sudah dibahas pada minggu lalu yaitu Browser, browser merupakan sebuah perangkat lunak yang memiliki fungsi untuk menerima dan menyajikan informasi yang ada pada web."

    pa "Kedua HTML, atau HyperText Markup Language merupakan sebuah bahasa markah standar untuk dokumen yang ditampilkan diinternet. 
    HTML menggunakan tanda-tanda atau sering disebut tag untuk menyatakan kode-kode ditafsirkan oleh browser untuk ditampilkan."

    pa "Secara umum fungsi HTML adalah untuk mengelola serangkaian data dan informasi sehingga suatu dokumen dapat diakses dan ditampilkan di internet melalui layanan web."

    pa "HTML secara umum juga memiliki tiga komponen yaitu Tag, Elemen, dan Atribut."

    hide screen web_2_1

    show screen web_2_2 with fade

    pa "Tag merupakan komponen HTML yang menjadi tanda awal dan akhiran dalam perintah HTML. Tag menggunakan tanda kurung siku < … > , 
    diantara kedua kurung siku tersebut biasanya diisi nama tag. Terdapat 2 macam tag, yaitu pembuka <..> dan penutup </..>."

    pa "Tag memiliki bermacam-macam fungsi, semisal tag <title> .. </tittle> berfungsi untuk memberi judul halaman, 
    tag <bold>.. </bold> berfungsi untuk menebalkan suatu teks."

    pa "Kemudian Element, Element merupakan komponen HTML yang berisi keseluruhan dari tag pembuka, konten, dan tag penutup."

    pa "Semisal contoh <bold> Teks ini akan di bold </bold> berisi tag pembuka <bold>, isi atau konten ‘Teks ini akan di bold’, dan tag penutup </bold>. 
    Keseluruhan hal tersebut disebut dengan elemen. Dalam satu elemen dapat juga berisi elemen lainnya."

    hide screen web_2_2

    show screen web_2_3 with fade

    pa "Lalu ada komponen Atribut, komponen ini merupakan informasi atau perintah tambahan pada suatu elemen untuk memperjelas perintah atau apa yang akan dilakukan oleh suatu tag."

    pa "Semisal contoh <a href=”laman.com”> …. </a>, elemen tersebut memiliki fungsi ketika elemen itu dipilih akan mengantarkan kita pada suatu halaman web bernama laman.com. Tag <a> pada contoh tersebut memiliki atribut yaitu ‘href’."

    pa "Selain itu fungsi-fungsi dari HTML yang lain adalah sebagai berikut."

    pa "Membuat struktur halaman web."

    pa "Menambahkan konten website."

    pa "Mengatur format dan tata letak konten yang ada didalamnya."

    pa "Mampu mengarahkan dari suatu halaman ke halaman web lainnya."

    hide screen web_2_3

    show screen web_2_4 with fade

    pa "Lalu komponen web yang ketiga, CSS atau Cascading Style Sheets merupakan bahasa yang digunakan untuk menampilkan tampilan dan format pada suatu halaman website. 
    Bahasa ini dapat digunakan untuk mengganti semisal warna font, warna background, menambah margin padding, dan lain sebagainya."

    pa "Selain itu, CSS juga berfungsi untuk Mempercepat loading halaman web."

    pa "Memudahkan pengelolaan kode."

    pa "Menawarkan lebih banyak variasi tampilan, dan"

    pa "Membuat website tampil lebih rapi disemua layar."

    pa "Lalu yang berikutnya ada Javascript, Javascript merupakan salah satu bahasa pemrograman 
    dimana dalam pemrograman web biasanya digunakan untuk membuat suatu halaman web menjadi lebih dinamis."

    pa "Dengan menggunakan Javascript pada suatu halaman web, web menjadi lebih dinamis semisal ketika pengguna memilih atau menekan tombol 
    maka kode program Javascript mampu merubah tata letak konten dari suatu halaman tersebut."

    hide screen web_2_4

    show screen web_2_5 with fade

    pa "Kemudian sebelum saya lupa, disini terdapat 2 macam jenis pemrograman web."

    pa "Yaitu Client Side Programming dan Server Side Programming."

    pa "Client Side Programming merupakan jenis bahasa pemrograman yang diterjemahkan dan  pengolahannya dilakukan oleh sisi client. 
    Kode pemrograman diterjemahkan oleh browser yang menjadi sisi client."

    pa "Contoh bahasa pemrograman yang ada pada Client Side Programming adalah HTML, CSS, Javascript dan lain sebagainya."

    pa "Sementara Server Side Programing merupakan bahasa pemrograman yang diterjemahkan dan pengelolaannya dilakukan pada sisi server. 
    Source code atau kode pemrograman tidak akan terlihat dari sisi client(browser)."

    pa "Contoh bahasa pemrograman yang ada pada Server Side Programming adalah PHP, SQL, dan lain sebagainya."
    
    hide screen web_2_5

    "[pa] Kemudian memberikan contoh dan praktik langsung dari materi yang diterangkan."

    "Pembelajaran berlanjut hingga waktu perkuliahan berakhir."

    "Kemudian tanya jawab masih terus berlangsung pada mahasiswa lain hingga jam perkuliahan selesai."

    pa "Saya kira cukup untuk pertemuan kali ini, sampai ketemu minggu depan teman-teman."

    r normal2"Terimakasih pak…"

    t normal "Terimakasih…"

    "[pa] meninggalkan ruang kelas, dan pertemuan PBO pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk pulang."

    call attend_web
    call attend_class

    if hima == True:
        call pengumuman_hima
    else:
        scene bg black with fade
        pause 1.5

        "Sebelum sempat meninggalkan ruangan, tiba-tiba [r] berdiri dan meminta perhatian."

        r normal2 "Uhmm teman-teman minta perhatiannya sebentar, buat yang belum tahu UTS kan dimulai dari minggu depan aku mau ngumumin sesutatu tentang UTS."

        t normal "Ha? UTS beneran dimulai minggu depan?"

        t "Aduhh bisa gak ya aku?"

        r "Iya dimulai minggu depan, untuk informasinya sendiri bisa kalian cek di Simaster."

        r "Tapi garis besarnya, UTS kita nanti kita jadwalnya seperti minggu-minggu biasa."

        r "Kemudian untuk materinya sendiri untuk semua mata kuliah ya yang sudah pernah diajarkan selama ini."

        r "Dan untuk UTS sendiri kalian nanti {b}perlu mengeprint kartu ujian{/b} kalian sendiri-sendiri ya, bisa diambil {b}dari Simaster{/b} nanti kartunya."

        "Mendengar [r] mengumumkan pengumuman untuk UTS minggu depan, mahasiswa langsung memeriksa akun Simaster mereka masing-masing."

        r "Mungkin itu dulu ya? Lebih lengkapnya nanti kalian bisa cek sendiri-sendiri atau tanya ke dosen akademik masing-masing."

        t "Okee makasih infonya [r]."

        t "Makasih [r]!!"

        "Setelah pengumuman selesai diumumkan mahasiswa meninggalkan ruangan."

        "Kamu meninggalkan ruang kelas dan langsung menuju tempat parkir."

        scene bg black with dissolve

        "Setelah menyalakan mesin motormu, kosan bukanlah tempat pertama yang kamu tuju."

        "Kamu mengendarai motor menuju tempat untuk mengeprint kartu ujian."

        "Setelah selesai mengeprint kosan merupakan tempat selanjutnya yang kamu tuju."
        

    call change_timephase
    call screen mapUI with dissolve

label uts_web:

    scene bg campus class with dissolve

    "Selesai dengan waktu istirahat kelas untuk ujian berikutnya sudah dibuka."

    "Setelah memastikan dimana posisi tempat dudukmu, kamu memasuki ruang kelas tersebut."

    "Dosen pengawas juga sudah menunggu di dalam kelas dan menyuarakan instruksi kepada semua mahasiswa yang ada."

    scene bg campus class with fade

    "Sesuai yang intruksi dari dosen pengawas ujian, tas-tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Sama seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    "bn normal Selamat siang teman-teman pada siang hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Pemrograman Web."

    "bn Saya harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    "bn Soal akan saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    "bn Saya harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Basis Data ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

    "Merasa cukup dengan persiapanmu, kamu mulai mengisi biodata pada lembar jawab sebelum mulai menelaah soal-soal UTS yang ada."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    "(Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    "(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)"

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    menu:
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS."
    "1. Kumpulan halaman-halaman web yang menampilkan informasi dengan berbagai macam bentuk dan dihubungkan menggunakan hyperlink disebut?"
    menu:
        "A. Websites.":
            "A. Websites."
            $a_webTS +=20
        "B. Laman.":
            "B. Laman."
        "C. URL.":
            "C. URL."
        "D. HTTP.":
            "D. HTTP."
        "E. Web.":
            "E. Web."
    "2. Dibawah ini yang kita perlukan sewaktu akan mengakses web adalah?"
    menu:
        "A. URL laman tujuan.":
            "A. URL laman tujuan."
        "B. Browser.":
            "B. Browser."
        "C. Client.":
            "C. Client."
        "D. Server.":
            "D. HTTP."
        "E. Akun admin.":
            "E. Akun admin."
            $a_webTS +=20
    "3. Sebuah protokol standard yang menyediakan aturan dalam proses pengaksesan sebuah halaman Web. Merupakan sebuah pengertian dari?"
    menu:
        "A. Websites.":
            "A. Websites."
        "B. HTML.":
            "B. HTML."
        "C. URL.":
            "C. URL."
        "D. HTTP.":
            "D. HTTP."
            $a_webTS +=20
        "E. Web.":
            "E. Web."
    "4. Pernyataan yang benar mengenai URL adalah?"
    menu:
        "A. URL merupakan protokol standard yang dibutuhkan untuk mengakses web.":
            "A. URL merupakan protokol standard yang dibutuhkan untuk mengakses web."
        "B. URL merupakan perangkat lunak yang digunakan untuk menerima dan menyajikan informasi yang ada di web.":
            "B. URL merupakan perangkat lunak yang digunakan untuk menerima dan menyajikan informasi yang ada di web."
        "C. URL merupakan salah satu bahasa pemrograman yang digunakan untuk membuat suatu halaman web menjadi lebih rapi.":
            "C. URL merupakan salah satu bahasa pemrograman yang digunakan untuk membuat suatu halaman web menjadi lebih rapi."
        "D. URL merupakan sebuah alamat dari suatu website yang ada di internet.":
            "D. HTTP."
            $a_webTS +=20
        "E. URL hanya terdiri dari protokol html saja.":
            "E. Web." 
    "5. Dibawah ini yang bukan komponen dari HTML adalah?"
    menu:
        "A. Tag, Element, dan Atribut.":
        "B. Tag, Element, dan Body":
        "C. Head, Body, dan Footer":
        "D. Head, Body, dan Atribut":
        "E. CSS, JavaScript, PHP":
    
    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengkoreksi dan meneliti kertas jawaban dan biodatamu selama beberapa kali akhirnya kamu beranjak dari tempat dudukmu."

    "Mengumpulkan kertas ujian, kemudian memasukan barang-barangmu pada tas yang sebelumnya sudah dikelompokan dengan rapi di depan kelas."

    "Keluar dari kelas, kamu merasa sangat lelah. Badan dan pikiranmu keduanya meminta dirimu untuk beristirahat."

    "Ujian pada hari ini telah berakhir, kamu langsung menuju motormu yang berada di parkiran kampus."

    "Setelah menyalakan mesin motor, kamu langsung mengendarainya menuju kosan."

    call change_timephase
    call screen mapUI



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


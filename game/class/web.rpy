
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

    bn normal "Selamat siang teman-teman pada siang hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Pemrograman Web."

    bn "Saya harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    bn "Soal akan saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    bn "Saya harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

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
        "D. Merupakan alamat web yang mengarahkan ke suatu websites, halaman web, atau dokumen tertentu.":
            "D. Merupakan alamat web yang mengarahkan ke suatu websites, halaman web, atau dokumen tertentu."
            $a_webTS +=20
        "E. URL hanya terdiri dari protokol html saja.":
            "E. Web." 
    "5. Dibawah ini yang merupakan komponen dari HTML adalah?"
    menu:
        "A. Tag, Element, dan Atribut.":
            "A. Tag, Element, dan Atribut."
            $a_webTS +=20
        "B. Tag, Element, dan Body":
            "B. Tag, Element, dan Body"
        "C. Head, Body, dan Footer":
            "C. Head, Body, dan Footer"
        "D. Head, Body, dan Atribut":
            "D. Head, Body, dan Atribut"
        "E. CSS, JavaScript, PHP":
            "E. CSS, JavaScript, PHP"
    
    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengkoreksi dan meneliti kertas jawaban dan biodatamu selama beberapa kali akhirnya kamu beranjak dari tempat dudukmu."

    "Mengumpulkan kertas ujian, kemudian memasukan barang-barangmu pada tas yang sebelumnya sudah dikelompokan dengan rapi di depan kelas."

    "Keluar dari kelas, kamu merasa sangat lelah. Badan dan pikiranmu keduanya meminta dirimu untuk beristirahat."

    "Ujian pada hari ini telah berakhir, kamu langsung menuju motormu yang berada di parkiran kampus."

    "Setelah menyalakan mesin motor, kamu langsung mengendarainya menuju kosan."

    call change_timephase
    call screen mapUI

label web_3:

    scene bg campus class with dissolve

    "Setelah jam istirahat berakhir, kamu dan teman-temanmu mulai memasuki kelas yang akan digunakan untuk jam perkuliahan terakhir pada hari ini."

    "Ketika memasuki ruang kelas, [pa] yang mengajar mata kuliah Pemrograman Web I telah berada di dalam ruang kelas."

    pa normal "Selamat siang teman-teman, silahkan masuk sembari menunggu teman-teman yang lain masuk kelas."

    "Tidak memakan waktu lama, satu persatu teman kelasmu memasuki ruangan, setelah dirasa mahasiswa yang berada dalam ruangan sudah banyak, [pa] membuka pertemuan pada siang hari ini."

    pa "Selamat siang, sepertinya teman-temannya sudah pada hadir sekarang… Kalau begitu bapak mulai kelas pada siang hari ini."

    pa "Bertemu lagi kita pada mata kuliah Pemrograman Web I pertemuan ke 3. Pada pertemuan siang hari ini, kita akan mencoba membuat sebuah halaman web menggunakan HTML dasar."

    pa "Dimana laman tersebut akan kita isi dengan beberapa tag dasar HTML."

    pa "Kita mulai saja, agar menghemat waktu pertemuan kali ini."

    show screen web_3_1 with fade

    pa class "Langkah pertama yang kita lakukan adalah membuat sebuah file pada teks editor seperti, Notepad++, Sublime Text, 
    Visual Studio Code, dan lain sebagainya kemudian menyimpannya dengan ekstensi .html."

    pa "Dengan membuat file dan menyimpannya dalam ekstensi .html kita berhasil membuat sebuah dokumen html."

    pa "Disini bapak menyimpan file tersebut dengan nama latihan.html ya teman-teman."

    pa "Kemudian setelah itu, pada baris pertama kita tuliskan <!DOCTYPE html>, hal ini merupakan sebuah deklarasi yang menyatakan tipe dokumen, dan dokumen ini menggunakan HTML5."

    pa "Lalu dilanjutkan kan dengan tag buka <html> dan dibaris yang paling bawah pada dokumen ini ditutup dengan tag tutup </html>."

    pa "Kurang lebih seperti pada gambar yang ada ya."

    hide screen web_3_1

    show screen web_3_1g with fade

    pa "Setelah itu kita menambahkan tag <head> dan </head> dalam tag <html> yang sudah ada."

    hide screen web_3_1g

    show screen web_3_2 with fade

    pa "<head> merupakan bagian kepala dari dokumen HTML, bagian ini merupakan bagian yang memiliki fungsi untuk menyertakan informasi tentang dokumen. Informasi tersebut seperti 
    judul dokumen, metadata, dan kode untuk menghubungkan dokumen dengan file css, js, dan dokumen eksternal lainnya."

    pa "Susunan dokumen html yang kita buat, akan menjadi seperti ini."

    pa "Pada <head> bapak tambahkan tag <title> dengan nama Latihan HTML, yang berfungsi untuk memberi nama dokumen pada tab browser. "

    pa "Kemudian, setelah menyelesaikan tag <head>, dibawahnya kita tambahkan tag <body> yang merupakan bagian isi dari dokumen. "

    pa "Pada bagian <body> kita bisa menambahkan semua konten yang kita inginkan, seperti teks, gambar, tabel, dan elemen lainnya di dalam tag body ini."

    pa "Struktur dokumen yang kita buat akan menjadi seperti ini."

    hide screen web_3_2

    show screen web_3_2g with fade

    pa "Pada hari ini kita mempelajari mengenai tag yang digunakan untuk teks, dan heading, daftar, dan gambar."

    pa "Pertama, kita akan mulai dengan mengisi dokumen dengan teks <h1>, tag tersebut merupakan teks header untuk teks yang ada di dokumen."

    hide screen web_3_2g

    show screen web_3_3 with fade

    pa "Tag header tersebut dapat kita atur ukurannya dengan mengubah angka yang berada setelah huruf ‘h’. 
    Kita bisa mengubahnya dari angka 1 sampai angka 6, dimana angka 1 merupakan ukuran terbesar dan angka 6 adalah ukuran terkecil."

    pa "Kali ini bapak akan menuliskan teks , “Ini adalah header” menggunakan beberapa macam teks header."

    hide screen web_3_3

    show screen web_3_3g with fade

    pa "Dokumen htmlnya akan menjadi seperti gambar ini."

    pa "Lalu untuk membuka dokumen ini pada browser, kita bisa memilih file dan membukanya dengan browser yang kita punya."

    pa "Setelah kita membuka file tersebut, kita dapat melihat hasilnya seperti pada gambar dibagian kanan."

    pa "<title> yang kita tulis dapat dilihat hasilnya pada judul dari browser tab yaitu, Latihan HTML."

    pa "Lalu kita juga dapat melihat hasil dari teks yang kita tulis memiliki ukuran teks yang berbeda beda, sesuai kode dan tag yang kita tulis."

    pa "Setelah itu, kita akan mencoba menuliskan tag paragraf <p>, tag tersebut memiliki fungsi seperti mengatur paragraf, mengatur spasi, dan penggunaan style ketika menggunakan CSS."

    hide screen web_3_3g

    show screen web_3_4 with fade

    pa "Dokumen html yang kita buat akan menjadi seperti ini."

    pa "Sementara tampilan pada htmlnya akan terlihat seperti ini."

    hide screen web_3_4

    show screen web_3_4g with fade

    pa "Setelah mencoba tag paragraf, yang akan pelajari terakhir pada hari ini adalah menggunakan tag untuk membuat sebuah daftar atau list."

    hide screen web_3_4g

    show screen web_3_5 with fade

    pa "Terdapat dua macam tag yang ada, <ul> merupakan tag untuk membuat daftar yang tak terurut seperti daftar dengan simbol-simbol, 
    dan <ol> merupakan tag untuk daftar yang terurut seperti dengan nomor."

    pa "Kemudian tiap-tiap elemen yang terdapat dalam daftar, dimasukan menggunakan elemen <li> atau list item."

    pa "Lihat dokumen html yang sudah bapak beri contoh dari daftar yang tidak terurut dan terurut pada gambar setelah ini."

    hide screen web_3_5

    show screen web_3_5g with fade

    pa "Kemudian ketika kita buka pada browser akan terlihat menjadi seperti gambar yang terdapat pada bagian kanan."

    pa "Perbedaan antara penggunaan <ul> dan <ol> bisa dilihat ya, <ul> digunakan untuk list pertama, dan <ol> digunakan untuk list kedua."

    pa "Penggunaan mana yang lebih baik ya tergantung bagaimana kalian ingin menampilkannya saja."

    pa "Kurang lebih begitu untuk tag daftar atau list yang kita bisa gunakan dalam html ya. Jika kalian ingin mengetahui lebih, bisa ditanyakan nanti."

    pa "Jadi hari ini, kita telah mempelajari bagaimana membuat file html, mempelajari tag dan struktur dasar html, lalu mencoba beberapa tag untuk teks, lalu membuat list."

    hide screen web_3_5g with fade

    pa "Mungkin untuk hari ini cukup sampai sini dulu ya, kita lanjutkan lagi untuk besok pembahasan mengenai htmlnya. 
    Besok kita akan mempelajari mengenai tabel dan form."

    pa  "Untuk perkuliahan hari ini, kita lanjutkan dengan sesi tanya jawab ya, kalau kalian ada pertanyaan untuk materi pada hari ini, 
    bisa kalian tanyakan sekarang."

    "Pembelajaran berlanjut pada sesi tanya jawab. Sesi tanya jawab masih terus berlangsung pada mahasiswa lain hingga jam perkuliahan selesai."

    pa "Saya kira cukup untuk pertemuan kali ini, terimakasih atas partisipasinya pada perkuliahan hari ini dan sampai ketemu minggu depan teman-teman."

    r normal2 "Terimakasih pak…"

    t normal "Terimakasih…"

    "[pa] meninggalkan ruang kelas, dan pertemuan ke-3 mata kuliah Web I pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk pulang."

    call attend_web
    call attend_class

    call change_timephase
    call screen mapUI with dissolve

label web_4:

    scene bg campus class with dissolve

    pa normal "Selamat siang teman-teman, bagaimana kabarnya? Semoga baik-baik saja ya."

    "[pa] memasuki ruang kelas, pertanda perkuliahan mata kuliah Web I akan segera dimulai."

    pa "Seperti yang kalian ketahui, hari ini merupakan hari pertemuan terakhir untuk mata kuliah Web I, dan seperti yang bapak bilang kemarin, 
    hari ini kita akan mempelajari mengenai table dan form pada HTML"

    pa "Minggu lalu kita sudah membuat sebuah dokumen HTML yang sudah kita coba tambahkan beberapa tag seperti header, paragraf, dan list."

    pa "Minggu ini kita masih akan menggunakan file tersebut untuk mempelajari materi berikutnya teman-teman."

    "[pa] menyiapkan materi yang akan dipaparkan pada perkuliahan. Setelah materi sudah terlihat pada depan kelas, perkuliahan pun dimulai."

    scene bg campus class with dissolve

    pa normal "Materi pertama yang akan kita pelajari hari ini adalah membuat sebuah tabel menggunakan HTML."

    show screen web_4_1 with fade

    pa class "Menggunakan HTML kita bisa membuat sebuah tabel dengan tag <table>, namun kita perlu memasukkan tag lainnya untuk mengatur berapa banyak kolom dan baris yang ada di dalam tabel tersebut. "

    pa "<tr> digunakan untuk membuat baris dalam tabel, sementara <td> dapat kita gunakan untuk menambahkan kolom dalam tabel."

    pa "Pada baris pertama dalam tabel kita bisa menggunakan tag <th> yang merupakan tag untuk membuat baris header dalam sebuah tabel dan menjadi tebal(bold)."

    pa "Bapak sudah menambahkan sebuah tabel pada dokumen HTML yang kita buat kemarin."

    pa "Tabel yang bapak tambahkan adalah tabel mahasiswa dengan 3 kolom di dalamnya yaitu, nama, nim, dan program studi. Tabel tersebut sudah bapak isi dengan 2 data mahasiswa."

    hide screen web_4_1

    show screen web_4_1g with fade

    pa "Berikut dokumen HTML yang sudah bapak tambahkan tabelnya pada gambar bagian kiri."
    
    pa "Lalu ketika bapak buka file HTML ini dalam browser, akan terlihat seperti gambar bagian kanan."

    pa "Tabel yang baru saja dibuat telah berhasil dibuat, namun tabel tersebut masih belum jelas bentuknya karena belum memiliki border."

    hide screen web_4_1g

    show screen web_4_2 with fade

    pa "Untuk menambahkan atribut border dalam tabel tersebut, kita bisa menuliskan border setelah tag pembuka <tabel>, dan akan menjadi seperti ini, <table border=”1”>"

    pa "Lalu tampilan dalam browser akan menjadi seperti gambar yang ada dibawah ini."

    pa "Sekarang kalian bisa melihat perbedaannya kan, terdapat border yang memisahkan tiap baris dan kolom dalam tabel tersebut."

    pa "Kurang lebih untuk membuat tabel sederhana seperti itu ya."

    pa "Kalian bisa menambahkan <tr> untuk menambah baris, dan <td> untuk menambah kolom dan data."

    pa "Kemudian kita akan berlanjut pada materi berikutnya yaitu, form."

    hide screen web_4_2

    show screen web_4_3 with fade

    pa "Form dapat kita gunakan untuk membuat formulir interaktif dalam sebuah laman yang memungkinkan untuk memasukan data atau mengirimkan data pada suatu server."

    pa "Kali ini kita hanya akan mempelajari bagaimana cara untuk membuat form, namun hanya tampilan saja tanpa ada perpindahan data pada server."

    pa "Tag yang bisa kita gunakan untuk membuat sebuah form adalah <form>. Kemudian terdapat <label> yang berfungsi untuk menampilkan instruksi atau teks yang ada sebelum elemen input."

    pa "Lalu elemen yang kita gunakan untuk memasukan data adalah <input>, <input> sendiri memiliki berbagai macam atribut yang dapat digunakan untuk menentukan tipe input yang kita inginkan."

    pa "Semisal kita ingin memasukan input dengan tipe data teks, kita dapat menggunakan atribut “text”, ketika ingin memasukan tanggal pada form kita dapat menggunakan tipe input “date”, 
    dan masih banyak lagi tipe input yang dapat kita gunakan sesuai kebutuhan kita."

    pa "Bapak disini sudah memberi contoh membuat sebuah form, yang berisikan 3 input yaitu nama, nomor induk, dan program studi."

    hide screen web_4_3

    show screen web_4_3g with fade

    pa "Dapat dilihat, pada label “Nama”, terdapat input dengan tipe “text”. 
    Lalu dibelakangnya jika kalian memperhatikan ada required, required menandakan input tersebut harus diisi sebelum bisa di submit."

    pa "Dibawahnya terdapat label dan input untuk “NIM”, dan “Prodi”. Kemudian pada baris terakhir sebelum form berakhir, terdapat input dengan 
    tipe <submit> yang merupakan sebuah tombol yang dapat ditekan untuk mengirimkan data yang dituliskan pada kolom input sebelumnya."

    pa "Hasil dari form yang dituliskan pada browser tampak seperti gambar diatas."

    pa "Terdapat label Nama, NIM, dan Prodi dengan masing-masing kolom inputnya."

    pa "Lalu pada bagian terakhir terdapat tombol submit untuk memasukan atau mengirimkan data yang kita input."

    pa "Ya untuk pengenalan form pada HTML sekiranya segini dulu ya, 
    untuk informasi yang lebih kalian dapat mencari tahu di internet sendiri."

    hide screen web_4_3g with dissolve

    pa normal "Karena waktu yang sudah mepet, jika kalian ingin bertanya mengenai materi bisa ditanyakan ya."

    "Tidak lama kemudian, [r] langsung mengangkat tangannya dan langsung ditunjuk oleh [pa]."

    r normal2 "Pak, untuk materi ujian akhirnya dari mana ya pak?"

    pa "Materi untuk ujian akhir semesternya dapat dimulai dari materi setelah UTS ya teman-teman."

    t normal "Berarti materi pertemuan ke-3 dan hari ini ya pak?"

    pa "Yak, betull."

    t "Baik pak terimakasih."

    "Sesi pertanyaan masih berlanjut hingga waktu perkuliahan berakhir."

    "Tidak lupa [pa] juga meninggalkan tugas untuk dikerjakan sebelum ujian akhir dimulai."

    "Sebelum perkuliahan ditutup, [pa] meninggalkan sebuah tugas untuk mata kuliah Pemorgaman Web."

    pa normal "Ini bapak siapkan tugas, nanti kalian kerjakan dan kumpulkan jadi satu sebelum dikirim ke saya ya…"

    $taskweb = True
    call n_task
    "Setelah waktu perkuliahan telah habis, [pa] kemudian menutup pertemuan terakhir pada hari ini."

    scene bg black with Dissolve(1.5)

    scene bg campus class with dissolve

    pa normal "Kalau begitu bapak tutup pertemuan hari ini. Selamat belajar dan semoga mendapatkan hasil yang diinginkan pada ujian nanti."

    pa "Terimakasih sudah mengikuti kelas sampai pertemuan kali ini, sampai jumpa pada pertemuan selanjutnya teman-teman."

    t normal "Terimakasih pak."

    t "Terimakasihhh"

    r normal2 "Terimakasih juga pak."

    "Dengan begitu kelas ditutup dan pembelajaran untuk hari ini telah usai. 
    Kamu keluar dari ruangan kelas dan melanjutkan aktivitasmu berikutnya."

    call attend_web
    call attend_class

    call change_timephase
    call screen mapUI with dissolve

label uas_web:

    scene bg campus upper hall with dissolve

    "Selesai menggunakan jam istirahat, kamu kembali ke area dimana teman-temanmu sedang belajar bersama."

    "Sama seperti sebelumnya, terlihat mahasiswa-mahasiswa lain juga sedang membaca materi perkuliahan yang akan diujikan."

    "Masih tersisa sekitar 10 menit lagi sebelum ujian terakhir pada hari ini dimulai."

    "Kamu duduk bersandar di tembok kelas sembari mengingat materi yang telah kamu pelajari."

    "Mengisi beberapa menit sebelum ujianmu dengan mengingat-ingat materi perkuliahan sebelum mengikuti ujian berikutnya."

    "Tidak lama kemudian pintu ruang kelas ujian dibuka, satu persatu mahasiswa memasuki ruang kelas, kemudian kamu juga ikut berdiri dan bergegas masuk ke ruang ujian."

    scene bg campus class with fade

    "Sebelum memasuki ruang kelas ujian tak lupa dirimu sempat mengecek dimana bangku ujian terakhir untuk hari ini."

    "Setelah mengetahui dimana bangku ujian mu, kamu memasuki ruang kelas dan melihat dosen pengawas ujian yang sudah duduk dan siap menjelaskan instruksi ujian."

    "Memasuki ruang kelas ujian, dosen pengawas ujian memberi instruksi kepada mahasiswa seperti instruksi yang ada pada ujian sebelumnya."

    "Meletakkan tas atau ransel di depan kelas secara rapi. Lalu hanya membawa peralatan tulis dan kartu mahasiswa ke bangku ujian."

    "Setelah meletakan tas ransel milikmu di depan ruang kelas, kamu mengambil peralatan tulis sebelum berjalan menuju bangku ujianmu."

    "Terlihat lembar jawab ujian sudah diletakan pada masing-masing bangku ujian."

    "Kemudian ketika semua bangku ujian telah terisi oleh peserta ujian, dosen pengawas lalu menjelaskan peraturan ujian."

    "Tidak ada yang berbeda seperti peraturan-peraturan ujian pada umumnya."

    "Selesai menjelaskan, beberapa menit kemudian soal ujian disebarkan kepada seluruh peserta yang ada."

    "Kamu menerima beberapa soal ujian dari bangku yang ada di depanmu, setelah mengambil salah satu soal ujian, kamu meneruskan pembagian soal-soal ujian lainnya ke bangku yang ada di belakangmu."

    "Dosen pengawas telah memberi instruksi jika ujian sudah dimulai, dan mahasiswa bisa mulai mengerjakan soal ujian."

    "Kamu berdiam dan berdoa terlebih dahulu sebelum mulai mengisi lembar jawaban dengan identitas dirimu."

    "Membuka lembar soal ujian, terdapat beberapa panduan pengerjaan soal pada bagian atas lembar. Kamu menyempatkan diri untuk membaca beberapa panduan pengerjaan tersebut."

    "({i}Ketika {b}UAS{/b} terdapat 5 soal pilihan ganda yang harus dikerjakan untuk menyelesaikan ujian{/i})"

    "({i}Setiap pertanyaan akan ditampilkan dan akan muncul dalam waktu 45 detik{/i})"

    "({i}Ketika waktu 90 detik habis, soal akan hilang dari layar{/i})"

    "({i}Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya{/i})"

    "({i}Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal{/i})"

    "({i}Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.{/i})"

    "({i}Perlu diketahui UTS pada kampus dapat dilaksanakan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.{/i})"

    "({i}Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.{/i})"

    "Selesai membaca panduan pengerjaan pada lembar soal, kamu lalu bersiap menjawab soal-soal ujian yang ada."

    "Mulai mengerjakan UAS?"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UAS"

    "Soal pertama yang terdapat lembar soal adalah:"

    label soalweb1:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_web1'

        show screen webas_1 with dissolve
        "1. Pada sebuah struktur sebuah HTML, dimana kita meletakan informasi tentang dokumen seperti judul dan meta data?"

        mc normal jacket "Judul itu kayaknya bagian atas, namanya apa ya?"
        show screen countdown
        menu:

            "A. <body>":
                "a. <body>"
                mc "body??"

            "B. <head>":
                "b. <head>"
                "mc <head> yaa, ini pasti diatas kalo di strukturnya sih."
                $ a_webAS += 5

            "C. <html>":
                "c. <html>"
                mc "html kan dokumennya….."

            "D. <title>":
                "d. <title>"
                mc "Itu buat judul aja, terus meta datanya?"
        hide screen countdown
        "Kamu menjawab pertanyaan pertama dengan lancar, setelah beberapa kali memeriksa jawaban kamu yakin akan jawaban pertamamu."
        hide screen webas_1 with dissolve
        jump soalweb2

    label telat_web1:
        "Kamu terlambat menjawab pertanyaan, soal no 1 dilewati"

    hide screen webas_1 with dissolve

    label soalweb2:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_web2'

        show screen webas_2 with dissolve
        "Kemudian kamu lanjut menuju pertanyaan selanjutnya."

        "2. 	Manakah dibawah ini merupakan pernyataan yang benar mengenai syntax untuk membuat daftar atau list?"
        show screen countdown
        menu:

            "A. <ul> digunakan untuk membuat daftar terurut":
                "a. <ul> digunakan untuk membuat daftar terurut"
                mc "Hmmm…."

            "B. <ol> digunakan untuk membuat daftar terurut":
                "b. <ol> digunakan untuk membuat daftar terurut"
                mc "Yayayaya…."
                $ a_webAS += 5

            "C. <il> digunakan untuk membuat daftar terurut":
                "c. <il> digunakan untuk membuat daftar terurut"
                mc "il ???"

            "D. <ul> dan <ol> digunakan untuk membuat daftar terurut":
                "d. <ul> dan <ol> digunakan untuk membuat daftar terurut"
                mc "Kayanya engga keduanya deh…"
        hide screen countdown
        "Berhasil menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."
        hide screen webas_2 with dissolve
        jump soalweb3

    label telat_web2:
        "Kamu terlambat menjawab pertanyaan, soal no 2 dilewati"

    hide screen webas_2 with dissolve

    label soalweb3:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_web3'

        show screen webas_3 with dissolve
        "3. Manakah syntax yang digunakan untuk membuat baris pertama menjadi tebal pada sebuah tabel pada HTML?"
        show screen countdown
        menu:

            "A. <tr>":
                "a. <tr>"
                mc "tr… tr… tabel row?"

            "B. <td>":
                "b. <td>"
                mc "td itu apa yaa??."

            "C. <table>":
                "c. <table>"
                mc "Yakin aku jawab ini huh..."
                $ a_webAS += 5

            "D. <th>":
                "d. <th>"
                mc "table header… yupss"
        hide screen countdown
        "Setelah menjawab pertanyaan nomor 3, kamu bergegas menuju pertanyaan selanjutnya."

        "Tersisa dua soal ujian lagi, merasa cepat ingin menyelesaikan quiz ini, kamu langsung membaca pertanyaan nomor 4."
        hide screen webas_3 with dissolve
        jump soalweb4

    label telat_web3:
        "Kamu terlambat menjawab pertanyaan, soal no 3 dilewati"

    hide screen webas_3 with dissolve

    label soalweb4:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_web4'

        show screen webas_4 with dissolve
        "4. 	Untuk membuat form yang berisi tanggal lahir dan tempat lahir baiknya kita menggunakan input type?"
        show screen countdown
        menu:

            "A. Number dan date":
                "a. number dan date"
                mc "Emang tanggal pakai number…"

            "B. Text dan date":
                "b. Text dan date"
                mc "Bukannya kebalik??"

            "C. Date dan text":
                "c. Date dan text"
                mc "Yang ini harusnya!"
                $ a_webAS += 5

            "D. Date dan number":
                "d. Date dan number"
                mc "kayaknya salah…"
        hide screen countdown
        "Selesai menjawab pertanyaan ke 4, kini hanya tinggal satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan ujian akhir Desain elementer pada pagi hari ini."

        "Setelah mengecek jawaban no 4, kamu langsung membaca soal terakhir yang terdapat pada lembar soal ujian."
        hide screen webas_4 with dissolve
        jump soalweb5

    label telat_web4:
        "Kamu terlambat menjawab pertanyaan, soal no 4 dilewati"

    hide screen webas_4 with dissolve

    label soalweb5:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_web5'

        show screen webas_5 with dissolve
        "5. Manakah dibawah ini yang tidak termasuk kedalam sebuah struktur dokumen HTML?"
        show screen countdown
        menu:

            "A. <hand>":
                "a. <hand>"
                mc "Hah hand?"
                $ a_webAS += 5

            "B. <footer>":
                "b. <footer>"
                mc "Harusnya ada sih kalau ini…."

            "C. <head>":
                "c. <head>"
                mc "Head ada kan??"

            "D. <body>":
                "d. <body>"
                mc "Body ada kannn?"
        hide screen countdown
        "Setelah memilih jawaban untuk pertanyaan terakhir, semua soal yang terdapat pada lembar soal ujian sudah kamu selesaikan."
        hide screen webas_5 with dissolve
        jump end_web

    label telat_web5:
        "Kamu terlambat menjawab pertanyaan, soal no 5 dilewati"

    hide screen webas_5 with dissolve

    label end_web:

        "Kamu melihat sekelilingmu, masih ada temanmu yang masih mengerjakan ujian, namun ada juga yang sudah beranjak dari bangku ujian."

        "Sebelum mengumpulkan jawaban, tidak lupa kamu mengecek apakah biodata dan jawaban yang kamu isi semuanya sudah benar."

        "Selesai mengecek, kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawaban ujianmu."

        "Lalu tidak lupa untuk mengambil tas ransel milikmu yang ketika ujian berlangsung diletakkan di depan kelas secara rapi."

        "Dengan selesainya ujian desain elementer pada siang hari ini, menandakan berakhirnya ujian pada hari ini."

        "Setelah menjalani 3 ujian akhir, ujian hari kedua telah usai, kini menyisakan satu hari ujian akhir lagi."

        "Kamu keluar dari ruangan sambil tersenyum lalu bergegas menuju kos untuk beristirahat."
        call change_timephase
        call screen mapUI


label attend_web:

    $ a_webA +=1
    $ a_webN +=8

    return


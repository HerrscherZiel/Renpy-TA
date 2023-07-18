
default a_alproA = 0
default a_alproT = 0
default a_alproC = 0
default a_alproTS = 0
default a_alproAS = 0
default a_alproN = 0

label pre_alpro:

    scene bg campus hall with dissolve

    "Setelah Pak Andy pergi meninggalkan ruangan, mahasiswa mengemas barang-barang yang mereka keluarkan bersiap meninggalkan ruangan." 
    
    "Ketika mahasiswa lain berjalan meninggalkan ruangan, tiba-tiba Rissa berdiri dan berjalan di depan kelas mengehentikan mereka lalu mengumumkan sesuatu."

    r normal2 "Halo teman-teman, sebelumnya untuk yang belum tahu kelas selanjutnya untuk kelas kita adalah pukul 9, kelas Algoritma Pemrograman, di ruang kelas U-202 yang berarti tepat di sebelah kiri kelas ini."

    r "Kemudian untuk jadwal kita selama satu minggu, aku udah buat ya... nanti akan aku share kalau udah jadi untuk yang kelas ini di group chat Lane."

    t normal "Okeee…"

    t "Makasih Rissa!"

    t "Berarti ini kita tinggal pindah ke sebelah aja kan, jam 9?"

    r "Iya sebentar lagi harusnya, atau mungkin kalau kelasnya kosong bisa langsung kita isi sih."

    t "Yuk pindah yuk…"

    "Melihat teman-temanmu mulai beranjak dari tempat duduk, kamu menyusul mereka dan keluar dari ruang kelas untuk berpindah ke ruang kelas berikutnya."

    jump alpro_1

label alpro_1:

    scene bg campus class with fade

    "Menempati ruang kelas yang baru, kamu kembali memilih tempat duduk pada baris no 3 dengan posisi bangku paling dekat dengan jendela."

    "Seperti kelas sebelumnya, tidak ada mahasiswa lain yang duduk tepat disebelahmu."

    "Selagi menunggu kelas dimulai, terdapat chat baru yang dikirimkan oleh Rissa mengenai jadwal perkuliahan."

    "Kamu membuka gambar yang dikirim oleh Rissa."

    call screen jadwal_kuliah with fade

    "{i}Untuk kembali mengakses halaman tersebut, kamu dapat menekan tombol jadwal yang ada di bagian kanan layar!!!{/i}"

    "{i}Kalendar juga kini dapat kamu akses, kamu dapat menekan tombol kalendar yang ada di bagian kanan layar!!!{/i}"

    show screen jadwal_btn with dissolve

    show screen kalendar_btn with dissolve

    mc normal jacket "Ohh begitu ya.. "

    call screen tutorial_jadwalkalender1

    "Selagi kamu menelaah jadwal yang ada, seorang dosen perempuan memasuki ruang kelas."

    siapa "Selamat pagi teman-teman! Haloo apa kabarnya?"

    t normal "Pagiii…"

    t "Selamat pagi bu…"

    "Dosen perempuan itu langsung duduk menempati bangku dosen yang ada, kemudian ia mengeluarkan laptop dari tas yang ia bawa."

    siapa "Iya… sebelumnya karena saya rasa ini pertemuan pertama kita, karena kalian belum kenal maka saya akan memperkenalkan diri dulu."

    siapa "Nama saya adalah Nira, kalian bisa manggil saya Bu Nira saja. Di kelas ini saya akan mengajar Algoritma Pemrograman, salam kenal teman-teman!"

    t "salam kenal bu Nira.."

    bn normal "Untuk mata kuliah ini perjanjian untuk tidak mengikuti kelas 3 kali ya, terus untuk presentase nilai mata kuliah itu, 20 persen Tugas, 30 persen untuk UTS dan UAS, terus masing-masing 10 persen untuk kehadiran dan keaktifan."

    bn "Kalau begitu ibu mulai kelasnya ya.."

    scene bg class campus with fade

    show screen alpro_1_1 with dissolve

    bn normal "Pagi hari ini kita akan mempelajari mengenai Algoritma Pemrograman, dihari ini kita akan membahas tentang pengertian dasar dan sejarahnya."

    bn "Sebelumnya kita harus mengerti apa itu program."

    bn "Program adalah sekumpulan perintah-perintah yang dikerjakan oleh komputer yang dibuat untuk mempermudah manusia dalam menyelesaikan suatu masalah."

    bn "Dalam pemrograman terdapat 3 level bahasa pemrograman yaitu, bahasa tingkat rendah, bahasa tingkat menengah, bahasa tingkat tinggi."

    bn "Bahasa tingkat rendah merupakan bahasa yang pertama kali digunakan untuk pengembangan program digital." 
    
    bn "Bahasa pemrograman yang ada dalam tingkat ini contohnya adalah bahasa mesin yang menggunakan kode biner(0 dan 1). 
    Bahasa ini mampu dibaca komputer tanpa memerlukan kompiler atau interpreter."

    bn "Kemudian bahasa tingkat menengah, merupakan bahasa pemrograman yang merupakan tingkatan penghubung antara tingkat rendah dan tingkat tinggi." 
    
    bn "Bahasa tingkat menengah lebih mudah untuk dipahami oleh manusia daripada bahasa tingkat rendah meskipun tetap agak sulit. 
    Contoh bahasa tingkat menengah adalah bahasa ADD, MUL, SUB."

    hide screen alpro_1_1

    show screen alpro_1_2 with fade

    bn "Yang terakhir adalah bahasa tingkat tinggi, merupakan bahasa pemrograman yang paling sering digunakan oleh manusia saat ini karena kemudahannya dalam dipelajari dan kodenya yang relatif lebih pendek." 
    
    bn "Contoh bahasa pemrograman dalam tingkat ini adalah C++, JAVA, Pascal dan lain sebagainya."

    bn "Kemudian kita masuk kedalam pengertian Algoritma."

    bn "Algoritma adalah Sebuah langkah-langkah atau intruksi logis yang dituliskan secara sistematis untuk menyelesaikan atau tugas yang diberikan."

    bn "Sebuah pertintah atau intruksi harus memiliki beberapa ciri-ciri untuk dapat dipanggil algoritma, Ciri-ciri tersebut adalah:"

    bn "Sebuah algoritma harus memilki jumlah langkah yang tentu dan tidak ambigu."

    bn "Lalu algoritma harus bisa berhenti setelah mengerjakan langkah yang ada."

    bn "Algoritma harus memiliki sebuah keluaran, dan algoritma memiliki instruksi efektif yang memungkinkan untuk dijalankan oleh pemroses."

    "Kemudian Bu Nira melanjutkan penjelasan algoritma dengan mempraktikannya menggunakan contoh dan gambar."

    "Kamu memperhatikan tiap penjelasan dari Bu nira dan menulisnya di buku catatanmu."
    hide screen alpro_1_2
    scene bg campus class with fade

    "Tidak terasa waktu sudah berjalan hingga kelas telah berakhir, Bu Nira sudah menutup pertemuan kali ini, tidak ada tugas yang diberikan."

    bn normal "Kalau begitu ibu tutup pertemuan pagi hari ini, terimakasih telah mengikuti pelajaran hari ini, sampai jumpa minggu depan teman-teman."

    t "Terimakasih…"

    t "terimakasih bu!"

    call attend_alpro
    call attend_class

    jump istirahat_1

label alpro_2:

    scene bg campus class with fade

    "[bn] memasuki ruang kelas, tanda perkuliahan akan segera dimulai."

    bn normal "Selamat pagi teman-teman kita berjumpa lagi pada pagi hari ini dalam perkuliahan Algoritma Pemrograman pertemuan ke 2."

    bn "Kalo kemarin kita sudah membahas mengenai pengertian, tiga tingkat bahasa pemrograman, dan ciri-ciri algoritma."

    bn "Sekarang kita akan mempelajari mengenai tiga macam konstruksi dasar algoritma, pseudocode, dan flowchart."

    show screen alpro_2_1 with fade

    bn "Jadi pada dasarnya algoritma itu mempunyai tiga macam konstruksi, yaitu sekuensial(berurutan dan bertahap), percabangan, dan pengulangan."

    bn "Algoritma Sekuensial merupakan suatu algoritma yang berjalan sesuai dengan prosedur atau tahap-tahap yang sudah ditentukan sebelumnya. 
    Proses demi proses dikerjakan untuk mencapai hasil akhir."

    bn "Kemudian ada Algoritma Percabangan, algoritma ini berjalan dan dapat mengmabil keputusan tertentu ketika mencapai suatu kondisi. 
    Dua atau lebih kondisi dapat memulai perbangan pada jalannya algoritma percabangan."

    bn "Lalu yang ketika terdapat Algoritma Pengulangan, sesuai dengan namanya algoritma ini menjalankan perintah yang menampilkan proses pengulangan dengan adanya syarat tertentu."

    bn "Itu mengenai konstruksi dasar algoritma, lalu kita akan melanjutkan pada penyajian algoritma menggunakan pseudocode dan flowchart."

    hide screen alpro_2_1

    show screen alpro_2_2 with fade

    bn "Apa itu Pseudocode? Pseudocode merupakan salah satu cara menyajikan algoritma. 
    Terlihat mirip seperti bahasa pemrograman, Pseudocode membantu kita dalam memahami jalannya sebuah algoritma yang dibuat."

    bn "Pseudocode terdiri dari judul(algoritma), deklarasi(variabel), dan isi(algoritma)."

    bn "Kemudian apa itu Flowchart? Flowchart merupakan cara penyajian suatu algoritma menggunakan simbol-simbol tertentu yang mampu menjelaskan jalannya program. 
    Flowchart biasanya digunakan sebagai pedoman dan dokumentasi dalam pembuatan suatu program."

    bn "Flowchart dimulai dari simbol terminator (start) dan berakhir pada simbol terminator (end). 
    Simbol yang biasanya terdapat pada flowchart yaitu proses(Untuk proses operasional), Data(Untuk input dan output data), Decision(Keputusan untuk percabangan.)"

    bn "Agar tidak bingung, ibu kasih contoh dengan sebuah algoritma untuk menghitung keliling suatu persegi."

    hide screen alpro_2_2

    show screen alpro_2_3 with fade   

    bn "Apabila suatu keliling persegi dapat diketahui dengan menjumlahkan 4 kali panjang sisinya dan diketahui panjang sisinya 
    adalah 4, algoritma untuk mengetahui keliling suatu persegi menggunakan pseudocode dan flowchart adalah sebagai berikut."

    bn "Jadi untuk pseudocode kita beri nama algoritmanya program menghitung_keliling_persegi"

    bn "Lalu kita deklarasikan variablenya seperti ini, variable sisi dan tipe datanya adalah integer."

    bn "Kemudian lanjut ke prosesnya, kita tulis sisi yang sudah diketahui lalu masukan rumusnya. 
    Kemudian write(tampilkan) output dari hasil perhitungannya."

    bn "Kurang lebih seperti pada gambar yang ada pada sisi kiri."

    bn "Bagaimana dengan flowchart?"

    bn "Dimulai dari simbol terminator untuk memulai program."

    bn "Lalu dilanjutkan dengan simbol data untuk menginput deklarasi dari panjang sisi yang diketahui."

    bn "Kemudian terdapat simbol proses untuk memasukan rumus perhitungan untuk mendapatkan keliling suatu persegi."

    bn "Setelah itu menggunakan simbol data lagi untuk menampilkan hasil dari proses yang dilakukan sebelumnya. 
    Sebelum akhirnya ditutup menggunakan simbol terminator(end) untuk mengakhiri jalannya program."

    bn "Kurang lebih seperti itu ya teman-teman, mungkin ada pertanyaan dari teman-teman?"

    hide screen alpro_2_3

    "Kemudian kelas dilanjutkan dengan sesi tanya jawab hingga waktu pertemuan berakhir."

    bn normal "Saya tutup pertemuan kali ini, terimakasih sudah berpartisipasi pada kelas hari ini dan sampai jumpa dipertemuan selanjutnya…"

    t normal "Terimakasih buuu…"

    r normal2 "Terimakasih buu.."

    "Kelas berakhir dan setelah ini merupakan jam istirahat, mahasiswa-mahasiswa mulai meninggalkan kelas."

    call attend_alpro
    call attend_class

    call istirahat

    jump de_2

label uts_alpro:

    scene bg campus class with dissolve

    "Memasuki jam ujian yang kedua, kamu sudah berada di depan ruang ujian yang sebentar lagi akan digunakan."

    "Sama seperti ruang kelas UTS sebelumnya, pada pintu masuk kelas sudah ditempel lembar berisikan informasi posisi tempat duduk masing-masing mahasiswa peserta UTS."

    "Setelah memastikan dimana posisi tempat dudukmu, kamu memasuki ruang kelas."

    "Sesuai yang diperintahkan dosen penjaga UTS, tas-tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    pa normal "Selamat pagi teman-teman pada pagi hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Algoritma Pemrograman."

    pa "Bapak harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    pa "Soal akan bapak bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    pa "Bapak harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Algoritma Pemrograman ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

    "Merasa cukup dengan persiapanmu, kamu mulai mengisi biodatamu pada lembar jawab sebelum mulai menelaah soal-soal UTS yang ada."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    "(Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    "(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)"

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS"

    "1. Terdapat 3 tingkat atau level dari bahasa pemrograman, manakah dibawah ini yang merupakan bahasa pemrograman tingkat tinggi?"
    menu:
        "A. Biner.":
            "A. Biner."
        "B. Add.":
            "B. Add."
        "C. SUB.":
            "C. SUB."
        "D. Assembly.":
            "D. Assembly."
        "E. Java.":
            "E. Java."
            $a_alproTS +=20
    "2. Dari beberapa pernyataan dibawah, manakah yang benar mengenai ciri suatu algoritma?"
    menu:
        "A. Sebuah algoritma memiliki jumlah langkah yang tentu dan tidak ambigu.":
            "A. Sebuah algoritma memiliki jumlah langkah yang tentu dan tidak ambigu."
            $a_alproTS +=20
        "B. Algoritma dapat melakukan perintah-perintah meskipun tidak tertulis pada perintah awal.":
            "B. Algoritma dapat melakukan perintah-perintah meskipun tidak tertulis pada perintah awal."
        "C. Algoritma tidak memerlukan sebuah keluaran.":
            "C. Algoritma tidak memerlukan sebuah keluaran."
        "D. Algoritma yang baik tidak perlu memerhatikan keefektivitasan karena hal terpenting adalah algoritma menyelesaikan masalah.":
            "D. Algoritma yang baik tidak perlu memerhatikan keefektivitasan karena hal terpenting adalah algoritma menyelesaikan masalah."
        "E. Algoritma tidak memerlukan suatu stopping point.":
            "E. Algoritma tidak memerlukan suatu stopping point."
    "3. Dari beberapa pernyataan dibawah, manakah yang salah mengenai ciri suatu algoritma?"
    menu:
        "A. Sebuah algoritma bisa memiliki jumlah langkah yang tak terbatas.":
            "A. Sebuah algoritma bisa memiliki jumlah langkah yang tak terbatas."
            $a_alproTS +=20
        "B. Algoritma akan berhenti setelah melakukan perintah-perintah yang ada.":
            "B. Algoritma akan berhenti setelah melakukan perintah-perintah yang ada."
        "C. Algoritma harus memiliki suatu keluaran.":
            "C. Algoritma harus memiliki suatu keluaran."
        "D. Sebuah instruksi efektif dibutuhkan agar instruksi tersebut dapat dijalankan oleh pemroses.":
            "D. Sebuah instruksi efektif dibutuhkan agar instruksi tersebut dapat dijalankan oleh pemroses."
        "E. Algoritma sebaiknya tidak memiliki suatu perintah yang ambigu.":
            "E. Algoritma sebaiknya tidak memiliki suatu perintah yang ambigu."
    "4. Dari beberapa algoritma dibawah manakah yang termasuk algoritma percabangan?"
    menu:
        "A. Algoritma cara memasak nasi goreng.":
            "A. Algoritma cara memasak nasi goreng."
        "B. Algoritma menjemur cucian basah.":
            "B. Algoritma menjemur cucian basah."
        "C. Algoritma pengelompokan siswa berdasarkan umur.":
            "C. Algoritma pengelompokan siswa berdasarkan umur."
            $a_alproTS +=20
        "D. Algoritma mencari luas segitiga.":
            "D. Algoritma mencari luas segitiga."
        "E. Algoritma membuat kopi.":
            "E. Algoritma membuat kopi."
    "5. Manakah dibawah yang merupakan sebuah Pseudocode untuk mencari volume sebuah balok?"
    menu:
        "A. Algoritma mencari volume balok | Input sisi, tinggi | volume = sisi*tinggi":
            "A. Algoritma mencari volume balok | Input sisi, tinggi | volume = sisi*tinggi"
        "B. Input panjang, lebar, tinggi | volume = panjang*lebar*tinggi":
            "B. Input panjang, lebar, tinggi | volume = panjang*lebar*tinggi"
        "C. Algoritma mencari volume balok | Input panjang*lebar*tinggi | output = volume":
            "C. Algoritma mencari volume balok | Input panjang*lebar*tinggi | output = volume"
        "D. Algoritma mencari volume balok | Input panjang*lebar*tinggi | volume = panjang*lebar*tinggi | output = volume":
            "D. Algoritma mencari volume balok | Input panjang*lebar*tinggi | volume = panjang*lebar*tinggi | output = volume"
            $a_alproTS += 20
        "E. Algoritma mencari volume balok | Input sisi*sisi*tinggi | volume = sisi*sisi*tinggi | output = volume":
            "E. Algoritma mencari volume balok | Input sisi*sisi*tinggi | volume = sisi*sisi*tinggi | output = volume"

    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengumpulkan kertas ujianmu, kamu memasukan barang-barangmu pada tas yang sebelumnya dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    call istirahat
    jump uts_de

label alpro_3:

    "ALPRO 3"

    call istirahat

    jump de_3

label alpro_4:

    "ALPRO 4"

    call istirahat

    jump de_4

label attend_alpro:

    $ a_alproA +=1
    $ a_alproN +=8

    return

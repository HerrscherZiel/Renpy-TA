
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


    scene bg campus hall with dissolve

    "Setelah beristirahat selama beberapa menit di luar ruang kelas, kini telah memasuki jam perkuliahan untuk kelas berikutnya."

    "Ruang kelas yang akan digunakan sudah dibuka karena telah digunakan pada kelas sebelumnya."

    "Kamu dan teman sekelasmu mulai memasuki ruang kelas satu persatu. Seperti biasanya kamu memilih tempat duduk di barisan tengah dan berada di dekat jendela."

    scene bg campus class with fade

    "Kamu menunggu dosen pengajar memasuki ruang kelas dengan memainkan hpmu dan mengobrol dengan teman sebelahmu."

    "Hampir 10 menit berada di dalam ruangan, akhirnya terlihat [bn] berjalan mendekati ruang kelas."

    "Setelah [bn] memasuki ruang kelas, tanda perkuliahan akan segera dimulai."

    bn normal "Selamat pagi teman-teman kita berjumpa lagi pada pagi hari ini dalam perkuliahan Algoritma Pemrograman pertemuan ke 3."

    bn "Ibu sudah memeriksa dan menilai pekerjaan kalian pada ujian tengah semester kemarin. Kalian bisa lihat hasilnya sendiri ya di Simaster."

    bn "Untuk hari ini kita akan membahas mengenai Prosedur dan Fungsi dalam pemrograman."

    bn "Apa itu prosedur dan fungsi, dan bagaimana contohnya akan kita bahas hari ini."

    "Setelah menyambungkan laptopnya dengan proyektor dan materi untuk hari ini sudah terlihat di depan kelas, perkuliahan pun dimulai."

    show screen alpro_3_1 with fade
    
    bn class "Apa itu prosedur dalam pemrograman? Prosedur merupakan suatu program yang disusun secara terpisah dan memiliki tujuan untuk melakukan suatu tugas atau fungsi tertentu."

    bn "Serangkaian instruksi yang terdapat pada prosedur dapat dipanggil atau dieksekusi oleh program utama atau bagian-bagian lain dari program."

    bn "Prosedur digunakan untuk mengelompokkan instruksi-instruksi tertentu menjadi satu kesatuan yang dapat digunakan kembali."

    bn "Terdapat dua macam prosedur, subrutin dan fungsi."

    hide screen alpro_3_1

    show screen alpro_3_2 with fade

    bn "Subrutin merupakan sebuah bagian dari suatu program yang berjalan terpisah untuk membantu melaksanakan tugas suatu program."

    bn "Fungsi merupakan suatu jenis khusus dari subroutine yang selalu mengembalikan nilai. Fungsi menerima argumen yang dimasukkan dan mengembalikan nilai hasil pemrosesan berdasarkan argumen tersebut kepada program utama."

    bn "Fungsi memiliki output dengan tipe variabel yang kita tentukan sebelumnya, pemakaian fungsi juga memerlukan sebuah parameter tidak seperti sebuah prosedur."

    bn "Untuk memperjelas perbedaan antara prosedur dan fungsi, akan ibu terangkan di bawah ini."

    hide screen alpro_3_2

    show screen alpro_3_3 with fade

    bn "Tujuan utama sebuah prosedur adalah melakukan tugas tertentu."

    bn "Sementara untuk fungsi, tujuan utamanya adalah melakukan perhitungan dan mengembalikan nilai."

    bn "Kemudian terdapat perbedaan pada pengembalian nilai."

    bn "Sebuah prosedur berjalan dan selesai tanpa mengembalikan sebuah nilai."

    bn "Fungsi disisi lain akan selalu mengembalikan sebuah nilai ketika selesai dieksekusi."

    bn "Sebagai contoh, prosedur meiliki tugas untuk mencetak maupun memanipulasi sebuah data."

    bn "Sementara fungsi misal digunakan untuk perhitungan matematis dan pengambilan sebuah data."

    bn "Ibu akan memberikan contoh code dalam bahasa python. "

    hide screen alpro_3_3

    show screen alpro_3_4 with fade

    bn "Contoh untuk prosedur adalah sebagai berikut:"

    "def sapa(nama):"

    bn "Merupakan line yang mendefinisikan prosedur sapa dengan parameter nama"
    
    "print('Halo,', nama)"

    bn "Ini adalah contoh prosedur yang mencetak pesan ke layar, dengan mencetak teks {i}Halo {/i} kemudian isi variabel nama."

    "sapa('Alice')"

    bn "Line tersebut memanggil prosedur sapa dengan memasukan nilai 'Alice' pada variabel nama sebagai parameter."

    bn "Kode tersebut akan berjalan sesuai program dan akan mencetak pesan ke layar tanpa mengembalikan nilai."

    bn "Kemudian untuk contoh kode fungsi adalah sebagai berikut:"

    hide screen alpro_3_4

    show screen alpro_3_5 with fade

    bn "Ini adalah contoh fungsi yang menghitung jumlah dua angka"

    "def tambah(a, b):"

    bn "Line tersebut berfungsi untuk mendefinisikan fungsi 'tambah' dengan parameter 'a' dan 'b'."

    "hasil = a + b"

    "return hasil"

    bn "Di dalam fungsi tambah, terdapat penjumlahan nilai 'a' dan 'b' yang disimpan pada variabel 'hasil' yang kemudian dikembalikan nilainya."

    bn "Kemudian kita panggil fungsi tambah dan kemudian menyimpan hasilnya dalam variabel hasil."

    "hasil = tambah(3, 4)"

    "print('Hasil penambahan:', hasil)"

    bn "Kode diatas akan berjalan dan melakukan perhitungan sebelum akhirnya akan mengembalikan hasil dari perhitungan tersebut."

    bn "Kurang lebih seperti itu untuk contoh dari prosedur dan fungsi."

    bn "Sekarang kita akan berlanjut pada manfaat dari prosedur dan fungsi."

    hide screen alpro_3_5

    show screen alpro_3_6 with fade

    bn "Mengapa prosedur dan fungsi kita gunakan dalam program kita? Tentu saja karena manfaat yang bisa kita peroleh dari penggunaannya."

    bn "Manfaat dari penggunaan prosedur dan fungsi adalah:"

    bn "1. Modularitas, yang berarti memungkinkan membagi program menjadi bagian-bagian yang lebih kecil, yang mampu mempermudah pengelolaan dan akan membuat kode menjadi lebih terstruktur dan lebih jelas."

    bn "2. Reuseabilitas, berarti kode yang sudah ada dapat digunakan kembali hanya perlu memanggil nama prosedur atau fungsi yang dibuat agar dapat digunakan kembali. Hal ini mampu mempercepat proses pengkodean."

    bn "3. Mengurangi duplikasi kode, dengan adanya prosedur atau fungsi maka tidak diperlukan lagi untuk mengetik kode yang memiliki fungsi yang sama. Oleh karena itu dapat menghindarkan kita dari duplikasi kode."

    bn "4. Memudahkan pemeliharaan kode, hal ini mungkin terjadi karena dengan adanya prosedur dan fungsi dapat dipisahkan antara tugas-tugas yang berbeda ke dalam prosedur dan fungsi."

    hide screen alpro_3_6 with dissolve

    bn "Kurang lebih seperti itu ya teman-teman, mungkin ada pertanyaan dari teman-teman?"

    "Kemudian kelas dilanjutkan dengan sesi tanya jawab hingga waktu pertemuan berakhir."

    scene bg campus class with dissolve

    bn normal "Saya tutup pertemuan kali ini, terimakasih sudah berpartisipasi pada kelas hari ini dan sampai jumpa dipertemuan selanjutnya…"

    t normal "Terimakasih buuu…"

    r normal2 "Terimakasih buu.."

    "Kelas berakhir dan setelah ini merupakan jam istirahat, mahasiswa-mahasiswa mulai meninggalkan ruang kelas."

    call attend_alpro
    call attend_class

    call istirahat

    jump de_3

label alpro_4:

    scene bg campus hall with dissolve

    "Setelah beristirahat selama beberapa menit di luar ruangan, jam perkuliahan berikutnya sudah dimulai."

    "Ruang kelas yang akan digunakan sudah dibuka karena telah digunakan pada kelas sebelumnya."

    "Kamu dan teman sekelasmu mulai memasuki ruang kelas satu persatu. Seperti biasanya kamu memilih tempat duduk di barisan tengah dan berada di dekat jendela."

    scene bg campus class with fade

    "Kamu menghabiskan waktumu dengan memainkan gim yang terdapat pada HPmu. Beberapa menit memainkan gim, dosen pengajar memasuki ruang kelas dan mahasiswa mulai mempersiapkan untuk kelas yang segera akan dimulai."

    bn normal "Selamat pagi teman-teman kita kembali berjumpa lagi pada perkuliahan pagi hari ini dengan mata kuliah Algoritma Pemrograman pertemuan ke 4."

    bn "Pertemuan kali ini merupakan pertemuan terakhir mata kuliah ini sebelum kalian akan melakukan ujian akhir semester."

    bn "Untuk pertemuan kali ini kita akan membahas mengenai algoritma untuk Pencarian(Search) dan Pengurutan(Sort) secara dasar."

    bn "Untuk menyingkat waktu, kita langsung saja mulai perkuliahan hari ini."

    show screen alpro_4_1 with fade

    bn class "Apakah algoritma pencarian itu?"

    bn "Algoritma Pencarian adalah sebuah algoritma yang dibuat untuk melakukan sebuah pencarian untuk menemukan sebuah informasi spesifik yang terdapat dalam suatu struktur data yang dimiliki."

    bn "Kenapa algoritma pencarian dibutuhkan ? Beberapa alasan mengapa algoritma pencarian digunakan adalah:"

    bn "1. Pencarian data, sesuai namanya algoritma ini dapat digunakan untuk menemukan elemen-elemen spesifik yang kita butuhkan dalam suatu kumpulan data."

    bn "2. Optimasi kinerja, dengan adanya algoritma pencarian yang efisien akan mampu mengoptimalkan kinerja dari aplikasi. Algoritma yang digunakan tersebut mampu untuk mengurangi eksekusi terutama dalam pencarian dalam skala yang besar. Kecepatan pencarian menjadi sangat dibutuhkan."

    hide screen alpro_4_1

    show screen alpro_4_2 with fade

    bn "3. Fungsionalitas perangkat lunak, seringkali fitur pencarian dibutuhkan atau diminta oleh pengguna sebuah perangkat lunak. Oleh karena itu algoritma pencarian digunakan dalam beberapa perangkat lunak yang membutuhkan fitur pencarian."

    bn "4. Analisis data, dengan adanya algoritma pencarian memungkinkan dan mempermudah kita dalam menemukan sebuah informasi tertentu dalam sebuah kumpulan data."

    bn "Kemudian setelah mengetahui kegunaan-kegunaan dari algoritma pencarian, ibu akan menjelaskan dan memberi contoh tentang algoritma pencarian."

    hide screen alpro_4_2

    show screen alpro_4_3 with fade

    "[bn] mengganti slide, kemudian terlihat contoh-contoh dari algoritma pencarian."

    bn "1. Linear Search, merupakan salah satu contoh algoritma pemrograman yang paling simple. Algoritma ini melakukan pencarian dengan cara mencari dan memeriksa secara urut dalam kumpulan data hingga elemen yang diinginkan didapatkan."

    bn "Algoritma ini akan mengecek satu persatu dari elemen pertama yang terdapat pada daftar, jika menemukan elemen dicari maka akan mengembalikan elemen tersebut, apabila tidak maka proses akan berulang sampai elemen terakhir diperiksa."

    bn "Salah satu alasan menggunakan algoritma linear search adalah karena algoritma ini sederhana dan mudah untuk dipahami."

    hide screen alpro_4_3

    show screen alpro_4_4 with fade

    bn "2. Depth First Search, algoritma pencarian yang satu ini merupakan sebuah algoritma pencarian yang digunakan dalam sebuah tree atau graf, dimana pencarian dilakukan dengan memasukan node kedalam sebuah stack."

    bn "Lalu pencarian dilakukan dengan menelusuri simpul terdalam, apabila hasil yang diinginkan tidak ditemukan maka pencarian akan kembali ke simpul yang telah dikunjungi sebelumnya yang bertetangga dengan simpul yang belum pernah dikunjungi. "

    bn "Pencarian akan berlanjut hingga hasil yang diinginkan ditemukan atau semua simpul telah dikunjungi."

    hide screen alpro_4_4

    show screen alpro_4_5 with fade

    bn "3. Binary Search, merupakan salah satu algoritma pencarian yang dilakukan pada kumpulan data yang telah diurutkan sebelumnya. Pencarian ini dilakukan dengan membagi data menjadi dua bagian dan membandingkan elemen tengah dengan elemen yang dicari. "

    bn "Sehingga memungkinkan kita untuk mengetahui apakah elemen yang dicari berada pada bagian kanan atau kiri dari elemen tengah yang ditemui."
    
    bn "Itu diatas merupakan beberapa penjelasan mengenai algoritma pencarian."

    bn "Kini kita akan berlanjut mempelajari tentang algoritma pengurutan."

    hide screen alpro_4_5

    show screen alpro_4_6 with fade

    bn "Apakah algoritma pengurutan itu?"

    bn "Algoritma pengurutan merupakan sebuah algoritma yang digunakan untuk merubah atau mengatur suatu elemen pada suatu struktur data kedalam aturan atau urutan tertentu yang diinginkan."

    bn "Sama seperti sebelumnya, apa kegunaan dari algoritma pengurutan?"

    bn "1. Memudahkan pencarian, kumpulan data yang telah dilakukan algoritma pengurutan sebelumnya akan lebih mudah ketika melakukan pencarian data."

    bn "2. Optimasi kinerja, dengan kemudahan dan kecepatan pengaksesan data yang menjadi lebih efisien maka program akan memiliki kinerja yang lebih optimal."

    bn "3. Lebih mudah membaca informasi, pengaplikasian algoritma pengurutan pada presentasi data dapat mempermudah informasi untuk diterima. Hal ini juga dapat meningkatkan pengalaman yang didapatkan oleh pengguna aplikasi."

    bn "4. Membuat pemrograman menjadi lebih efisien, dengan adanya algoritma pengurutan yang digunakan akan membuat kode yang ditulis menjadi lebih efisien."

    bn "Kemudian pembahasan kita selanjutnya pada hari ini adalah mengenai contoh algoritma pengurutan."

    bn "Berikut adalah contoh dari algoritma pengurutan:"

    hide screen alpro_4_6

    show screen alpro_4_7 with fade

    "[bn] mengganti slide dan slide berganti menjadi penjelasan contoh algoritma pemrograman."

    bn "1. Bubble sort, merupakan salah satu algoritma pengurutan yang bisa dibilang sederhana. Algoritma pengurutan ini cenderung mudah untuk dipahami dan diterapkan. Cara kerja pada algoritma ini adalah melakukan perbandingan dan penukaran terhadap elemen-elemen array yang ada."

    bn "Perbandingan akan terus diulang prosesnya hingga urutan elemen sudah sesuai yang diinginkan dan tidak diperlukannya proses penukaran lagi."

    bn "2. Quick sort, merupakan algoritma pengurutan yang tergolong cepat namun cenderung rumit untuk penggunaannya. Cara kerja algoritma quick sort adalah dengan membagi data yang ada kedalam dua sisi, kiri dan kanan dan menggunakan data yang terdapat di tengah sebagai pusat."

    bn "Algoritma akan membandingkan dan mengurutkan suatu data yang ada dengan data tengah yang menjadi pusat, kemudian data yang lebih kecil daripada data tengahakan dikumpulkan pada sebelah kiri data tengah. Sementara data yang lebih besar dari data tengah akan dikumpulkan dibagian kanan data tengah."

    bn "Memungkinkan pada suatu bagian untuk memiliki data tengah baru untuk melakukan pengurutan terhadap sisi tersebut."

    hide screen alpro_4_7

    show screen alpro_4_8 with fade

    bn "3. Insertion sort, sesuai namanya algoritma yang satu ini bekerja dengan mengambil elemen pertama pada suatu array yang belum diurutkan dan diletakan pada bagian baru dari array yang sudah diurutkan. Proses dilakukan kembali dengan elemen array berikutnya, namun ketika akan diletakan pada array yang sudah diurutkan dilakukan perbandingan."

    bn "Apabila elemen kedua tersebut lebih kecil dari elemen pertama pada array yang sudah diurutkan maka elemen kedua tersebut akan diletakan di kiri elemen pertama. Begitu pula sebaliknya, apabila elemen kedua memiliki nilai yang lebih besar maka akan diletakan pada sisi kanan elemen pertama pada array yang sudah diurutkan."

    bn "Mungkin itu dulu penjelasan yang dapat ibu berikan pada pertemuan kali ini mengenai algoritma pencarian dan pengurutan."

    hide screen alpro_4_8 with dissolve

    bn normal "Sebelum ibu tutup ibu akan memperlihatkan gambaran mengenai apa yang ibu terangkan sebelumnya."

    "[bn] memperlihatkan slide yang berisi contoh dari algoritma pencarian dan pengurutan."

    "Setelah memperlihatkan slide contoh, kelas dilanjutkan dengan sesi tanya jawab."

    scene bg black with Dissolve(2.0)

    scene bg campus class with fade

    "Waktu pertemuan kelas siang ini sudah berada pada penghujung waktu."

    bn normal "Sebelum ibu tutup pertemuan kali ini, akan kembali ibu ingatkan untuk materi ujian akhir semesternya akan diambil dari materi setelah ujian tengah semester."

    mc normal jacket "Hmm berarti materinya mulai dari pertemuan 3 dan 4 saja ya."

    bn "Selamat belajar, semoga berhasil dan mendapatkan hasil yang memuaskan ya teman-teman."

    bn "Terimakasih sudah mengikuti kelas pada mata kuliah ini, sampai jumpa pada pertemuan di lain waktu."

    t normal "Terimakasih buu!!"

    t "Terimakasihhh"

    r normal2 "Terimakasih juga buu"

    scene bg campus hall with dissolve

    "Kelas telah usai, kamu dan teman-temanmu keluar dari kelas."

    "Sebelum kelas terakhir pada hari ini, terdapat waktu istirahat yang bisa kamu gunakan untuk melakukan aktivitas lain."

    call attend_alpro
    call attend_class

    call istirahat

    jump de_4

label uas_alpro:

    scene bg campus hall with dissolve

    "Tidak jauh berbeda dengan suasana sebelum ujian pertama dimulai, mahasiswa-mahasiswa duduk mengelompok di depan ruang kelas ujian dan belajar materi perkuliahan yang akan diujikan."

    "Termasuk dirimu dan teman-teman sekelasmu, kamu melihat [r] dan beberapa teman kelas lainnya saling mengajukan tanya jawab seputar materi ALPRO yang menjadi mata kuliah yang akan diujikan kedua pada hari ini."

    "Masih tersisa sekitar 15 menit lagi sebelum ujian kedua pada hari ini dimulai."

    "Seperti sebelumnya, kamu hanya duduk bersandar di tembok kelas sembari mengingat materi yang telah kamu pelajari."

    t normal "Hei [name] gimana tadi? Lancar gak ngerjainnya?"

    mc normal jacket "Yahh… gitulah ya, harusnya sih oke hasilnya, lu gimana?"

    t "Hahaha jangan tanya, ya jelas sebisanya lahh, semalem baru belajar bentar malah mati listrik kosan gua."

    mc "Lahhh… yaudah belajar lagi sana, masih sisa beberapa menit lagi nihh"

    t "Santaii… masih dikit-dikit inget kok materinya."

    mc "Jiahhh… yakin inget?"

    t "Ingettttt lahhhh…. dikit."

    mc "Hahaha yaudah good luck aja dah"

    "Mengisi beberapa menit sebelum ujianmu dengan mengobrol dengan teman sekelasmu membuat dirimu menjadi lebih tenang sebelum mengikuti ujian berikutnya."

    "Namun obrolan pagi harimu dihentikan ketika suara pintu ruang ujian yang ada didekatmu telah terbuka."

    "Sekarang sudah memasuki waktu ujian akhir yang kedua, kamu berdiri dan bergegas masuk ke ruang ujian."

    scene bg campus upper hall with fade

    pause 2.0

    scene bg campus class with fade

    "Sebelum memasuki ruang kelas ujian tak lupa dirimu sempat mengecek dimana bangku ujian untuk ujian akhir mata kuliah ALPRO kali ini."

    "Setelah mengetahui dimana bangku ujian mu, kamu memasuki ruang kelas dan melihat dosen pengawas ujian yang familiar pada perkuliahanmu."

    pa normal "Selamat pagi teman-teman, bagaimana persiapannya untuk ujian kali ini, bapak harap kalian sudah siap yaa."

    pa "Mungkin seperti yang sudah kalian tahu, bapak akan membaca instruksi untuk ujian kali ini."

    "Memasuki ruang kelas ujian, [pa] selaku pengawas ujian memberi instruksi kepada mahasiswa seperti instruksi yang ada pada ujian sebelumnya."

    "Meletakkan tas atau ransel di depan kelas secara rapi. Lalu hanya membawa peralatan tulis dan kartu mahasiswa ke bangku ujian."

    "Setelah meletakan tas ransel milikmu di depan ruang kelas, kamu mengambil peralatan tulis sebelum berjalan menuju bangku ujianmu."

    "Terlihat lembar jawab ujian sudah diletakan pada masing-masing bangku ujian."

    "Kemudian ketika semua bangku ujian telah terisi oleh peserta ujian, [pa] lalu menjelaskan peraturan ujian."

    "Tidak ada yang berbeda seperti peraturan-peraturan ujian pada umumnya."

    "Selesai menjelaskan, beberapa menit kemudian soal ujian disebarkan kepada seluruh peserta yang ada."

    "Kamu menerima beberapa soal ujian dari bangku yang ada di depanmu, setelah mengambil salah satu soal ujian, kamu meneruskan pembagian soal-soal ujian lainnya ke bangku yang ada di belakangmu."

    "[pa] telah memberi instruksi jika ujian sudah dimulai, dan mahasiswa bisa mulai mengerjakan soal ujian."

    "Kamu berdiam dan berdoa terlebih dahulu sebelum mulai mengisi lembar jawaban dengan identitas dirimu."

    "Membuka lembar soal ujian, terdapat beberapa panduan pengerjaan soal pada bagian atas lembar. Kamu menyempatkan diri untuk membaca beberapa panduan pengerjaan tersebut."

    "({i}Ketika {b}UAS{/b} terdapat 5 soal pilihan ganda yang harus dikerjakan untuk menyelesaikan ujian)"

    "({i}Setiap pertanyaan akan ditampilkan dan akan muncul dalam waktu 90 detik{/i})"

    "({i}Ketika waktu 90 detik habis, soal akan hilang dari layar {/i})"

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

    "1. Berikut merupakan beberapa pernyataan mengenai prosedur dan fungsi, pernyataan yang benar adalah?"

    mc normal jacket "fungsi dan prosedur yaa…"

    menu:
        "A. Prosedur dan Fungsi mengembalikan nilai":
            "a. Prosedur dan Fungsi mengembalikan nilai."
            mc "Emang dua duanya return value ya?"

        "B. Prosedur dan Fungsi tidak mengembalikan nilai":
            "b. Prosedur dan Fungsi tidak mengembalikan nilai."
            mc "Hmmmm masa sih keduanya ga ngembaliin nilai?"

        "C. Prosedur tidak mengembalikan nilai":
            "c.Prosedur tidak mengembalikan nilai."
            mc "Ya prosedur engga ngereturn value?"
            $ a_alproAS += 5

        "D. Fungsi tidak mengembalikan nilai":
            "d. Fungsi tidak mengembalikan nilai."
            mc "Fungsi harusnya ngembaliin nilai kan?"

    "Kamu menjawab pertanyaan pertama dengan lancar, setelah beberapa kali memeriksa jawaban kamu yakin akan jawaban pertamamu."

    "Kemudian kamu lanjut menuju pertanyaan selanjutnya."

    "2. 	Manakah dibawah ini yang bukan merupakan manfaat dari pemanfaatan prosedur dan fungsi?"

    mc "Manfaat-manfaat prosedur dan fungsi itu…."

    menu:

        "A. Modularitas":
            "a. Modularitas."
            mc "Modularitas itu kalau gak salah..."

        "B. Reusabilitas":
            "b. Reusabilitas."
            mc "Menggunakan prosedur atau fungsi memang bisa dipanggil berkali-kali sih."
	
        "C. Memudahkan pemeliharaan kode":
            "c. Memudahkan pemeliharaan kode."
            mc "Harusnya juga pemeliharaannya jadi lebih mudah…"

        "D. Menambah estetika kode":
            'd. Menambah estetika kode.'
            mc "Kayanya engga ngaruh keestetika juga deh…"
            $ a_alproAS += 5

    "Berhasil menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."

    "3. Algoritma pencarian yang dilakukan pada kumpulan data yang telah diurutkan sebelumnya. Pencarian ini dilakukan dengan membagi data menjadi dua bagian dan membandingkan elemen tengah dengan elemen yang dicari.
    Merupakan penjelasan dari algoritma pencarian....?"

    menu:

        "A. Linear Search":
            "a. Linear Search"
            mc "Hmmmmm…."

        "B. Binary Search":
            "b. Binary Search"
            mc "Kayaknya kalau diurutin dulu itu yang binary dah…."
            $ a_alproAS += 5

        "C. Depth First Search":
            "c. Depth First Search"
            mc "Ini yang pake node-node itu ga sih?"

        "D. Tree Search":
            "d. Tree Search"
            mc "Baru denger ada yang namanya Tree Search…."

    "Setelah menjawab pertanyaan nomor 3, kamu bergegas menuju pertanyaan selanjutnya."

    "Tersisa dua soal ujian lagi, merasa cepat ingin menyelesaikan quiz ini, kamu langsung membaca pertanyaan nomor 4."

    "4. 	Cara kerja algoritma dengan melakukan perbandingan dan penukaran terhadap elemen-elemen array yang ada hingga semua data terurutkan
    Merupakan penjelasan dari cara kerja algoritma pengurutan....."

    menu:

        "A. Bubble Sort":
            "a. Bubble Sort"
            mc "Kalo ga salah yang paling simple itu bubble sort…"
            $ a_alproAS += 5

        "B. Insertion Sort":
            "b. Insertion Sort"
            mc "Insertion sort itu yang ngesisipin terus dibandingkan itu kan ya?"

        "C. Quick Sort":
            "c. Quick Sort"
            mc "Quick Sort?? Hmmm….."

        "D. Depth First Sort":
            "d. Depth First Sort"
            mc "Yang ini kali ya?"

    "Selesai menjawab pertanyaan ke 4, kini hanya tinggal satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan ujian akhir ALPRO pada pagi hari ini."

    "Setelah mengecek jawaban no 4, kamu langsung membaca soal terakhir yang terdapat pada lembar soal ujian."

    "5. Apa manfaat dari penggunaan algoritma pencarian dan pengurutan, kecuali?"

    menu:

        "A. Optimasi kinerja":
            "a. Optimasi kinerja"
            mc "Harusnya yang ini bener sih…"

        "B. Memudahkan pencarian":
            "b. Memudahkan pencarian"
            mc "Namanya algoritma pencarian, harusnya ya jadi mudah pencariannya."

        "C. Pemrograman lebih efisien":
            "c. Pemrograman lebih efisien"
            mc "Lebih simple terus bisa dipakai berkali-kali, bener berarti…"

        "D. Redudansi kode":
            "d. Redudansi kode"
            mc "Harusnya kan bikin nggak redundant??"
            $ alproAS += 5

    "Setelah memilih jawaban untuk pertanyaan terakhir, semua soal yang terdapat pada lembar soal ujian sudah kamu selesaikan."

    "Kamu melihat sekelilingmu, masih ada temanmu yang masih mengerjakan ujian, namun ada juga yang sudah beranjak dari bangku ujian."

    "Sebelum mengumpulkan jawaban, tidak lupa kamu mengecek apakah biodata dan jawaban yang kamu isi semuanya sudah benar."

    "Selesai mengecek, kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawaban ujianmu."

    "Lalu tidak lupa untuk mengambil tas ransel milikmu yang ketika ujian berlangsung diletakkan di depan kelas secara rapi."

    "Keluar dari ruang kelas ujian, menandakan kamu telah menyelesaikan ujian akhir mata kuliah ALPRO, kamu merasa senang namun kamu belum bisa merasa lega karena pada hari ini masih tersisa 1 ujian akhir mata kuliah Desain Elementer."

    scene bg campus hall with dissolve

    pause 1.5

    call istirahat_uas

    jump uas_de


label attend_alpro:

    $ a_alproA +=1
    $ a_alproN +=8

    return

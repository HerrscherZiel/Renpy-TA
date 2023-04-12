
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

    r "Kemudian untuk jadwal kelas dan ruangan selama satu minggu, aku sedang buat ya... nanti akan aku share kalau udah jadi untuk yang kelas ini di group chat Lane."

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

    call screen jadwal with fade

    "Untuk mengakses jadwal pilih menu jadwal!!!"

    show screen jadwal_btn with dissolve

    mc normal jacket "Ohh begitu ya.. "

    "Selagi kamu menelaah jadwal yang ada, seorang dosen perempuan memasuki ruang kelas."

    siapa "Selamat pagi teman-teman! Haloo apa kabarnya?"

    t normal "Pagiii…"

    t "Selamat pagi bu…"

    "Dosen perempuan itu langsung duduk menempati bangku dosen yang ada, kemudian ia mengeluarkan laptop dari tas yang ia bawa."

    siapa "Iya… sebelumnya karena saya rasa ini pertemuan pertama kita, karena kalian belum kenal maka saya akan memperkenalkan diri dulu."

    siapa "Nama saya adalah Nira, kalian bisa manggil saya Bu Nira saja. Di kelas ini saya akan mengajar Algoritma Pemrograman, salam kenal teman-teman!"

    t "salam kenal bu Nira.."

    bn normal "Untuk mata kuliah ini perjanjian untuk tidak mengikuti kelas 3 kali ya, terus untuk presentase nilai mata kuliah itu, 20% Tugas, 30% untuk UTS dan UAS, terus masing-masing 10% untuk kehadiran dan keaktifan."

    bn "Kalau begitu ibu mulai kelasnya ya.."

    scene bg class campus with fade

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

    scene bg campus class with fade

    "Tidak terasa waktu sudah berjalan hingga kelas telah berakhir, Bu Nira sudah menutup pertemuan kali ini, tidak ada tugas yang diberikan."

    bn normal "Kalau begitu ibu tutup pertemuan pagi hari ini, terimakasih telah mengikuti pelajaran hari ini, sampai jumpa minggu depan teman-teman."

    t "Terimakasih…"

    t "terimakasih bu!"

    call attend_alpro
    call attend_class

    jump istirahat

label attend_alpro:

    $ a_alproA +=1
    $ a_alproN +=8

    return

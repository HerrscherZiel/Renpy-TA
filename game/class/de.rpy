
default a_deA = 0
default a_deT = 0
default a_deC = 0
default a_deTS = 0
default a_deAS = 0
default a_deN = 0

label istirahat:

    scene bg campus upper hall with dissolve

    "Setelah kelas kedua berakhir, masih ada sekitar satu jam untuk kelas berikutnya."

    "Beberapa teman sekelasmu pergi meninggalkan kelas dan langsung keluar dari lingkungan kampus. 
    Namun juga ada mahasiswa yang teteap menetap di kampus, kamu adalah salah satu mahasiswa yang tidak meninggalkan kampus."

    "Kamu duduk pada bangku yang ada di lorong kampus selama beberapa menit, sembari memainkan game yang ada di HPmu."

    "Kadang kali kamu berbicara dengan teman sekelasmu yang juga menunggu di kampus."

    "Karena merasa lapar, salah satu teman sekelasmu mengajak untuk pergi menuju kantin yang ada di dalam gedung kampus."

    t normal "Hei ayo cari makan dulu, lapar nih aku, masih ada setengah jam an lagi sebelum kelas kan."

    mc normal jacket "Ayok gas, ikut aku, laper juga… "

    t "Skuyy… ikut aku ke kantin."

    "Kamu mengikuti temanmu menuju kantin kejujuran yang terletak pada lantai 2 gedung kampusmu."

    "Disana kamu melihat beberapa tempat makanan yang berisi berbagai macam jenis jajanan lokal. Terlihat juga minuman bungkus plastik yang dijual."

    "Karena kantin yang kamu kunjungi adalah kantin kejujuran, maka tidak ada penjual yang menunggu jualan mereka."

    "Hanya ada jajanan dan toples terbuka yang digunakan untuk menaruh uang pembelian jajanan. Disamping jajanan juga ada kertas yang bertuliskan harga setiap jajanan."

    "Sesuai namanya, kantin kejujuran, para penjual hanya percaya kepada pembeli untuk menaruh uang dengan jumlah yang pas."

    "Pembeli hanya tinggal mengambil jajanan yang diinginkan, lalu menaruh uang kedalam tempatnya, jika perlu kembalian maka pembeli dapat menukar uang pada toples uang yang ada."

    "Kamu membeli beberapa jajanan untuk mengisi perutmu yang sudah mulai keroncongan."

    "Setelah mengambil jajanan, kamu duduk di bangku yang terletak di kantin kejujuran kemudian langsung mengkonsumsinya."

    "Sembari menunggu kelas berikutnya, kamu mengkonsumsi jajanan yang dibeli dan mengobrol dengan teman sekelasmu."

    scene bg canteen with fade

    call small_eat

    "Lama menunggu kini jam digital yang ada di hpmu sudah menunjukan pukul 11.50."

    "Kamu dan teman sekelasmu melihat jadwal yang dikirimkan oleh Rissa untuk mengetahui ruang kelas untuk kelas selanjutnya."

    "Setelah mengerti dimana kelas selanjutnya diadakan, kamu dan teman sekelasmu pergi menuju ke ruang tersebut."

    jump de_1

label de_1:

    scene bg campus class with dissolve

    "Memasuki ruangan yang baru, kamu kembali memilih untuk menempati tempat duduk yang ada pada posisi yang sama seperti dimana kamu duduk sebelumnya."

    "Untuk kelas siang hari ini, mata kuliah Desain Elementer juga akan diampu oleh Pak Andy. Jadi kelas ini merupakan pertemuan kedua dengan Pak Andy sebagai dosen."

    "Setelah waktu menunjukkan pukul 12.00, tidak lama kemudian Pak Andy memasuki ruang kelas."

    "Pak Andy kembali membicarakan peraturan dan perjanjian dalam kelas yang diampunya. Apa yang Pak Andy bicarakan kurang lebih sama dengan mata kuliah lain yang diampunya."

    "Selesai menyambungkan laptop dengan proyektor Pak Andy langsung memulai menjelaskan materi perkuliahan."

    pa "Yak selamat siang teman-teman, kita bertemu lagi hari ini meskipun disini mata kuliahnya beda ya."

    pa "Di mata kuliah Desain Elementer pertemuan pertama ini, bapak akan menjelaskan pengertian dan elemen-elemen dasar pada desain elementer."

    pa "Pertama, desain elementer itu apa sih? Jadi Desain elementer adalah mata kuliah yang mempelajari mengenai unsur-unsur dasar seni rupa seperti garis, warna, bentuk, tipografi, dan juga strategi penyusunannya agar dapat dinikmati dengan baik."

    pa "Desain Elementer juga memiliki elemen atau unsur-unsur dasar, elemen tersebut adalah sebagai berikut:"

    pa "Titik, titik merupakan sebuah unsur paling kecil dari suatu objek. Titik tidak memiliki dimensi, ukuran maupun panjang."

    pa "Umumnya penampilan titik ditampilkan secara berkelompok, dengan berbagai variasi baik dari jumlah, susunan, maupun warna."

    pa "Kemudian, unsur yang kedua adalah Garis, bisa dibilang garis merupakan gabungan dari beberapa titik yang ditarik kedalam suatu arah sehingga membentuk suatu kesatuan. Garis merupakan unsur seni rupa 2 dimensi."
    
    pa "Berbagai macam bentuk garis seperti lurus, tebal, tipis, dan lain sebagainya memiliki arti tersendiri. Semisal garis lurus horizontal memiliki arti atau kesan yang stabil."

    pa "Selanjutnya ada Bidang, bidang juga merupakan gabungan dari beberapa garis yang membentuk kesatuan dan membuat ruang yang tertutup. Bidang menempati ruang dua dimensi. Bidang dapat digunakan untuk menggambarkan sebuah objek."
    
    pa "Bidang terdapat bidang geometris seperti persegi, segitiga, lingkaran dan lain sebagainya, dan bidang non geometris seperti bidang yang berbentuk bebas."

    pa "Lalu setelah bidang ada unsur Warna, Warna memberikan suatu desain suatu makna dan tujuan."
    
    pa "Pemilihan warna yang digunakan tidak boleh semena-mena, karena jika suatu desain kurang berwarna atau terlalu redup maka desain akan terlihat redup atau kurang menarik."
     
    pa "Sementara pemakaian warna yang terlalu banyak atau terlalu mencorok dapat menyebabkan suatu desain terlihat norak dan kurang enak dipandang."

    pa "Unsur berikutnya adalah Tekstur, tekstur dapat memberikan kesan yang menarik."
    
    pa "Terdapat tekstur yang bisa dirasakan dengan pengelihatan atau tekstur visual, dan tekstur yang dapat dirasakan dengan pengerabaan dan pengelihatan atau tekstur taktil."

    pa "Lalu ada unsur Ruang, unsur ruang merupakan unsur yang digunakan untuk membuat unsur-unsur yang ada pada suatu ruangan atau tempat agar tidak berkesan terlalu menumpuk ataupun penuh, sehingga ruangan yang ada dapat terlihat lebih tenang atau rileks."

    "Pelajaran dilanjutkan dengan tampilan gambar-gambar yang diperlihatkan oleh Pak Andy."

    "Kamu mendengarkan dan mencatat apa yang menurutmu penting."

    "Kelas berjalan dengan tenang hingga waktu pertemuan telah berakhir."

    scene bg campus class with fade

    pa "Yak terimakasih telah menghadiri pertemuan hari ini, sampai jumpa di pertemuan kita yang selanjutnya."

    t normal "terimakasih pak"

    t "terimakasih…"

    "Sekarang sudah menunjukan pukul 02.00, Pak Andy meninggalkan ruang kelas tanpa memberikan tugas untuk mata kuliah." 
    
    "Satu-persatu teman kelasmu juga ikut meninggalkan ruang kelas."

    "Kamu mengemas barang-barangmu dan segera meninggalkan ruangan." 

    scene bg campus parking lot with fade
    
    "Merasa sangat lelah dengan hari pertama kuliahmu, kamu bergegas menuju motor yang kamu parkirkan di parkiran kampus."

    "Setelah menyalakann motormu, tidak ada tujuan lain selain menuju kosan untuk beristirahat."

    "Brummmm"

    jump kosan




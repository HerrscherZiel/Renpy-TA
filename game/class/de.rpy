
default a_deA = 0
default a_deT = 0
default a_deC = 0
default a_deTS = 0
default a_deAS = 0
default a_deN = 0

label istirahat_1:

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

    call small_eat from _call_small_eat_3

    $vit += 10

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

    pa normal "Yak selamat siang teman-teman, kita bertemu lagi hari ini meskipun disini mata kuliahnya beda ya."

    pa "Di mata kuliah Desain Elementer pertemuan pertama ini, bapak akan menjelaskan pengertian dan elemen-elemen dasar pada desain elementer."

    show screen de_1_1 with dissolve

    pa "Pertama, desain elementer itu apa sih? Jadi Desain elementer adalah mata kuliah yang mempelajari mengenai unsur-unsur dasar seni rupa seperti garis, warna, bentuk, tipografi, dan juga strategi penyusunannya agar dapat dinikmati dengan baik."

    pa "Desain Elementer juga memiliki elemen atau unsur-unsur dasar, elemen tersebut adalah sebagai berikut:"

    pa "Titik, titik merupakan sebuah unsur paling kecil dari suatu objek. Titik tidak memiliki dimensi, ukuran maupun panjang."

    pa "Umumnya penampilan titik ditampilkan secara berkelompok, dengan berbagai variasi baik dari jumlah, susunan, maupun warna."

    pa "Kemudian, unsur yang kedua adalah Garis, bisa dibilang garis merupakan gabungan dari beberapa titik yang ditarik kedalam suatu arah sehingga membentuk suatu kesatuan. Garis merupakan unsur seni rupa 2 dimensi."
    
    pa "Berbagai macam bentuk garis seperti lurus, tebal, tipis, dan lain sebagainya memiliki arti tersendiri. Semisal garis lurus horizontal memiliki arti atau kesan yang stabil."

    hide screen de_1_1

    show screen de_1_2 with fade
    
    pa "Selanjutnya ada Bidang, bidang juga merupakan gabungan dari beberapa garis yang membentuk kesatuan dan membuat ruang yang tertutup. Bidang menempati ruang dua dimensi. Bidang dapat digunakan untuk menggambarkan sebuah objek."
    
    pa "Bidang terdapat bidang geometris seperti persegi, segitiga, lingkaran dan lain sebagainya, dan bidang non geometris seperti bidang yang berbentuk bebas."

    pa "Lalu setelah bidang ada unsur Warna, Warna memberikan suatu desain suatu makna dan tujuan."
    
    pa "Pemilihan warna yang digunakan tidak boleh semena-mena, karena jika suatu desain kurang berwarna atau terlalu redup maka desain akan terlihat redup atau kurang menarik."
     
    pa "Sementara pemakaian warna yang terlalu banyak atau terlalu mencorok dapat menyebabkan suatu desain terlihat norak dan kurang enak dipandang."

    hide screen de_1_2

    show screen de_1_3 with fade
    
    pa "Unsur berikutnya adalah Tekstur, tekstur dapat memberikan kesan yang menarik."
    
    pa "Terdapat tekstur yang bisa dirasakan dengan pengelihatan atau tekstur visual, dan tekstur yang dapat dirasakan dengan pengerabaan dan pengelihatan atau tekstur taktil."

    pa "Lalu ada unsur Ruang, unsur ruang merupakan unsur yang digunakan untuk membuat unsur-unsur yang ada pada suatu ruangan atau tempat agar tidak berkesan terlalu menumpuk ataupun penuh, sehingga ruangan yang ada dapat terlihat lebih tenang atau rileks."

    "Pelajaran dilanjutkan dengan tampilan gambar-gambar yang diperlihatkan oleh Pak Andy."

    "Kamu mendengarkan dan mencatat apa yang menurutmu penting."

    "Kelas berjalan dengan tenang hingga waktu pertemuan telah berakhir."

    hide screen de_1_3

    scene bg campus class with fade

    pa normal "Yak terimakasih telah menghadiri pertemuan hari ini, sampai jumpa di pertemuan kita yang selanjutnya."

    t normal "terimakasih pak"

    t "terimakasih…"

    "Sekarang sudah menunjukan pukul 02.00, Pak Andy meninggalkan ruang kelas tanpa memberikan tugas untuk mata kuliah." 
    
    "Satu-persatu teman kelasmu juga ikut meninggalkan ruang kelas."

    "Kamu mengemas barang-barangmu dan segera meninggalkan ruangan." 

    scene bg campus parking lot with fade
    
    "Merasa sangat lelah dengan hari pertama kuliahmu, kamu bergegas menuju motor yang kamu parkirkan di parkiran kampus."

    "Setelah menyalakann motormu, tidak ada tujuan lain selain menuju kosan untuk beristirahat."

    "Brummmm"

    call attend_de from _call_attend_de
    call attend_class from _call_attend_class_8

    call change_timephase from _call_change_timephase_8
    call screen mapUI

label de_2:

    scene bg campus class with dissolve

    pa normal "Bertemu lagi dengan saya pada hari ini untuk perkuliahan mata kuliah Desain Elementer pada pertemuan yang kedua."

    "[pa] memasuki ruang kelas dan langsung memulai perkuliahan pada siang hari ini."

    pa "Pertemuan Desain Elementer yang kedua ini kita akan membahas mengenai prinsip-prinsip yang digunakan pada seni rupa."

    pa "Kemudian kita juga akan membahas mengenai warna."

    pa "Pertama saya akan menerangkan mengenai prinsip seni."

    show screen de_2_1 with fade

    pa "Prinsip Kesatuan atau Unity, prinsip ini menekankan pada bagian-bagian pada karya seni yang merupakan suatu kesatuan untuk saling mendukung dan sistematik dalam membentuk suatu karya seni."

    pa "Kemudian Prinsip Keseimbangan, prinsip ini berkaitan dengan bobot yang ada pada karya seni. 
    Bobot yang dimaksud bukan selalu mengenai berat namun keseimbangan antara unsur-unsur yang ada pada suatu karya seni."

    pa "Lalu Prinsip Irama pada seni biasanya berkaitan dengan penggunaan unsur secara berulang-ulang. Pengulangan unsur tersebut bisa dilakukan dengan perubahan ataupun secara kontinyu."

    pa "Prinsip seni yang berikutnya adalah Prinsip Penekanan, prinsip ini menekankan atas unsur-unsur yang ada dalam seni rupa memiliki prioritas atas unsur-unsur yang lain. Sehingga suatu unsur terasa lebih dominan daripada unsur lainnya."

    hide screen de_2_1

    show screen de_2_2 with fade   

    pa "Setelah itu Prinsip Proporsi, prinsip memperlihatkan perbandingan antara suatu unsur dengan unsur lainnya. 
    Perbandingan tersebut dapat berupa pertimbangan seperti besar-kecil, luas sempit, panjang pendek dan lain sebagainya."

    pa "Prinsip keselarasan, prinsip ini juga dikenal sebagai prinsip harmoni dimana unsur-unsur yang digunakan pada karya seni memiliki kesamaan, kesesuaian, dan tidak adanya pertentangan antar unsur."

    pa "Kurang lebih untuk prinsip pada seni seperti itu ya. Kita akan lanjut ke Teori Warna dan Roda Warna."

    pa "Teori Warna merupakan sebuah pedoman penggunaan warna yang dapat digunakan untuk mengkomunikasikan dan menyampaikan pesan melalui warna secara visual."

    pa "Sir Isaac Newton menumukan apa yang dinamakan Roda Warna, Roda Warna mengkelompokan warna dengan tiga kelompok yaitu Warna Primer, Warna Sekunder, dan Warna Tersier."

    hide screen de_2_2

    show screen de_2_3 with fade

    pa "Warna Primer, warna primer merupakan warna dasar yang tidak bisa dibuat menggunakan gabungan warna lainnya. Contoh warna primer adalah warna merah, biru, dan kuning."

    pa "Warna Sekunder, merupakan warna yang didapatkan setelah menggabungkan dua atau lebih warna primer. Contoh warna sekunder adalah warna hijau dari gabungan warna kuning dan biru."

    pa "Warna Tersier, adalah warna yang diciptakan dengan menggabungkan warna primer dan sekunder. Contoh warna tersier adalah warna magenta yang didapatkan dari gabungan warna merah dan ungu."

    "[pa] memberikan beberapa contoh warna dan menjelaskannya."

    "Tidak lama kemudian, [pa] melihat ke arah jam yang ada di dinding."

    hide screen de_2_3

    pa normal "Karena sudah jam segini dan kebetulan saya ada tugas dan harus meninggalkan kampus jadi saya akan meninggalkan tugas untuk dikumpulkan minggu depan ya."

    pa "Nanti saya kirim keperwakilan kelas."

    pa "Kelas sekarang saya tutup, cukup sekian dan terimakasih atas partisipasinya."

    t normal "Terimakasih pak."

    r normal2 "Terimakasih."

    pa "Sampai jumpa dipertemuan selanjutnya teman-teman."

    "Kemudian [pa] meninggalkan ruang kelas, kuliah hari ini pun berakhir."

    "Setelah mengemas barang-barang dan mengobrol untuk sebentar bersama teman sekelasmu, kamupun meninggalkan ruangan untuk pulang."

    call attend_de from _call_attend_de_1
    call attend_class from _call_attend_class_9

    call change_timephase from _call_change_timephase_9
    call screen mapUI

label uts_de:

    scene bg campus class with dissolve

    "Setelah menikmati waktu istirahat, kini sudah waktunya kamu untuk melakukan UTS terakhir pada hari ini. "

    "Seperti sebelumnya ketika mendekati ruang UTS kamu melihat lembar berisikan informasi posisi tempat duduk masing-masing mahasiswa peserta UTS yang ditempel pada pintu kelas."

    "Setelah memastikan dimana posisi tempat dudukmu, kamu memasuki ruang kelas tersebut."

    "Sesuai instruksi dosen pengawas UTS, tas-tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    bn normal "Selamat siang teman-teman kita memasuki waktu UTS terakhir pada hari ini."

    bn "Saya disini akan mengawasi berjalannya UTS mata kuliah Desain Elementer pada siang hari ini, saya harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    bn "Soal akan saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    bn "Saya harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Desain Elementer ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

    "Merasa cukup dengan persiapanmu, kamu mulai mengisi biodatamu pada lembar jawab sebelum mulai menelaah soal-soal UTS yang ada."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    "(Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    "(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)"

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    menu:
        "Mulai!":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS."
    "1. Unsur seni paling dasar dan merupkan satuan paling kecil yaitu?"
    menu:
        "A. Garis.":
            "A. Garis."
        "B. Ruang.":
            "B. Ruang."
        "C. Titik.":
            "C. Titik."
            $a_deTS += 20 
        "D. Warna.":
            "D. Warna."
        "E. Bidang.":
            "E. Bidang."
    "2. Kenapa ketika kita membuat sebuah seni atau desain kita memerlukan untuk mengetahui unsur-unsur seni yang ada didalamnya kecuali?"
    menu:
        "A. Agar karya seni yang dibuat lebih dapat bisa dinikmati lebih baik.":
            "A. Agar karya seni yang dibuat lebih dapat bisa dinikmati lebih baik."
        "B. Sehingga unsur yang ada dalam karya seni mencipatakan harmoni satu sama lain.":
            "B. Sehingga unsur yang ada dalam karya seni mencipatakan harmoni satu sama lain."
        "C. Sehingga karya seni mampu menampilkan seni yang lebih menarik.":
            "C. Sehingga karya seni mampu menampilkan seni yang lebih menarik."
        "D. Sehingga karya seni menjadi lebih mahal.":
            "D. Sehingga karya seni menjadi lebih mahal."
            $a_deTS += 20
        "E. Agar karya seni mampu menampilkan unsur-unsurnya secara lebih jelas.":
            "E. Agar karya seni mampu menampilkan unsur-unsurnya secara lebih jelas."
    "3. Penggunaan suatu unsur seni agar lebih menonjol atau lebih dominan pada suatu unsur ketimbang unsur lainnya merupakan penjelasan dari prinsip seni?"
    menu:
        "A. Kesatuan.":
            "A. Kesatuan."
        "B. Harmoni.":
            "B. Harmoni."
        "C. Penekanan.":
            "C. Penekanan."
            $a_deTS += 20
        "D. Irama.":
            "D. Irama."
        "E. Proprosi.":
            "E. Proprosi."
    "4. Pernyataan yang benar mengenai teori warna pada suatu desain?"
    menu:
        "A. Pengaplikasian teori warna yang baik pada desain mampu menjadikan desain lebih bermakna atau lebih jelas.":
            "A. Pengaplikasian teori warna yang baik pada desain mampu menjadikan desain lebih bermakna atau lebih jelas."
            $a_deTS += 20
        "B. Teori warna tidak begitu berpengaruh pada desain.":
            "B. Teori warna tidak begitu berpengaruh pada desain."
        "C. Teori warna membuat desain lebih tidak menarik.":
            "C. Teori warna membuat desain lebih tidak menarik."
        "D. Dengan teori warna desain menjadi lebih rumit.":
            "D. Dengan teori warna desain menjadi lebih rumit."
        "E. Teori warna tidak memiliki banyak manfaat pada desain.":
            "E. Teori warna tidak memiliki banyak manfaat pada desain."
    "5. Contoh warna dari kelompok warna primer adalah?"
    menu:
        "A. Merah, Ungu, Kuning.":
            "A. Merah, Ungu, Kuning."
        "B. Biru, Ungu, Merah.":
            "B. Biru, Ungu, Merah."
        "C. Kuning, Biru, Ungu.":
            "C. Kuning, Biru, Ungu."
        "D. Kuning, Merah, Biru.":
            "D. Kuning, Merah, Biru."
            $a_deTS += 20
        "E. Kuning, Merah, Putih.":
            "E. Kuning, Merah, Putih."        
            
    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengumpulkan kertas ujianmu, kamu memasukan barang-barangmu pada tas yang sebelumnya dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Menyelesaikan semua UTS pada hari ini, kamu merasa sangat lelah. Bukan hanya tubuhmu yang merasa lelah namun pikiranmu juga terasa sangat penuh."

    "Setelah mengobrol dengan teman-temanmu untuk beberapa menit, kamu memutuskan untuk pulang ke kosan."

    "Istirahat merupakan hal yang kamu perlukan saat ini. Setelah berpamitan dengan teman-temanmu kamu meninggalkan kampus."
    $application += 7
    if a_deTS < 50:
        $ knowledge+=1
        $ practice+=1
    elif a_deTS < 81:
        $ knowledge+=2
        $ practice+=2
    else:
        $ knowledge+=3
        $ practice+=3
    call change_timephase from _call_change_timephase_10
    call screen mapUI

label de_3:

    scene bg campus class with dissolve

    "Setelah jam istirahat berakhir, kamu dan teman-temanmu mulai memasuki kelas yang akan digunakan untuk pembelajaran terakhir pada hari ini."

    "Ketika memasuki ruang kelas, [pa] yang mengajar mata kuliah desain elementer telah berada di dalam ruang kelas."

    pa normal "Selamat siang teman-teman, silahkan masuk sembari menunggu teman-teman yang lain masuk kelas."

    "Tidak memakan waktu lama, satu persatu teman kelasmu memasuki ruangan, setelah dirasa mahasiswa yang berada dalam ruangan sudah banyak, [pa] membuka pertemuan pada siang hari ini."

    pa "Selamat siang, sepertinya sudah pada masuk ya… Kalau begitu bapak mulai kelas pada siang hari ini."

    pa "Bertemu lagi kita pada mata kuliah Desain Elementer pertemuan ke 3. Pada pertemuan siang hari ini, kita akan membahas lebih detail mengenai apa yang telah kita bahas pada pertemuan sebelumnya."

    pa "Ya pada pertemuan sebelumnya kita telah sedikit membahas mengenai warna, di siang hari ini kita akan membahasnya lagi secara lebih mendetail."

    pa "Apa itu warna?"

    show screen de_3_1 with fade

    pa class "Warna merupakan salah satu aspek visual yang terdapat pada spektrum cahaya. 
    Identitas warna dapat diketahui melalui panjang gelombang yang dimiliki. 
    Semisal panjang gelombang 711 nanometer merupakan panjang gelombang dari warna hijau."

    pa "Seperti yang kita tahu, mempelajari warna memiliki banyak manfaat pada kehidupan kita. 
    Warna dapat berpengaruh dalam berbagai bidang seperti seni, desain, psikologi, ilmu pengetahuan, teknologi, dan budaya."

    pa "Bapak akan mengulang sedikit materi mengenai warna yang telah disampaikan pada pertemuan sebelumnya."

    pa "Sir Isaac Newton menemukan apa yang dinamakan Roda Warna, sementara Brewster mengelompokkan warna menjadi empat kelompok yaitu Warna Primer, Warna Sekunder, Warna Tersier, dan Netral."

    hide screen de_3_1

    show screen de_3_2 with fade

    pa "Warna Primer, warna primer merupakan warna dasar yang tidak bisa dibuat menggunakan gabungan warna lainnya. Contoh warna primer adalah warna merah, biru, dan kuning."

    pa "Warna Sekunder, merupakan warna yang didapatkan setelah menggabungkan dua atau lebih warna primer. Contoh warna sekunder adalah warna hijau dari gabungan warna kuning dan biru."

    pa "Warna Tersier, adalah warna yang diciptakan dengan menggabungkan warna primer dan sekunder. Contoh warna tersier adalah warna magenta yang didapatkan dari gabungan warna merah dan ungu."

    pa "Selain ketiga warna tersebut, pada teori yang dikenalkan oleh Brewster terdapat satu golongan warna lagi, yaitu warna netral."

    pa "Warna netral merupakan warna yang digunakan untuk menyeimbangkan dan membantu warna lain agar terlihat lebih fokus. "

    pa "Contoh dari warna netral adalah warna monokrom atau hitam dan putih, dan warna earth tone seperti krem, cokelat, dan warna-warna yang menyerupai bumi lainnya."

    pa "Kemudian setelah membahas macam-macam pengelompokkan kategori warna, kita akan membahas mengenai skema warna."

    hide screen de_3_2

    show screen de_3_3 with fade

    pa "Skema warna merupakan perpaduan atau kombinasi warna yang digunakan dalam seni dan desain."

    pa "Contoh dari skema warna adalah sebagai berikut:"

    pa "Monokromatik, skema warna monokromatik merupakan skema warna yang masih menggunakan rona atau hue yang sama. Skema ini terdiri dari suatu rona dengan variasi yang lebih cerah atau gelap."

    pa "Analog, skema warna analog merupakan skema warna yang menggunakan warna yang bersebelahan pada roda warna. Letaknya yang bersebelahan membuat warna yang digunakan terlihat mirip."

    pa "Complementary, skema warna yang berbeda dengan skema analog yang menggunakan warna yang bersebelahan pada roda warna. Skema ini menggunakan warna yang kontradiktif atau berlawanan dengan warna yang digunakan pada roda warna."

    pa "Triadic, merupakan skema warna yang menggunakan tiga warna pada roda warna. Warna-warna yang digunakan pada skema ini memiliki jarak yang sama antara satu sama lainnya."

    pa "Masih ada beberapa skema warna yang lain, namun pada siang hari ini kita akan membahas seputar 4 skema itu dulu ya."

    hide screen de_3_3

    show screen de_3_4 with fade

    pa "Lalu pembahasan mengenai warna yang berikutnya adalah mengenai Tint, Tone, dan Shades."

    pa "Apa itu Tint? Tint merupakan sebuah variasi warna yang didapatkan dari kombinasi sebuah warna dengan warna putih yang akan memberikan sebuah variasi kecerahan dari sebuah warna."

    pa "Apa itu Tone? Berbeda dengan Tint yang mendapatkan kombinasi sebuah warna dengan mencampurkan warna putih, Tone mendapatkan variasi keburaman sebuah warna dengan menambahkan warna abu-abu pada suatu warna."

    pa "Lalu yang terakhir adalah Shades, Shades merupakan variasi warna yang didapatkan ketika menambahkan warna hitam ke suatu warna. Shades akan menghasilkan variasi gelapnya suatu warna."

    pa "Mungkin itu saja pembahasan kita di siang hari ini, selanjutnya bapak akan memperlihatkan contoh-contoh dari apa yang bapak terangkan barusan."

    "[pa] kemudian memperlihatkan slide power point yang berisi gambar-gambar mengenai materi yang diterangkan sebelumnya."

    hide screen de_3_4

    scene bg campus class with fade

    "Setelah sesi tanya selesai, [pa] mengakhiri kelas pada siang hari ini."

    pa normal "Mungkin itu saja ya untuk siang hari ini. Kita lanjutkan untuk minggu depan kelasnya."

    pa "Oh iya untuk kelas minggu depan kita isi dengan quiz yaa."

    t normal "Waahhhh"

    t "Materi apa saja pak nanti di quiz?"

    t "Yahhh harus belajar dong"

    "Mendengarkan informasi mengenai quiz yang akan dilakukan pada minggu depan, mahasiswa mulai mengutarakan keluh kesah mereka."

    pa "Hahaha enggak susah kok, anggap aja buat latihan ujian akhir semester nanti kan."

    pa "Untuk materinya dari yang bapak sudah ajarkan ya teman-teman."

    r normal2 "Berarti dari materi sebelum uts pak?"

    pa "Iya, dari materi yang awal ya."

    t "Yahhhh"

    t "Banyak banget dong pak."

    pa "Udah tinggal belajar saja, enggak susah kok nanti."

    pa "Yaudah kalo begitu bapak tutup ya pertemuan siang hari ini."

    pa "Terimakasih telah mengikuti pelajaran siang hari ini, sampai berjumpa pada pertemuan selanjutnya teman-teman."

    t "Terimakasih pak."

    t "Terimakasihhhh"

    t "Sekarang waktunya pulang-pulangg"

    mc normal jacket "Huh minggu akhir malah ada quiz begini."

    "Kelas ditutup dan mahasiswa mulai keluar dari ruang kelas. Tidak ada kelas lagi siang hari ini, pertanda sudah waktunya dirimu untuk pulang."

    call attend_de from _call_attend_de_2
    call attend_class from _call_attend_class_10

    call change_timephase from _call_change_timephase_11
    call screen mapUI

label de_4:

    scene bg campus class with dissolve

    "Istirahat telah usai, kini telah memasuki jam untuk kelas terakhir yang ada pada hari ini."

    "Mata kuliah selanjutnya adalah Desain Elementer. Kamu teringat pada pertemuan kali hari ini, mata kuliah desain elementer akan diadakan quiz."

    "Setelah memasuki ruang kelas, kamu langsung mempersiapkan dirimu untuk membaca ulang beberapa materi yang telah diajarkan."

    "Selama beberapa menit kamu membaca ulang materi, akhirnya [pa] memasuki ruang kelas."

    pa normal "Selamat siang teman-teman, kita bertemu lagi pada siang hari ini. Apa ada yang ingat apa yang akan kita lakukan hari ini?"

    t normal "Quiz kan pak?"

    t "Enggak jadi quiz hari ini kan pak?"

    pa "Ahahaha jadi dong, iya hari ini kita akan melakukan quiz pada siang hari ini."

    pa "Langsung saja untuk menyingkat waktu, soal dapat kalian akses pada laman berikut."

    "[pa] menulis alamat sebuah laman pada whiteboard yang berisi soal-soal untuk quiz pada siang hari ini."

    pa "Kalian kerjakan saja pada kertas, tulis nama dan NIM kalian lalu kumpulkan ketika jam telah usai ya."

    "Kamu membuka alamat laman yang ditulis oleh [pa] menggunakan HPmu, setelah membuka laman tersebut kamu mulai menyiapkan secarik kertas dan bolpoinmu."

    "Kamu mulai mengerjakan soal yang terdapat pada layar HPmu. Kamu melihat terdapat 5 soal yang ada lembar quiz."

    show screen de_4_0 with fade

    "Soal pertama yang terdapat lembar soal adalah:"

    "Gabungan dari beberapa garis yang membentuk suatu kesatuan dan membuat ruang yang tertutup merupakan pengertian dari unsur seni?"

    mc normal jacket "Hmmm kalau gabungan unsur titik itu kan garis, kalau gabungan garis berarti…"

    show screen de_4_1 with dissolve

    menu:
        "a. Unsur Tekstur":
            "a. Unsur Tekstur"

            mc "Ini mah unsur tekstur"

        "b. Unsur Bidang":
            "b. Unsur Bidang"
            $ a_deC += 2

            mc "Unsur bidang kan ya?"

        "c. Unsur Ruang":
            "c. Unsur Ruang"

            mc "Seharusnya sih unsur ruang"

    "Selesai menjawab pertanyaan pertama, kamu kemudian melanjutkan ke pertanyaan kedua."

    hide screen de_4_1 with dissolve

    "2. 	Manakah dibawah ini yang bukan merupakan prinsip-prinsip seni?"

    mc "Kalau enggak salah waktu itu diterangin 6 prinsip seni, masih inget enggak ya?"

    show screen de_4_2 with dissolve

    menu:

        "Prinsip Kesatuan":

            "a. Prinsip Kesatuan"

            mc "Prinsip kesatuan? Kayaknya bukan salah satu prinsip seni deh."

        "Prinsip Penekanan":

            "b. Prinsip Penekanan"

            mc "Prinsip penekanan hmm… prinsip penekanan? Bukan-bukann"

        "Prinsip Keselarasan":

            "c. Prinsip keselarasan"

            mc "Kalau yang satu ini pasti bukan prinsip seni dah"

        "Prinsip Perbedaan":

            "d. Prinsip Perbedaan"
            $ a_deC += 2

            mc "Prinsip perbedaan itu bukan salah satu prinsip seni."

    "Menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."

    hide screen de_4_2 with dissolve

    "3. Teori warna mengelompokkan warna menjadi beberapa golongan warna, manakah dibawah ini yang bukan merupakan warna dalam satu golongan warna pada teori warna?"

    show screen de_4_3 with dissolve

    menu:
        
        "Merah, Hitam, Ungu":

            "a. Merah, Hitam, Ungu"
            $ a_deC += 2

            mc "Ini sih ga dalam satu golongan warna."

        "Hitam, Putih, Cokelat":

            "b. Hitam, Putih, Cokelat"

            mc "Kok ada cokelat sih, bukan dalam satu golongan ini."

        "Orange, Hijau, Ungu":

            "c. Orange, Hijau, Ungu"

            mc "Golongan warna apaan ini, random banget sih berarti jawabannya ini nih."

    "Setelah menjawab pertanyaan nomor 3, tinggal 2 pertanyaan lagi yang tersisa."

    "Merasa cepat ingin menyelesaikan quiz ini, kamu langsung membaca pertanyaan nomor 4."

    hide screen de_4_3 with dissolve

    "4. 	Menggunakan warna-warna yang bersebelahan satu sama lain pada roda warna merupakan contoh pengaplikasian dari skema warna?"

    show screen de_4_4 with dissolve

    menu:
        "Komplementer":

            "a. Komplementer"

            mc "Kalau engga salah ini skema komplementer sihh…"

        "Monokromatik":

            "b. Monokromatik"

            mc "Monokromatik kalo ga salah warnanya mirip-mirip gitu kan? Kalau bersebelahan harusnya warnanya mirip."

        "Analog":

            "c. Analog"
            $ a_deC += 2

            mc "Analog itu merupakan skema warna yang menggunakan warna yang bersebelahan pada roda warna."

        "Triadic":

            "d. Triadic"

            mc "Duh lupaaa…. Jawab yang ini saja lah."

    "Selesai menjawab, kini ada satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan quiz pada siang hari ini."

    hide screen de_4_4 with dissolve

    "5. Variasi warna yang dapat kita dapatkan dengan mencampur warna putih, hitam, atau abu-abu disebut dengan warna… kecuali."

    show screen de_4_5 with dissolve

    menu:
        "Shades":

            "a. Shades"

            mc "Shades?"

        "Monokrom":

            "b. Monokrom"
            $ a_deC += 2

            mc "Kalau monokrom berarti hitam putih kan…	"

        "Tint":

            "c. Tint"

            mc "Kayaknya yang ini dehhh…"

        "Tone":

            "d. Tone"

            mc "Tone kayaknya bukan deh."

    hide screen de_4_5 with dissolve

    hide screen de_4_0 with dissolve

    scene bg campus class with fade

    "Dengan memilih jawaban terakhir, semua soal yang terdapat pada lembar soal sudah semuanya kamu selesaikan."

    "Kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawabanmu."

    "Tidak lupa sebelumnya kamu menulis nama dan NIM mu pada lembar jawaban."

    "Melihat sekelilingmu kamu melihat beberapa dari temanmu masih mengerjakan quiz yang ada. Meskipun sebagian besar dari temanmu telah menyelesaikan quiz yang diberikan."

    "Setelah mengumpulkan lembar jawaban, kamu kembali ke bangkumu dan menunggu hingga semua temanmu menyelesaikan quiz yang diberikan."

    scene bg campus class with dissolve

    "Kurang lebih 30 menit, semua mahasiswa telah menyelesaikan quiz yang diberikan. Kini [pa] sedang menjelaskan mengenai materi yang akan digunakan sebagai bahan soal untuk ujian akhir semester."

    pa normal "Jadi nanti untuk ujian akhir semester, materinya adalah semua materi yang telah bapak berikan ya."

    pa "Mungkin bisa jadi bapak mengambil dari soal yang digunakan untuk quiz nanti."

    pa 'Jadi selamat belajar ya teman-teman.'

    t normal "Jangan susah-susah ya pak."

    t "Hmmm berarti materi-materi tadi ya…"

    t "Kalau soal yang tadi sih aku lumayan bisa, semoga aja mirip-mirip."

    r normal2 "Berarti ringkasan materi yang dulu masih bisa digunain yeyyy"

    pa "Kalau begitu bapak tutup ya, pertemuan hari ini. Selamat belajar dan semoga mendapatkan hasil yang diinginkan pada ujian nanti."

    pa "Terimakasih sudah mengikuti kelas sampai pertemuan kali ini, sampai jumpa pada pertemuan selanjutnya teman-teman."

    t "Terimakasih pak."

    t "Terimakasihhh"

    r "Terimakasih juga pak."

    "Dengan begitu kelas ditutup dan pembelajaran untuk hari ini telah usai. Kamu keluar dari ruangan kelas dan melanjutkan aktivitasmu berikutnya."

    call attend_de from _call_attend_de_3
    call attend_class from _call_attend_class_11

    call change_timephase from _call_change_timephase_12
    call screen mapUI

label uas_de:

    scene bg campus upper hall with fade

    "Selesai menggunakan jam istirahat, kamu kembali ke area dimana teman-temanmu sedang belajar bersama."

    "Sama seperti sebelumnya, terlihat mahasiswa-mahasiswa lain juga sedang membaca materi perkuliahan yang akan diujikan."

    "Masih tersisa sekitar 10 menit lagi sebelum ujian terakhir pada hari ini dimulai."

    "Kamu duduk bersandar di tembok kelas sembari mengingat materi yang telah kamu pelajari."

    "Mengisi beberapa menit sebelum ujianmu dengan mengingat-ingat materi perkuliahan sebelum mengikuti ujian berikutnya."

    "Tidak lama kemudian pintu ruang kelas ujian dibuka, satu persatu mahasiswa memasuki ruang kelas "

    "Kemudian kamu juga ikut berdiri dan bergegas masuk ke ruang ujian."

    scene bg campus class with dissolve

    pause 1.5

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

    "({i}Ketika {b}UAS{/b} terdapat 5 soal pilihan ganda yang harus dikerjakan untuk menyelesaikan ujian)"

    "({i}Setiap pertanyaan akan ditampilkan dan akan muncul dalam waktu 45 detik{/i})"

    "({i}Ketika waktu 45 detik habis, soal akan hilang dari layar{/i})"

    "({i}Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya{/i})"

    "({i}Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal{/i})"

    "({i}Setelah pemain menjawab nomor terakhir, maka UAS akan berakhir.{/i})"

    "({i}Perlu diketahui UAS pada kampus dapat dilaksanakan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.{/i})"

    "({i}Soal UAS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.{/i})"

    "Selesai membaca panduan pengerjaan pada lembar soal, kamu lalu bersiap menjawab soal-soal ujian yang ada."

    "Mulai mengerjakan UAS?"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UAS"

    "Soal pertama yang terdapat lembar soal adalah:"

    label soalde1:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_de1'

        show screen deas_1 with dissolve
        "1. Penggunaan unsur-unsur yang memiliki kesamaan, kesesuaian, dan tidak memiliki pertentangan unsur merupakan penjelasan dari prinsip?"
        mc normal jacket "prinsip…"
        show screen countdown
        menu:
            "A. Prinsip Proporsi":
                "a. Prinsip Proporsi"
                mc "Proporsi itu perbandingan ukuran gitu gak sih?"

            "B. Prinsip Harmoni":
                "b. Prinsip Harmoni"
                mc "Prinsip harmoni itu sama kaya prinsip keselarasan kan."
                $ a_deAS += 5

            "c. Prinsip Irama":
                "c. Prinsip Irama"
                mc "Emang prinsip irama yah?"

            "D. Prinsip Keseimbangan":
                "d. Prinsip Keseimbangan."
                mc "Prinsip Keseimbangan itu keseimbangan bobot unsur seni kan?"
        hide screen countdown
        "Kamu menjawab pertanyaan pertama dengan lancar, setelah beberapa kali memeriksa jawaban kamu yakin akan jawaban pertamamu."
        hide screen deas_1 with dissolve
        jump soalde2

    label telat_de1:

        "Kamu terlambat menjawab pertanyaan, soal no 1 dilewati"

    hide screen deas_1 with dissolve

    label soalde2:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_de2'

        show screen deas_2 with dissolve
        "Kemudian kamu lanjut menuju pertanyaan selanjutnya."

        "2. 	Manakah dibawah ini yang bukan merupakan salah satu pengelompokan warna?"
        mc "Pengelompokan warna itu ada 4….."
        show screen countdown
        menu:

            "A. Warna Primer":
                "a. Warna Primer"
                mc "Warna primer itu merah, biru, sama kuning."

            "B. Warna Sekunder":
                "b. Warna Sekunder"
                mc "Warna sekunder itu warna hasil pencampuran warna primer, semisal hijau kan."
                
            "C. Warna Irama":
                "c. Warna Irama"
                mc "Irama kan salah satu prinsip, bukan pengelompokan warna"
                $ a_deAS += 5

            "D. Warna Netral":
                "d. Warna Netral"
                mc "Warna netral itu yang hitam, putih, sama warna-warna bumi"
        hide screen countdown
        "Berhasil menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."
        hide screen deas_2 with dissolve
        jump soalde3

    label telat_de2:

        "Kamu terlambat menjawab pertanyaan, soal no 2 dilewati"

    hide screen deas_2 with dissolve

    label soalde3:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_de3'

        show screen deas_3 with dissolve
        "3. Menggunakan warna-warna yang bersebelahan satu sama lain pada roda warna merupakan contoh pengaplikasian dari skema warna?"
        show screen countdown
        menu:

            "A. Komplementer":
                "a. Komplementer"
                mc "Kalau engga salah ini skema komplementer sihh…"

            "B. Monokromatik":
                "b. Monokromatik"
                mc "Monokromatik kalo ga salah warnanya mirip-mirip gitu kan? Kalau bersebelahan harusnya warnanya mirip."

            "C. Analog":
                "c. Analog"
                mc "Analog itu merupakan skema warna yang menggunakan warna yang bersebelahan pada roda warna."
                $ a_deAS += 5

            "D. Triadic":
                "d. Triadic"
                mc "Duh lupaaa…. Jawab yang ini saja lah."
        hide screen countdown
        "Setelah menjawab pertanyaan nomor 3, kamu bergegas menuju pertanyaan selanjutnya."

        "Tersisa dua soal ujian lagi, merasa cepat ingin menyelesaikan quiz ini, kamu langsung membaca pertanyaan nomor 4."
        hide screen deas_3 with dissolve
        jump soalde4

    label telat_de3:

        "Kamu terlambat menjawab pertanyaan, soal no 3 dilewati"

    hide screen deas_3 with dissolve

    label soalde4:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_de4'

        show screen deas_4 with dissolve
        "4. 	Gabungan dari beberapa garis yang membentuk suatu kesatuan dan membuat ruang yang tertutup merupakan pengertian dari unsur seni?"
        show screen countdown
        menu:

            "A. Titik":
                "a. Titik"
                mc "Titik itu unsur seni paling dasar…"

            "B. Garis":
                "b. Garis"
                mc "Garis itu gabungan dari beberapa titik"

            "C. Ruang":
                "c. Ruang"
                mc "Ruang?? Bener gak yaa?"

            "D. Bidang":
                "d. Bidang"
                mc "Harusnya bidang, karena garis yang membuat ruang tertutup"
                $ a_deAS += 5
        hide screen countdown
        "Selesai menjawab pertanyaan ke 4, kini hanya tinggal satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan ujian akhir Desain elementer pada pagi hari ini."

        "Setelah mengecek jawaban no 4, kamu langsung membaca soal terakhir yang terdapat pada lembar soal ujian."
        hide screen deas_4 with dissolve
        jump soalde5

    label telat_de4:

        "Kamu terlambat menjawab pertanyaan, soal no 4 dilewati"

    hide screen deas_4 with dissolve

    label soalde5:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_de5'

        show screen deas_5 with dissolve
        "5. Manakah dibawah ini yang bukan merupakan istilah yang mengacu pada teori warna?"
        show screen countdown
        menu:

            "A. Monolog":
                "a. Monolog"
                mc "Hah monolog?"
                $ a_deAS +=5

            "B. Analog":
                "b. Analog"
                mc "Analog itu dalam roda warna itu kan…"

            "C. Tone":
                "c. Tone"
                mc "Tone itu kombinasi warna dengan warna putih itu kalau gak salah."

            "D. Warna Kebumian":
                "d. Warna Kebumian"
                mc "Warna kebumian itu warna netral kaya coklat, krem, dan yang kaya gitu lah…"
        hide screen countdown
        "Setelah memilih jawaban untuk pertanyaan terakhir, semua soal yang terdapat pada lembar soal ujian sudah kamu selesaikan."
        hide screen deas_5 with dissolve
        jump end_de

    label telat_de5:

        "Kamu terlambat menjawab pertanyaan, soal no 5 dilewati"

    hide screen deas_5 with dissolve

    label end_de:

        if a_deAS*4 < 50:
            $ knowledge+=1
            $ practice+=1
        elif a_deAS*4 < 81:
            $ knowledge+=3
            $ practice+=3
        else:
            $ knowledge+=4
            $ practice+=4

        "Kamu melihat sekelilingmu, masih ada temanmu yang masih mengerjakan ujian, namun ada juga yang sudah beranjak dari bangku ujian."

        "Sebelum mengumpulkan jawaban, tidak lupa kamu mengecek apakah biodata dan jawaban yang kamu isi semuanya sudah benar."

        "Selesai mengecek, kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawaban ujianmu."

        "Lalu tidak lupa untuk mengambil tas ransel milikmu yang ketika ujian berlangsung diletakkan di depan kelas secara rapi."

        "Dengan selesainya ujian desain elementer pada siang hari ini, menandakan berakhirnya ujian pada hari ini."

        "Setelah menjalani 3 ujian akhir, ujian hari pertama telah usai, kini tersisa dua hari ujian lagi sebelum minggu ujian selesai."

        "Kamu bersegera untuk pulang untuk berisitirahat di kosan."
        $application += 7
        call change_timephase from _call_change_timephase_13
        call screen mapUI

label attend_de:

    $ a_deA +=1
    $ a_deN +=8

    return



label first_hima:

    scene bg campus class with fade

    r normal2 "Maaf temen-temen.... sebelum pada pulang, boleh minta waktunya sebetar yaa...."

    t normal "Hmmm ? Ada apa [r]?"

    r "Ini semalem aku dititipi sama kakak tingkat kita, suruh menyampaikan pengumuman sebentar..."

    t "Pengumuman apa tuhh?"

    "Para mahasiswa yang sebelumnya sudah berjalan untuk meninggalkan ruangan berhenti dan memperhatikan [r]."

    r "Jadi temen-temen udah pada tau kan sebelumnya, kalau pasti di setiap program studi itu pasti ada himpunan atau organisasi mahasiswanya?"

    t "Iyaa tau tau.."

    t "Kayak osis gitu kah?"

    t "Iya tapi tiap prodi ada gituu..."

    r "Nah ituu... di prodi kita ada yang namanya {b}HIMAKOMSI{/b} atau Himpunan Mahasiswa KOMSI."

    r "Jadi, semalem aku dapat informasi, kalau HiMa ini mau ngadain perekrutan anggota baru."

    r "Jadi buat temen-temen yang tertarik apalagi yang suka banget berorganisasi boleh banget kalau mau gabung yaa.."

    t "Daftarnya sistemnya gimana [r]?"

    r "Bagi yang tertarik untuk bergabung, besok siang ini bisa datang langsung ke kampus ke ruang U-203."

    t "Jam berapa [r]?"

    t "Syaratnya apa aja [r]?"

    r "Besok jam 9 ya temen-temen, yang dibilang ke aku sih tinggal berangkat aja jadi ya mungkin ga harus bawa apa-apa."

    t "Langsung wawancara kah kalau begitu?"

    r "Uhmm... kurang tau juga sih, tapi ya itu yang pengin gabung bisa datang besok ya temen-temen..."

    r "Yaudah kalau begitu... terimakasih atas waktunya dan hati-hati di jalan temen-temen...."

    t "Okee masama [r]...."

    "Setelah [r] selesai menyampaikan informasi, kamu melihat terdapat 2 cara teman kelasmu meresponnya."

    "Mahasiswa yang tertarik untuk bergabung menjadi himpunan langsung pergi meninggalkan kelas. 
    Sementara mahasiswa yang tertarik untuk bergabung terlihat bergerombol dan bertanya pada [r]."

    "Dirimu sendiri tidak langsung memutuskan untuk memilih bergabung dengan himpunan mahasiswa atau tidak."

    "Beranjak dari tempat dudukmu, kamu berjalan keluar dari ruang kelas dan langsung menuju tempat parkir."

    scene bg black with fade
    pause 1.5

    "Sebelum pulang ke kos kamu sempat mampir pada suatu warung makan untuk mengisi perutmu."

    call eat

    "Setelah perutmu terisi, kamar kos merupakan tujuan selanjutnya pada siang hari ini."

    "Menyegarkan tubuhmu adalah salah satu hal yang ingin kamu lakukan ketika matahari bersinar terik."

    "Kamu melanjutkan perjalanan dan pulang ke kos."

    call change_timephase
    call screen mapUI with dissolve

label join_hima:

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve

    "Setelah lama berpikir, akhirnya kamu memutuskan untuk mendaftar menjadi pengurus himpunan mahasiswa pada program studimu."

    "Kamu berpikir dengan bergabung menjadi himpunan mahasiswa kamu dapat menambah pengalamanmu."

    "Bukan hanya pada berorganisasi tapi juga dalam hal akademik."

    "Meskipun itu akan menyita waktu tapi paling tidak kamu juga akan menerima ilmunya, belum lagi dengan berorganisasi kamu juga akan mendapatkan teman baru."

    "Tentu saja semua itu jika kamu diterima menjadi pengurus."

    mc normal jacket "Paling tidak sudah coba ikut lah ya..."

    mc "Kalau diterima ya syukur kalau tidak ya gimana lagi...."

    "Berganti mengenakan pakaian yang lebih rapi, dan memakai jaketmu kamu keluar dari kamar."

    "Berjalan menuju motor yang masih terparkir berjejer dengan motor penghuni kos lainnya, kamu mengamati kamar yang ada disekitarmu."

    "Berbeda dengan hari kerja, ketika hari libur kamu melihat kamar-kamar disekitarmu masih tertutup rapat."

    mc "Libur terus masih pada tiduran kali ya?"

    "Sampai dimotormu kamu langsung mengecek kondisi bensin yang masih tersisa."

    mc "Masih seperempat, masih banyak juga ya?"

    mc "Tapi ya jarak dari kos ke kampus ya nggak jauh-jauh juga sih..."

    "Menghidupkan motor, dan setelah menunggu beberapa menit kamu akhirnya mengendarai motor keluar dari kos menuju kampus."

    scene bg town street 1 with fade
    pause 0.5
    scene bg town street 2 with fade
    pause 0.5
    scene bg town street 3 with fade
    pause 0.5
    $ placeKeys = 8
    show screen trans_screen with dissolve
    scene bg campus parking lot with dissolve
    pause 0.5

    "Setelah mengendarai motor selama beberapa menit, akhirnya kamu sampai di parkiran kampus."

    "Kampus terlihat sepi, meskipun itu wajar karena hari ini merupakan hari libur."

    "Meskipun terlihat sepi, namun masih terdapat beberapa mahasiswa yang berada di kampus."

    mc normal jacket "Kukira bakal sepi banget... ternyata nggak sepi-sepi juga ya pas libur."

    mc "Apa mereka juga ada urusan sama organisasi mahasiswa masing-masing ya?"

    "Setelah melepas helm, kamu membuka group chat Lane sembari berjalan masuk ke gedung kampus."

    "Beberapa chat mengenai rekruitment pengurus himpunan mahasiswa mengisi timeline dari group."

    "Jam masih menunjukan pukul 08.45, yang berarti masih ada sekitar 15 menit sebelum acara dimulai."

    scene bg campus hall with fade
    pause 0.5
    scene bg campus class with dissolve

    "Sampai di kelas yang dituju, kamu sudah ditunggu oleh salah satu kakak tingkatmu."

    "Duduk di dekat pintu, kakak tingkatmu itu menyuruhmu untuk mengisi daftar hadir terlebih dahulu."

    k "Halo... mau ikut seleksi jadi pengurus himpunan kah?"

    mc normal jacket "Iya kak..."

    k "Ohh kalau gitu isi ini dulu yak..."

    mc "Ohh oke kak."

    "Setelah mengisi daftar hadir, kamu juga harus mengisi semacam kertas untuk identitas dimana nama, nomor induk, dan beberapa data lainnya harus kamu masukan."

    k "Kalau sudah nanti duduk dulu ya? Sambil menunggu yang lain dan nanti kalau udah waktunya satu-satu bakal diwawancara."

    mc "Oh begitu ya ? Makasih kak."

    "Setelah dipersilahkan untuk duduk, kamu mendekati kursi kosong yang terletak pada bagian paling belakang."

    "Tidak aneh dan tidak membuatmu terkejut melihat [r] sudah duduk dan menunggu bersama teman-temannya."

    r normal2 "Ohhh kamu mau daftar juga tah [name]?"

    mc "hahaha iya coba-coba buat nyari pengalaman gitu.. Kalau kamu?"

    r "Aku sih biasa kalau ikut organisasi gitu, jadi kalau enggak ikut rasanya kurang hehe..."

    "{i}Hahaha sudah pasti begitu.{/i}"

    mc "Ohhh... begitu.."

    r "Yap-yap good luck ya [name]"

    mc "Sama-sama..."

    "Setelah tukar-menukar kata dengan [r], kamu duduk di kursi kosong yang tadi kamu tuju."

    "Duduk dan menunggu, itulah hal yang paling tidak 15 menit lagi harus kamu lakukan."

    "Namun tidak lama setelah duduk, tiba-tiba ada yang menempati kursi kosong yang ada disebelahmu."

    siapa "Yo bro!"

    mc "Umm.. Yo"

    "Tidak lain adalah mahasiswa yang sudah beberapa kali kamu lihat, namun setelah kuliah dimulai kamu tidak melihatnya lagi."

    siapa "Perkenalkan... namaku Jonathan Johny Jatmiko temen-temen biasanya manggil TriJe."

    mc "Uhh.. ohh... salam kenal bro namaku [name]."

    j "Salam kenal browski."

    "Kamu masih tercengang kaget, melihat [j] dengan sifatnya yang sangat friendly."

    "Padahal dari penampilan luarnya dia mempunyai fisik yang tinggi dan wajah yang garang."

    mc "Mungkin ini yang disebut jangan menilai buku dari covernya ya hahaha..."

    j "Ngomong apa bro?"

    mc "Ahh engga-engga..."

    j "Ohh okey... btw kamu daftar juga ya?"

    mc "Iya coba-coba nambah pengalaman juga kan?"

    j "Hahaha sama bro, aku juga coba-coba."

    mc "Ngomong-ngomong [j], aku kok nggak pernah liat kamu lagi ya sekarang? bukannya dulu ikut kumpul ya pas pertama sama [pa]?"

    j "Ohh yaa hahahaha... itu aku asal ikut aja, biar tahu informasi... karena pas itu dari dosen pembimbingku belum ketemuan gitu."

    j "Beda kelas juga kan kita? jadi wajar kalau nggak ketemu jadwalnya beda bro."

    mc "Pantes... ga liat kamu waktu kelas, beda kelas juga tah..."

    j "Hahaha begitulah...."

    mc "Setelah itu kamu berlanjut mengobrol hingga kegiatan dimulai."

    scene bg campus class with fade

    "Proyektor telah memproyesikan layar laptop, presentasi dilakukan oleh kakak tingkatmu mengenai himpunan mahasiswa."

    "Kakak tingkatmu menceritakan semua agenda yang biasanya dilakukan oleh himpunan itu sendiri."

    "Kerangka, jabatan, dan divisi pada organisasi dan masing-masing tugas hariannya."

    "Kegiatan besar seperti festival yang berisi lomba-lomba, hingga kegiatan masing-masing divisi juga dijelaskan oleh kakak tingkatmu."

    "Himpunan organisasi ini memiliki x divisi."

    "Tiap divisi memiliki tugas dan tujuan masing-masing."

    "Setelah presentasi selesai, masuklah ke waktu wawancara dimana satu persatu mahasiswa di wawancarai oleh kakak tingkat."

    "Setelah menunggu selama beberapa menit, kini tiba giliranmu untuk diwawancara."

    "Namamu dipanggil dan dirimu berdiri dari kursi lalu berjalan menuju arah yang diarahkan oleh kakak tingkat."

    scene bg campus upper hall

    "Setelah sampai, disitu kamu duduk dan ternyata yang mewawancaraimu adalah kakak tingkat yang tadi menerimamu sewaktu datang."

    k "Ohh haloo ketemu lagi kita..."

    mc normal jacket "Halo kak..."

    k "Oh iya, sebelumnya nama saya Wisnu, dan kamu [name] kan?"

    mc "Iya kak."

    k "Baik, kalau begitu kalau boleh tahu apa yang membuatmu ingin menjadi salah satu pengurus untuk himpunan mahasiswa ini?"

    mc "Umm sebenarnya untuk mengembangkan diri sendiri kak, karena menurut saya jika mengikuti keorganisasian seperti ini
    mampu membuat diri saya berkembang secara individu karena tugas dan kewajiban yang ada."

    mc "Selain itu akan sangat berguna untuk mendapatkan pengalaman baik dari segi organisasi maupun dari akademik kak."

    k "Hmm... apakah sebelumnya sudah sering ikut berorganisasi seperti itu ?"

    menu:
        "Belum kak, sebelumnya belum pernah ikut organisasi.":
            mc "Belum kak, ini pertama kalinya saya mendaftar untuk mengikuti sebuah organisasi."

            k "Jadi pengin nambah pengalaman baru gitu ya? Kurang lebih?"

            mc "Kurang lebih begitu kak."

        "Pernah kak, dulu pernah ikut menjadi pengurus suatu organisasi.":
            mc "Pernah kak, dulu pernah ikut menjadi pengurus suatu organisasi sewaktu sekolah dulu."

            k "Ohh udah ada pengalaman ya..."

            mc "Ya kurang lebih begitu kak."

    k "Kemudian menurutmu apa kemampuan yang menjadi kelebihanmu saat ini?"

    menu:
        "Saya memiliki kemampuan untuk mengorganisir dengan baik.":

            k "Ohh jadi kamu melakukan sesuatu secara terorganisir begitu ya..."

        "Saya memiliki kemampuan untuk mendesain dan mengedit video kak.":

            k "Memiliki skill untuk multimedia kurang lebih begitu ya."

        "Saya memiliki kemampuan dan pengetahuan mengenai pemrograman web. ":

            k "Ohhh jadi sudah punya pengalaman mengenai pengodingan lah ya..."

        "Saya memiliki kemampuan untuk dapat menarik atau mengajak orang.":

            k "Punya publik speaking yang bagus begitu ya saya rasa..."

    "Mengetik jawabanmu di laptopnya [k] memberikan pertanyaan selanjutnya."

    k "Sekarang sebutkan hal yang menjadi kekuranganmu!"

    mc "Hmm kekurangan ya..."

    menu:
        "Saya merupakan orang yang pemalu...":

            k "Hmm pemalu ya.. tapi nggak kelihatan pemalu tuh hahaha..."

            mc "Ahahaha..."

        "Saya sering mengerjakan sesuatu ketika sudah mepet batas waktunya...":

            k "Wahh inii deadlinerss... kalau belum mepet males kalo udah mepet adrenalin memuncak hahaha..."

            k "Tapi tetep selesai kan kerjaannya?"

            mc "Ahaha... pasti dong kak meski mepet selesainya..."

        "Saya merupakan seorang yang boros...":

            k "Kurang bisa ngontrol gitu ya?"

            mc "Iya begitu kak.. kalau mau langsung saya beli gitu biasanya hahaha..."

        "Saya rasa saya tidak memiliki kekurangan yang signifikan...":

            k "Wohh tipe yang percaya diri ini... saya suka..."

            mc "Yang penting mantap dulu kan kan..."

    "[k] kembali mengetik hasil percakapan pada laptopnya."
    
    k "Oke.. sekarang lanjut ke pertanyaan berikutnya."

    k "Jadi apakah kamu, semisal diterima mau dan mampu melakukan tugas dengan baik dan sesuai permintaan?"

    menu:

        "Tentu saja, saya siap.":

            mc "Saya siap menerima dan melaksanakan semua tugas yang diberikan kepada saya."

        "Jika permintaannya sesuai dengan kewajiban saya, saya siap.":

            mc "Ketika tugas yang diberikan kepada saya sesuai dengan kewajiban saya, saya siap menerima dan melaksanakannya."

    k "Hmmm... baik-baik."

    "[k] kembali mengetik jawaban yang kamu berikan pada pertanyaan sebelumnya."

    k "Oke... sekarang pertanyaan terakhir."

    k "Apakah kamu bersedia bertanggung jawab atas hasil yang diberikan ketika melaksanakan suatu tugas yang diberikan?"

    mc "Ketika saya menerima suatu tugas dan kewajiban maka saya siap bertanggung jawab penuh akan hal tersebut."

    k "Baik-baik..."

    k "Terimakasih saya rasa sudah cukup..."

    mc "Terima kasih kak."

    k "Nanti akan dikabari yak di grup beberapa hari kedepan."

    mc "Ohh baik-baik... apa ini boleh langsung pulang?"

    k "Boleh-boleh sudah tidak ada acara lagi kok."
    
    mc "Kalau begitu terimakasih kak."

    k "Ya sama-sama... Hati-hati di jalan." 

    "Wawancara selesai, kamu tidak menduga akan selesai secepat itu."

    "Kamu langsung berjalan menuju tempat parkir untuk pulang."

    $ hima = True

    scene bg campus hall with fade

    "Ketika berjalan menuju tempat parkir kamu kembali bertemu dengan [j]."

    j "Udah selesai juga bro?"

    mc normal jacket "Iya ini barusan selesai."

    j "Cepet banget ya? Kirain bakal lama gitu."

    mc "Iya ga nyangka cuma ditanyain sedikit begitu."

    j "Eh ngomong-ngomong diumuminnya kapan?"

    mc "Tadi sih katanya beberapa hari kedepan, mau di umumin di grup gitu."

    j "Ohhh oke oke... langsung balik kamu ini?"

    mc "Niatnya gitu, mau apalagi?"

    j "Makan dulu lah.. masih jam segini juga."

    "[j] mengajakmu untuk makan sebelum pulang ke kosan."

    j "Gimana ikut gak?"

    mc "Ummm..."

    menu:

        "Ayo aja lah...":

            mc "Yaudah ayo, sekalian makan."

            j "Asikk ayo, ikut aku aja."

            mc "Pakai motor?"

            j "Iya, deket sih, tapi kan sekalian pulang."

            mc "Oh iya.. yaudah yuk..."

            "Kemudian kalian berdua mengambil motor masing-masing dan mengendarainya menuju tempat makan."

            scene bg black with dissolve

            "[j] mengajakmu menuju salah satu restoran yang menyediakan menu ayam geprek dan keju."

            "Kamu memesan satu menu tersebut dengan 5 cabai untuk digeprek bersama ayam sebelum ditaburi keju."

            "Kalian berdua menikmati makan siang dengan berbagai candaan sembari mengenal lebih satu sama lain."

            call eat

            $ trije_fond += 20

            "Setelah menyelesaikan makan siang kalian, kalian menyimpan nomor masing-masing sebelum pulang ke kosan masing-masing."

            "Merasa puas dengan hari ini dan karena perutmu telah terisi, kamu merasa ingin segera rebahan di tempat tidur."

            "Mengistirahatkan badanmu sekaligus mendinginkan tubuh dari suhu yang cukup panas ini."

            "Mengendarai motor masing-masing kalian pulang ke kosan masing-masing."

            #j fond++
        
        "Kayaknya ga dulu deh.":

            mc "Hmmm kayaknya gak dulu deh."

            j "Yahhh... yaudah hati-hati di jalan ya brow."

            mc "Yoii sama-sama, mungkin lain kali aja ya."

            j "Okeyy aku catet nih..."

            mc "Cabut dulu dah..."

            j "Okey-okey..."

            "Setelah itu kalian berpisah dan kamu langsung mengambil motormu untuk pulang."

            "Brummm"

            scene bg town street 3 with fade
            pause 0.5
            scene bg town street 2 with fade
            pause 0.5
            scene bg black with fade

            "Sebelum sampai ke kosan, kamu merasakan perutmu keroncongan."

            "Kamupun berhenti di warmindo yang biasa kamu kunjungi."

            "Memesan satu nasi telur dan es teh, kamu menikmati makan siangmu di warmindo dekat kos tersebut."

            call eat

            "Menghabiskan makananmu, kamu tidak langsung meninggalkan warmindo."

            "Kamu lebih memilih untuk menghabiskan waktu selama beberapa menit untuk membuka HP dan memainkan gim terlebih dahulu."

            "Setelah merasa cukup dengan gimmu, kamu merasa sudah waktunya untuk pulang."

            "Sebelum meninggalkan warmindo kamu mengambil beberapa roti untuk dimakan sewaktu-waktu."

            "Lalu setelah membayarnya kamu baru melanjutkan perjalananmu pulang."
    
    "Sesampai di kos, kamu memarkir motor dan langsung menuju kamarmu."

    "Kondisi kamar sekitar masih sama seperti tadi pagi, pintu-pintu yang ada masih tertutup rapat meskipun sekarang sudah terdengar suara dari dalam kamar."

    "Memasuki kamarmu, setelah mengganti pakaian kamu langsung merebahkan tubuhmu."

    "Menyalakan kipas angin dan mengarahkannya ke tubuhmu."

    "Kamu mengistirahatkan tubuh ditemani dengan angin sepoi-sepoi yang berhembus dari kipas angin."

    call change_timephase
    call screen mapUI with dissolve
            #call eat

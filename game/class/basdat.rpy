
default a_basdatA = 0
default a_basdatT = 0
default a_basdatC = 0
default a_basdatTS = 0
default a_basdatAS = 0
default a_basdatN = 0

label basdat_1:

    scene bg black with fade
    pause 2.0
    scene bg campus class with dissolve

    "Menempati posisi tempat duduk yang kurang lebih sama dengan ruang kelas sebelumnya."

    "Kamu mengamati kondisi ruang kelas yang ada saat ini."

    "Setelah berada pada kurang lebih 3 ruang kelas yang berbeda, kamu mendapati beberapa hal yang sama pada ruang kelas yang kamu tempati."

    "Tiap ruang kelas memiliki paling tidak 2 buah AC atau pendingin ruangan, memiliki proyektor, dan pada meja untuk pengajar terdapat sebuah komputer yang dapat digunakan."

    "Ketika mengamati ruang kelas saat ini, tiba-tiba [pa] memasuki ruang kelas."

    pa normal "Selamat pagi teman-teman!!"

    t normal "Selamat pagi [pa]!"

    pa "Kita bertemu pada pagi hari ini pada pertemuan pertama mata kuliah Basis Data."

    pa "Pertemuan kali ini saya menjelaskan mengenai pengertian basis data dan mengapa basis data penting untuk kita gunakan."

    "[pa] menyambungkan laptop dengan proyektor dan memperlihatkan apa yang ada pada layar laptopnya."

    show screen basdat_1_1 with fade

    pa "Langsung saja, apa itu basis data ? Basis data merupakan sebuah koleksi atau kumpulan data-data yang memiliki relasi yang disimpan secara sistematis dan dalam bentuk elektronik."

    pa "Basis data kita gunakan dalam berbagai bidang kehidupan. Semisal dalam sekolah, kita gunakan untuk menyimpan data administrasi yang ada di sekolah. 
    Pada perusahaan basis data digunakan untuk menyimpan semua data yang ada, dan masih banyak contoh lain."

    pa "Basis data tidak jauh dari penggunaan perangkat lunak Sistem Manajemen Basis Data, dengan perangkat lunak tersebut kita dapat lebih mudah dalam mengolah data-data yang ada."

    pa "Proses pengolahan data tersebut meliputi penambahan, pengurangan, perubahan, penyimpanan, dan pemanggilan data-data."

    hide screen basdat_1_1

    show screen basdat_1_2 with fade

    pa "Mengapa basis data itu penting dan apa manfaatnya?"

    pa "Basis data itu penting, seperti yang diterangkan sebelumnya penggunaan basis data dapat membantu kita dalam berbagai hal seperti."

    pa "Integritas Data, menggunakan manajemen basis data dapat membantu kita dalam menjaga konsistensi dari data-data dengan menerapkan aturan-aturan pada data yang ada."

    pa "Keamanan Data, menggunakan sistem manajemen basis data juga dapat meningkatkan keamanan data-data yang kita miliki. 
    Semisal dengan penggunaan hak ases untuk masing-masing tipe atau jabatan pengguna."

    pa "Lalu dengan menggunakan sistem manajemen basis data, kita dapat menganalisis data-data yang ada dengan mengelompokan sesuai keinginan kita. 
    Sehingga akan lebih mudah mendapatkan informasi dari data yang ada."

    pa "Dan tentu saja, ketika kita memiliki banyak data jutaan hingga miliaran data tidak mungkin atau akan sangat sulit ketika mengelolanya tanpa menggunakan basis data."
    
    pa "Sehingga dengan menggunakan perangkat lunak untuk basis data memungkinkan kita untuk mengelola data dalam jumlah yang banyak tersebut."

    "Pertama kali mendengarkan pengertian dan manfaat basis data kamu dan teman-temanmu dengan tanggap mencatat apa yang sekiranya perlu untuk dicatat."

    "[pa] menerangkan mata kuliah ini hingga slide terakhir yang ada pada presentasinya."

    "Kemudian kelas dilakukan dengan tanya jawab mengenai dasar basis data."

    hide screen basdat_1_2    

    scene bg campus class with fade

    pa normal "Saya rasa cukup untuk hari ini, kita bertemu lagi minggu depan untuk mata kuliah ini."

    pa "dan kalau tidak salah nanti kelas siang juga dengan saya ya?"

    "Teman-temanmu langsung mengecek jadwal untuk kelas selanjutnya."

    "Ketika temanmu yang lain sedang mengecek jadwal, Rissa mengeluarkanya suaranya."

    r normal2 "Iya pak, nanti pukul 12 ada kelas bapak untuk mata kuliah Web 1."

    pa "Oh yaa…. Kalau begitu sampai ketemu nanti siang, terimakasih…."

    r "Terimakasih pak…."

    t normal "Terimakasih….."

    "Dengan selesai pertemuan kali ini, kini saatnya mahasiswa untuk beristirahat"

    "Tanpa pikir panjang kamu mengemas barang-barangmu dan keluar dari kelas."

    call attend_basdat
    call attend_class

    call istirahat

    jump web_1

label basdat_2:

    "Basdat 2"

    call istirahat

    jump web_2

label basdat_3:

    "Basdat 3"

    call istirahat

    jump web_3

label basdat_4:

    "Basdat 4"

    call istirahat

    jump web_4

label attend_basdat:

    $ a_basdatA +=1
    $ a_basdatN +=8

    return
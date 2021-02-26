### GENERAL TEST

1. Apakah anda familiar dengan JWT (Jason Web Token? Jelaskan.
2. Pertimbangan-pertimbangan apa yang Anda ambil dari sisi UI, Keamanan, Kinerja, SEO,
  Maintainability maupun Teknologi saat Anda membangun aplikasi web atau situs ?
3. Apakah anda terbiasa menggunakan sprint development methodology ? jika sudah tools
  apa yang anda gunakan dan bagaimana cara kerja anda agar on time delivery serta
  performance 100% tiket selesai ?
4. Kesulitan-kesulitan apa saja yang pernah anda hadapi pada saat membuat API dan
  bagaimana cara anda mengatasinya ?
5. Apakah anda pernah menggunakan Python sebelumnya? Jika iya apakah anda familiar
  dengan Context Manager? Jelaskan.
6. Apakah anda pernah menggunakan Docker? Jika pernah jelaskan cara anda membuat
  container

###### Jawaban:

1.  JWT ini adalah sebuah token berbentuk string panjang yang sangat random yang gunanya sendiri untuk melakukan sistem autentikasi dan pertukaran informasi. Umumnya  JWT atau Token ini seperti password jadi ketika users berhasil melakukan login maka server akan memberikan sebuah Token. Nanti Token tersebut akan disimpan oleh users pada Local Storage atau Cookies Browser dan bila users ingin mengakses halaman halaman tertentu maka harus menyertakan token tersebut. Untuk itu users akan mengirim balik token yang dikasih diawal tadi sebagai bukti bila user ini, sudah melakukan login. 

  Sekarang kita akan lihat struktur dasarnya Tokennya dimana terdiri dari tiga bagian yaitu yang pertama header lalu kedua bagian payloadnya atau datanya dan yang ketiga adalah bagian verify signature.

  \- **Header** berisi informasi tentang algoritma dan jenis token yang digunakan, seperti contoh dibawah

  ```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
  ```

  Bagian ini hanyalah string yang di-encode menggunakan base64. Jadi kita bisa mendapatkan nilai asli dari teks tersebut dengan men-decodenya.

  \- **Payload** berisi data yang ingin dikirim melalui token.

  ```
  eyJuYW1hIjoiRmFxaWgifQ
  ```

  Dalam penerapannya di otentikasi atau pun otorisasi, biasanya data ini berupa data yang sifatnya unik bagi user, seperti: email, id/uuid, dan juga data yang berkaitan dengan otorisasi seperti role, karena data tersebut akan digunakan sebagai tanda pengenal si pengirim token.

  Jangan pernha menyelipkan data yang sifatnya konfidental atau sensitif ke dalam JWT (seperti password). Karena dapat dengan mudah men-decodenya.

  \- **Verify Signature** adalah hash gabungan dari header, payload dan sebuah secret key (berupa string random panjang biasanya), seperti contoh di bawah:

  ```
  jtYrULLMxWPWfy39r4Qm0gCxo-5–542VhsRDSO5cjQ
  ```

  Algoritma hash yang digunakan mengikuti dari apa yang sudah ditentukan di dalam header. Contoh hashcode

  ```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1hIjoiRmFxaWgifQ.jtYrULLMxWPWfy39r4Qm0gCxo-5–542VhsRDSO5cjQ
  ```

  Signature ini berguna untuk memverifikasi bahwa header maupun payload yang ada dalam token tidak berubah dari nilai aslinya. Signature-nya sendiri tidak mungkin dapat diakali, karena sudah dalam berbentuk hash,  yang mana adalah fungsi satu arah (tidak dapat dikembalikan ke nilai semula), dan meski kita tahu algoritma hashing-nya, kita juga memerlukan secret key yang mana hanya si pembuat aplikasi yang tahu.

  Token juga memiliki masa expired biasanya 30 hari atau 1 minggu (dapat diatur), tetapi dalam hal ini membuat aplikasi menjadi tidak dinamis pada saat user logout, token yang digunakan dapat di revoke (di buat expired secara paksa dengan cara dimasukkan ke database dll). Pada saat user tersebut login maka token baru akan tergenerate kembali.

2. **UI**

   Memiliki UI yang terintegrasi dan harmonis atau UX dalam aplikasi seluler membantu bisnis untuk menarik lebih banyak pengguna tetapi juga meningkatkan kepuasan pelanggan. Disini juga dapat menguatkan branding kita kepada user agar produk kita semakin dikenal secara meluas. Meningkatkan traffic pelanggan.

   **Keamanan**

   Pengembangan Web memperhitungkan banyak pertimbangan keamanan, seperti kesalahan entri data pengecekan melalui bentuk-bentuk, output filtering, dan enkripsi. Script dapat dimanfaatkan untuk memberikan akses tidak sah ke pengguna yang jahat mencoba untuk mengumpulkan informasi seperti alamat email, password dan konten yang dilindungi seperti nomor kartu kredit.

   **Kinerja**, beberapa peningkatan kinerja umum dalam pengembangan web meliputi:

   - Sederhanakan pemilih CSS untuk meminimalkan penghitungan ulang dan biaya tata letak.
   - Minimalkan manipulasi DOM dan hapus elemen yang tidak perlu.
   - Hindari pengikatan data ketika jumlah elemen DOM mencapai ratusan.
   - Bersihkan penangan acara dalam melihat kejadian yang tidak lagi diperlukan.
   - Cobalah untuk menghasilkan sebagian besar HTML di sisi server. Setelah di klien, buat tampilan backing dengan elemen DOM yang ada.
   - Memiliki server khusus wilayah untuk lebih cepat berputar.
   - Gunakan CDN untuk melayani pustaka dan aset statis.

   **SEO**

   - Gunakan permalink sederhana
   - Buat judul konten yang menarik
   - Letakkan focus keyword pada 100 kata petama
   - Sisipkan outbound Link
   - Maksimalkan Internal Link
   - Tingkatkan kecepatan website

   **Maintainability** 

   - Membuat web menjadi modular, dimana membagi repositori sendiri-sendiri jadi jika ada kesalahan atau menambah fitur tidak mempengaruhi repositori lain

   **Teknologi**

   - Menggunakan teknologi yang up-to-date dan mengikuti perkembangan jaman

3. Saya belum ada pengalaman menggunakan sprint development methodology, tetapi saya pernah mendapat definisi mengenai sprint yang hampir sama istilahnya dengan Scrum Agile Metodhology. Scrum banyak digunakan untuk pengembangan produk software apapun yang bersifat kompleks. Proses pengembangan dilakukan secara berulang, aturan dan solusi disepakati dan dilakukan dengan kolaborasi tiap tim secara terorganisir dan terstruktur. 

   Scrum berjalan pada sebuah batasan waktu (*timebox*) yang disebut sprint, untuk pengembangan produk yang akan digunakan oleh pengguna atau dimasukkan ke lingkungan produksi dengan berdurasi tidak lebih dari 30 hari. Karena durasi Sprint lebih singkat dibandingkan durasi pengembangan produk, maka dalam daur hidup pengembangan produk akan ada beberapa Sprint. Artinya pengembangan produk menggunakan Scrum dilakukan secara berualng dan inkremental.

   Sprint diawali dengan Sprint Planning dimana Product Owner, satu orang yang telah diberikan wewenang  untuk memaksimalkan nilai dari produk di pasar, bertemu dengan Development Team, berkolaborasi untuk memprakirakan Product Backlog item mana saja yang akan dikerjakan selama satu Sprint. Sprint 

   Setelah Sprint Planning berakhir, Development Team akan swakelola (*self-organise*) tanpa interfensi dari pihak manapun untuk mengambil Sprint Backlog untuk diri mereka masing-masing dan mengerjakannya. **Setiap hari hingga akhir Sprint Development Team akan melakukan Daily Scrum tidak lebih dari 15 menit untuk menentukan apa yang mereka akan kerjakan selama 24 jam ke depan berdasarkan perkembangan 24 jam terakhir serta memaparkan permasalahan yang menghambat mereka untuk bisa mencapai Sprint Goal dan memenuhi Definition of Done.** 

   Di akhir Sprint, Product Owner akan mempresentasikan hasil pekerjaan Development Team selama satu Sprint kepada para pemegang kepentingan guna mendapatkan umpan balik di acara bernama Sprint Review. Product Owner juga menjelaskan apakah dalam Sprint tersebut pencapaian Development Team menuju Sprint Goal kepada seluruh pemegang kepentingan. Hanya Product Owner yang menentukan kapan produk tersebut dimasukkan ke lingkungan produksi. Untuk Sprint berdurasi 30 hari, batasan waktu Sprint Review tidak lebih dari 4 jam.

   Setelah Sprint Review, Development Team, Product Owner akan berkolaborasi untuk menentukan *improvement* apa yang mereka akan implementasikan di Sprint berikutnya di acara bernama Sprint Retrospectives. Setidaknya satu *improvement* yang disepakati di Sprint Retrospectives akan masuk ke dalam Sprint Backlog di Sprint berikutnya. *Definition of Done* adalah salah satu hal yang ditekankan oleh Development Team pada saat Sprint Retrospectives. Sprint Retrospectives adalah acara yang *paling penting* dalam Scrum karena sifatnya yang menekankan *continuous learning* yang dapat meningkatkan tingkat agility perusahaan. Untuk Sprint berdurasi 30 hari, batasan waktu Sprint Review tidak lebih dari 3 jam.

   Sprint berikutnya langsung dilakukan setelah Sprint Retrospectives berakhir tanpa ada jeda antar Sprint. Pengembangan produk menggunakan Scrum akan berakhir ketika:

   - Anggaran pengembangan produk sudah habis atau;
   - Pengguna sudah tidak mau menggunakan produk yang bersangkutan atau;
   - *Return on Investment* (ROI) dari produk sudah maksimal atau tercapai;

   Setiap Sprint, Product Owner akan memastikan agar nilai dari produk setinggi mungkin pengembangan produk diakhiri. Product Owner, Scrum Master dan Development Team memegang nilai-nilai: komitmen, keberanian, saling menghargai, keterbukaan dan fokus.

   Cara kerja agar on time delivery serta performance 100% :

   ###### Buat list pekerjaan yang akan, sudah dan belum terselesaikan

   Membuat daftar kerja terlebih dulu sebelum memulai suatu pekerjaan, apa yang akan dilakukan dan menentukan setiap prioritas pekerjaan.

   ###### Komunikasi jika ada kendala

   Di dalam perkejaan kita tidak mungkin bekerja sendiri dan pasti memiliki team, jangan sampai hasil yang dicapai keseluruhan team menjadi tidak sesuai target karena ada kendala yang tidak kita komunikasikan dengna baik.

   ###### Aktif bertanya

   Saat bekerja, jangan sampai menjadi pasif, tetap turut aktif apakah itu tentang pekerjaan atau diluar pekerjaan (sosial), jika kita terus aktif hal tersebut karena akan menjadi dampak positif bagi diri kita sendiri

   

4. Masih kesulitan apabila mengintegrasikannya dengan JWT dan dulu pernah membuat CRUD API dengan menggunakan JPA di SpringBoot Java dan agak kesulitan jika menambah fitur baru. Kalau JWT saya belum menemukan best practice yang baik diterapkan (masih mencari) dan untuk CRUD API saya mengubah menggunakan native SQL jadi saat menambah fitur baru menjadi lebih fleksibel

5. Saya pernah menggunakan Python sebelumnya, untuk Context Manager sendiri saya belum familiar tetapi berdasarkan hasil eksplor saya, Context Manager digunakan untuk menghandle penggunaan resources seperti koneksi ke database, memastikan untuk menghentikan proses penggunaan resources setelah digunakan, agar resources tidak bocor/menjadi lambat bahkan crash. 

   Saat menggunakan Context Manager menggunakan class, user harus memastikan bahwa didalam class terdapat method *__enter__()* and *__exit__()*.  __enter__()  mengembalikan resources yang akan dipakai sementara  __exit__() tidak mengambalikan nilai apapun tetapi melakukan cleanup atau close(). Contoh penggunaan context manager dalam database context management

   ```python
   from pymongo import MongoClient 
   
   class MongoDBConnectionManager(): 
   	def __init__(self, hostname, port): 
   		self.hostname = hostname 
   		self.port = port 
   		self.connection = None
   
   	def __enter__(self): 
   		self.connection = MongoClient(self.hostname, self.port) 
   		return self
   
   	def __exit__(self, exc_type, exc_value, exc_traceback): 
   		self.connection.close() 
   
   with MongoDBConnectionManager('localhost', '27017') as mongo: 
   	collection = mongo.connection.SampleDb.test 
   	data = collection.find({'_id': 1}) 
   	print(data.get('name')) 
   
   ```


****

   Dengan mengeksekusi fungsi `with`:

   - Object *MongoDBConnectionManager* terbuat dengan *localhost* sebagai hostname dan *27017* sebagai port dimana method init terkesekusi

   - Method enter membuka mongodb connection mengembalikan *MongoDBConnectionManager* object ke dalam variabel.

   - Lalu mencari collection di SampleDb databasedengan *_id*=1. Field nama di print.
   - Method exit memanage untuk closing connection

6. Iya saya pernah menggunakan docker. Jika ingin mengintegrasikan applikasi dengan docker pertama tambahkan depedency docker pada project anda (ini fleksibel sesuai bahasa dan IDE yang digunakan), selanjutkan buat Docker File

   ```java
   FROM adoptopenjdk/openjdk11:alpine-slim
   
   ENV DATA_DIR=/inventory-api
   ENV DB_HOST=host.docker.internal
   
   RUN addgroup -S spring && adduser -S spring -G spring
   RUN mkdir -p $DATA_DIR
   RUN chown spring $DATA_DIR
   
   USER spring:spring
   ARG JAR_FILE=./target/inventory-api-0.0.1-SNAPSHOT.jar
   COPY ${JAR_FILE} app.jar
   ENTRYPOINT ["java","-jar","/app.jar"]
   ```

Contoh diatas merupakan contoh Docker File pada project saya sebelumnya menggunakan SpringBootJava

Lalu buka terminal dan Docker Dekstop, install image yang sekiranya akan digunakan dalam docker anda (seperti mySQL, SonarQube, JDK etc), untuk install image gunakan command berikut di terminal

```
docker pull mcr.microsoft.com/windows/servercore/iis //contoh
```

Untuk membuat image aplikasi kita gunakan

```powershell
docker build -t container1 .\Container1 //contoh
```

Untuk deploynya

```
docker container run --detach --publish 8081:80 
--name web2  <YourDockerID>/firstimage
```

jika dingin menggabungkan 2 image gunakan docker compose 
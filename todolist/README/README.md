 # Tugas 5 PBP
 - Nama   : Rizka Nisrina Nabila
 - NPM    : 2106653344
 - Kelas  : PBP - B
 
 # Link: https://tugas2rizka.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

## Inline CSS
Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. 

**Kelebihan**:
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
- Sangat membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen. 

**Kekurangan**
Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

## Internal CSS
Internal CSS merupakan kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. 

**Kelebihan**:
- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
- Class dan ID bisa digunakan oleh internal stylesheet. 

**Kekurangan**
- Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
- Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

## Eksternal CSS
Eksternal CSS merupakan kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. Kelebihan:

**Kelebihan**:
- Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
- Loading website menjadi lebih cepat
- File CSS dapat digunakan di beberapa halaman website sekaligus.

**Kekurangan**
- Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

## Jelaskan tag HTML5 yang kamu ketahui.
1. <button> : Creates a clickable button.
2. <div> : Specifies a division or a section in a document.
3. <form> : Defines an HTML form for user input.
4. <span> : Defines an inline styleless section in a document.
5. <video> : Embeds video content in an HTML document.
6. <section> : Defines a section of a document, such as header, footer etc.
7. <nav> : Defines a section of navigation links.
8. <header> : Represents the header of a document or a section.
9. <footer> : Represents the footer of a document or a section.
10. <embed> : Embeds external application, typically multimedia content like audio or video into an HTML document.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Tag selector -- menggunakan tag HTML sebagai selectornya
- ID Selector -- menggunakan atribut “id” pada element HTML sebagai selectornya. Kemudian mengimplementasikannya dengan tanda pagar(#)
- Class Selector -- cara menggunakannya hampir sama dengan ID selector, namun pada class selector tentunya menggunakan atribut class pada element HTML yang akan dipilih. Diimplementasikan dengan tanda titik (.)
- Universal Selector -- hanya ada 1 di dalam CSS, yaitu tanda bintang “*”. Selector ini bertujuan untuk ‘mencari’ semua tag yang ada.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pertama, kita mendefinisikan link src bootstrap ke dalam tag <head>
2. Kustomisasi template untuk halaman login, register, dan create-task semenarik mungkin.
3. Lalu, membuat struktur HTML dengan menggunakan class dan menyesuaikan bootstrap sesuai kebutuhan, untuk membuat cards pada todolist menggunakan class="card"
4. Selanjutnya, mengubah style dari tampilan bootstrap dengan menambahkan Internal CSS ke dalam tag <style>
5. Terakhir, men-Deploy aplikasi ke Heroku
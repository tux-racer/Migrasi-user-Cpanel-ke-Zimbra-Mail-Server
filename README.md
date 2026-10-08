Mumpung inget dan setelah setelesai ada pekerjaan migrasi user cpanel ke zimbra
 Zimbra sudah berjalan normal dan domain sudah di buat di zimbra,
masuk ke cpanel buka file manager ambill file /home/usercpanel/etc/domain.com/shadow
upload file shadow ke mesin zimbra, misal di /srv

gunakan file convert.py

buka file  convert.py sesuiakan dengan kebutuhan

# Konfigurasi Domain
DOMAIN = "domain.com"
INPUT_SHADOW_FILE = "/srv/shadow"  # Sesuaikan path jika file berada di direktori lain
OUTPUT_ZMP_FILE = "create-account-zimbra.zmp"
 

jalan convert 

[root@mail srv]# python3 convert.py
Berhasil! File provisi Zimbra telah dibuat: create-account-zimbra.zmp


pastikan jumlah user sama di cpanel dan isi file shadow di sini sudah sama 168 user


membuat user zimbra dari file create-account-zimbra.zmp
[root@mail srv]# su - zimbra -c "zmprov -f /srv/create-account-zimbra.zmp"
prov> 15b572a8-bc40-4ce7-8b07-d3a591361b05
....
....


 setelah di tambahkan user dari create-account-zimbra.zmp di zimbra akan menambah sebanyak 168 user dan 1 user admin total ada 168

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

<img width="1590" height="321" alt="Screenshot at 2026-10-08 14-20-25" src="https://github.com/user-attachments/assets/7f570160-aa08-412a-8899-a350f07a799a" />

<img width="1137" height="628" alt="Screenshot at 2026-10-08 14-26-41" src="https://github.com/user-attachments/assets/b0780488-5e58-4d73-b415-fb42a8e09e2f" />

membuat user zimbra dari file create-account-zimbra.zmp

[root@mail srv]# su - zimbra -c "zmprov -f /srv/create-account-zimbra.zmp"

prov> 15b572a8-bc40-4ce7-8b07-d3a591361b05
....

<img width="946" height="494" alt="Screenshot at 2026-10-08 14-33-18" src="https://github.com/user-attachments/assets/35f9167e-adf6-4e36-ae7c-03a2c185973b" />

 setelah di tambahkan user dari create-account-zimbra.zmp di zimbra akan menambah sebanyak 168 user dan 1 user admin total ada 169

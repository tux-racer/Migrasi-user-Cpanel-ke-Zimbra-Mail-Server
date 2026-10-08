#!/usr/bin/env python3

# Konfigurasi Domain
DOMAIN = "domain.com"
INPUT_SHADOW_FILE = "/srv/shadow"  # Sesuaikan path jika file berada di direktori lain
OUTPUT_ZMP_FILE = "create-account-zimbra.zmp"

def convert_shadow_to_zimbra(input_file, output_file, domain):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            # Abaikan baris kosong atau komentar
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(':')
            if len(parts) >= 2:
                username = parts[0]
                password_hash = parts[1]
                
                # Abaikan akun jika password tidak valid/dikunci (* atau !)
                if password_hash in ['*', '!', '!!', '']:
                    continue
                
                email = f"{username}@{domain}"
                
                # Format perintah Zimbra CLI (zmprov)
                # Menggunakan {crypt} di depan hash agar Zimbra membaca hash cPanel secara langsung
                zm_command = f"createAccount {email} '' userPassword '{{crypt}}{password_hash}'\n"
                f_out.write(zm_command)

    print(f"Berhasil! File provisi Zimbra telah dibuat: {output_file}")

if __name__ == "__main__":
    convert_shadow_to_zimbra(INPUT_SHADOW_FILE, OUTPUT_ZMP_FILE, DOMAIN)

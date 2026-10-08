#!/bin/bash

# --- Konfigurasi ---
DOMAIN="domain.com"
SHADOW_FILE="/srv/shadow"
OUTPUT_FILE="create-account-zimbra.zmp"

# Reset / buat file output baru
> "$OUTPUT_FILE"

# Pastikan file shadow ada
if [ ! -f "$SHADOW_FILE" ]; then
    echo "Error: File $SHADOW_FILE tidak ditemukan!"
    exit 1
fi

# Membaca baris demi baris dari file shadow
while IFS=':' read -r user pass_hash rest; do
    # Abaikan komentar, baris kosong, atau akun tanpa hash valid (*, !, !!)
    if [[ -z "$user" || "$user" =~ ^# ]] || [[ "$pass_hash" =~ ^(\*|\!|\!\!|)$ ]]; then
        continue
    fi

    # Tulis perintah zmprov ke file output
    echo "createAccount ${user}@${DOMAIN} '' userPassword '{crypt}${pass_hash}'" >> "$OUTPUT_FILE"

done < "$SHADOW_FILE"

echo "Selesai! File $OUTPUT_FILE berhasil dibuat."

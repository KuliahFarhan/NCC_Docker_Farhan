# Webhook Logger Service

## Identitas Penugasan

- Nama: Muhammad Farhan
- NRP: 5054241018
- Topik: Laporan Docker (NCC Oprec)
- Service: Webhook Logger Service

## Ringkasan

Repository ini berisi implementasi service berbasis Flask yang dijalankan menggunakan Docker.

Fokus utama penugasan:
- Build image Docker dari aplikasi Python
- Menjalankan container dan verifikasi endpoint
- Menyusun bukti proses pengerjaan dan deployment
- Mendokumentasikan hasil pada laporan Docker

## Struktur Proyek

```text
Oprec_2026_Pertemuan_1-main/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LAPORAN_DOCKER.md
├── log.txt
├── deployment-log.txt
├── img/
└── latihan-dockerfile/
```

## Endpoint Service

Aplikasi menyediakan endpoint berikut:

- `GET /` -> menampilkan pesan sederhana
- `GET /health` -> mengembalikan status service

Contoh respons `/health`:

```json
{"status": "ok"}
```

## Menjalankan Secara Lokal

### 1. Build image

```bash
docker build -t flask-health .
```

### 2. Run container

```bash
docker run -d --name flask-health -p 8003:8000 flask-health
```

### 3. Uji endpoint

```bash
curl http://localhost:8003/health
```

### 4. Cek log container

```bash
docker logs flask-health
```

## Menjalankan dengan Docker Compose

```bash
docker compose up -d
```

Akses service di:
- `http://localhost:8003/`
- `http://localhost:8003/health`

Hentikan service:

```bash
docker compose down
```

## Ruang Lingkup Penugasan

Ruang lingkup yang dipertahankan dari dokumentasi sebelumnya meliputi:
- Pengenalan konsep Docker image dan container
- Implementasi proses build, run, dan verifikasi service
- Publikasi serta deployment service
- Dokumentasi bukti pengerjaan (perintah, output, dan tangkapan layar)

Dokumentasi lengkap pengerjaan tersedia pada:
- `LAPORAN_DOCKER.md`

## Pengingat Penting

- File `log.txt` tersedia dan menjadi bagian bukti praktik command Docker.
- File `deployment-log.txt` berisi transcript sesi deployment.
- Simpan konsistensi port antara aplikasi (`8000`) dan host (`8003`) saat menjalankan container.

## Referensi Singkat

- Docker Docs: https://docs.docker.com/
- Flask Docs: https://flask.palletsprojects.com/

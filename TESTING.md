# Panduan Pengujian `gpt4-interface`

## 1. Instalasi Dependensi

```bash
pip install -r requirements.txt
```

## 2. Contoh Pengujian Manual

Buat file `test_gpt4.py`:

```python
from gpt4_interface import GPT4Interface

api_key = "sk-..."  # Ganti dengan API key OpenAI Anda
gpt = GPT4Interface(api_key)

try:
    result = gpt.ask("Apa itu AgentGPT?")
    print("Hasil:", result)
except Exception as e:
    print("Error:", e)
```

## 3. Pengujian Otomatis (Opsional)

Bisa menggunakan `pytest` untuk pengujian otomatis:

```bash
pip install pytest
pytest
```

## 4. Catatan
- Jangan commit API key ke repository!
- Pastikan koneksi internet aktif saat testing. 
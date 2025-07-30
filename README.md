# 🏛️ Akıllı Turizm Rehberi

Türkiye özelinde geliştirilmiş, LLAMA 3.2 3B modeli ile çalışan akıllı turizm rehberi uygulaması. Kullanıcılar yazılı olarak soru sorabilir ve gerçek zamanlı, doğal yanıtlar alabilir.

## 📋 Özellikler

- 🏺 Tarihi Yerler: Türkiye'nin tarihi mekanları hakkında detaylı bilgi
- 🎭 Kültürel Etkinlikler: Yerel festivaller ve kültürel aktiviteler
- 🍽️ Yöresel Yemekler: Şehirlere özel lezzetler ve tarifler
- 🚌 Ulaşım Bilgileri: Şehirler arası ve şehir içi ulaşım rehberi
- 💬 Gerçek Zamanlı Sohbet: Doğal dil işleme ile akıcı konuşma
- 🧠 Konuşma Hafızası: Önceki mesajları hatırlayan akıllı sistem

## 🛠️ Gereksinimler

### Sistem Gereksinimleri

- Python 3.8+
- En az 4GB RAM
- 2GB boş disk alanı (model için)

### Python Kütüphaneleri

```python
pip install langchain-ollama langchain
```

## ⚙️ Kurulum

#### 1. Ollama Kurulumu

##### Windows

Ollama İndirme Sayfası'na gidin
Windows installer dosyasını indirin
İndirilen .exe dosyasını çalıştırın
Kurulum talimatlarını takip edin

##### macOS

```bash
# Homebrew ile kurulum
brew install ollama

# Veya doğrudan indirme
curl -fsSL https://ollama.com/install.sh | sh
```

##### Linux (Ubuntu/Debian)

```bash
# Resmi kurulum scripti
curl -fsSL https://ollama.com/install.sh | sh

# Manuel kurulum
sudo apt update
sudo apt install ollama
```

#### 2. LLAMA 3.2 Modelini İndirme
Ollama kurulduktan sonra terminal/komut istemcisinde:

```bash
# LLAMA 3.2 3B modelini indirin (yaklaşık 2GB)
ollama pull llama3.2:3b

# Modeli test edin
ollama run llama3.2:3b
```

#### 3. Python Ortamı Kurulumu

```bash
# Sanal ortam oluşturma (önerilen)
python -m venv ollama-tourism-guide
source ollama-tourism-guide/bin/activate  # Linux/macOS
# turizm_rehberi\Scripts\activate    # Windows

# Gerekli kütüphaneleri yükleme
pip install langchain-ollama langchain
```

#### Proje Dosyası Oluşturma

```bash
touch terminal_tourist_bot.py
```

## 🚀 Çalıştırma

#### Ollama Servisini Başlatma

```bash
# Ollama servisini başlatın (arka planda çalışır)
ollama serve
```

#### Uygulamayı Çalıştırma

```bash
python terminal_tourist_bot.py
```


## 📝 Kullanım

Uygulama başladığında terminal üzerinden soru sorabilirsiniz:

```bash
Akıllı Turizm Rehberine Hoş Geldiniz
Size gezilecek yerler, tatil önerileri ve ulaşım bilgileri gibi konularda yardımcı olabilirim.

Siz: İstanbul'da gezilecek yerler neler?
Rehber AI: İstanbul'da mutlaka görmeniz gereken yerler...

Siz: Kapadokya'ya nasıl gidebilirim?
Rehber AI: Kapadokya'ya ulaşım seçenekleri...

Siz: çık
Program sonlandırıldı
```

## 🔧 Yapılandırma

#### Model Parametreleri

`turizm_rehberi.py` dosyasında model ayarlarını değiştirebilirsiniz:

```python
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.8,    # Yaratıcılık seviyesi (0.0-1.0)
    num_predict=256     # Maksimum yanıt uzunluğu
)
```

#### Sistem Mesajını Özelleştirme

```python
SystemMessage(content = "Sen bir akıllı turizm rehberisin..."
    # Buraya özel talimatlar ekleyebilirsiniz
)
```

## 🔄 Gelecek Geliştirmeler

 - Streamlit web arayüzü eklenmesi
 - Görsel destekli yanıtlar
 - Konum bazlı öneriler
 - Çoklu dil desteği
 - Rezervasyon entegrasyonu

## 📚 Ek Kaynaklar

- (Ollama Dokümantasyonu)[https://ollama.com/docs]
- (LangChain Rehberi)[https://python.langchain.com/docs/get_started/introduction]
- (LLAMA Model Detayları)[https://ollama.com/library/llama3.2]


## 📄 Lisans

Bu proje açık kaynak kodlu olarak geliştirilmiştir.


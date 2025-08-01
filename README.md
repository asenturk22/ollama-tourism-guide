# 🏛️ Akıllı Turizm Rehberi

Türkiye özelinde geliştirilmiş, LLAMA 3.2 3B modeli ile çalışan akıllı turizm rehberi uygulaması.  **İki farklı versiyonu** bulunmaktadır: Terminal tabanlı ve Web tabanlı (Streamlit).  Kullanıcılar yazılı olarak soru sorabilir ve gerçek zamanlı, doğal yanıtlar alabilir.

## 🚀 Versiyon Seçenekleri

### 🖥️ Terminal Versiyonu (terminal_tourist_bot.py)

- Basit ve hızlı terminal arayüzü
- Doğrudan komut satırı kullanımı
- Minimal kaynak kullanımı
- Geliştiriciler için ideal

### 🌐 Web Versiyonu (streamlit_tourist_bot.py)

- Modern web arayüzü (Streamlit)
- Görsel tasarım ve kullanıcı dostu arayüz
- Model seçimi ve ayar seçenekleri
- Son kullanıcılar için ideal

### ⚡ Streaming Web Versiyonu(streamlit_tourism_bot_streaming.py)

- **Canlı metin akışı** - Yanıtlar kelime kelime görünür
- **Real-time deneyim** - ChatGPT benzeri etkileşim
- **Gelişmiş UX** - Daha dinamik ve etkileyici
- **Custom streaming handler** - Streamlit için optimize edilmiş


## 📋 Ortak Özellikler

- 🏺 **Tarihi Yerler**: Türkiye'nin tarihi mekanları hakkında detaylı bilgi
- 🎭 **Kültürel Etkinlikler**: Yerel festivaller ve kültürel aktiviteler
- 🍽️ **Yöresel Yemekler**: Şehirlere özel lezzetler ve tarifler
- 🚌 **Ulaşım Bilgileri**: Şehirler arası ve şehir içi ulaşım rehberi
- 💬 **Gerçek Zamanlı Sohbet**: Doğal dil işleme ile akıcı konuşma
- 🧠 **Konuşma Hafızası**: Önceki mesajları hatırlayan akıllı sistem

## ✨ Web Versiyonu Ek Özellikleri

### 🌐 Standart Web Versiyonu

- 🎨 **Modern Arayüz**: Streamlit ile responsive tasarım
- ⚙️ **Model Seçimi**: llama3.2:3b, llama3.2:1b, llama3.1:8b seçenekleri
- 🎚️ **Üretkenlik Kontrolü**: Temperature ayarı (0.0-1.0)
- 🗑️ **Sohbet Yönetimi**: Geçmişi temizleme butonu
- 🔧 **Hata Yönetimi**: Gelişmiş hata yakalama sistemi
- 💾 **Session Yönetimi**: Web tabanlı hafıza sistemi

### ⚡ Streaming Web Versiyonu :

- 🔥 **Canlı Metin Akışı**: Yanıtlar kelime kelime real-time görünür
- 💬 **ChatGPT Benzeri UX**: Modern sohbet deneyimi
- ⚡ **Dinamik Etkileşim**: Anında geri bildirim
- 🎭 **Custom Stream Handler**: Streamlit için özel geliştirilmiş
- 🚀 **Gelişmiş Performans**: Daha hızlı ve etkileyici yanıtlar

## 🛠️ Gereksinimler

### Sistem Gereksinimleri

- Python 3.8+
- En az 4GB RAM
- 2GB boş disk alanı (model için)
- Ollama servisi

### Python Kütüphaneleri

```python
# terminal versiyonu icin
pip install langchain-ollama langchain

# web versiyonu icin
pip install streamlit langchain-ollama langchain
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

# Ek modeller (web versiyonu için)
ollama pull llama3.2:1b
ollama pull llama3.1:8b

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

# Web versiyonu için (ek # Terminal versiyonu
touch terminal_tourist_bot.py

# Web versiyonu  
touch streamlit_tourist_bot.py

# Web versiyonu (streaming)
touch streamlit_tourism_bot_streaming.py
```

#### Proje Dosyası Oluşturma

```bash
# Terminal versiyonu
touch terminal_tourist_bot.py

# Web versiyonu  
touch streamlit_tourist_bot.py
```

## 🚀 Çalıştırma

#### Ollama Servisini Başlatma

```bash
# Ollama servisini başlatın (arka planda çalışır)
ollama serve
```

#### Uygulamayı Çalıştırma

```bash
# terminal versiyonu calistirmak icin
python terminal_tourist_bot.py

# web versiyonunu calistirmak icin
streamlit run streamlit_tourist_bot.py

# web versiyonu(streaming) calistirmak icin
streamlit run streamlit_tourism_bot_streaming.py
```

Web versiyonu varsayılan olarak [http://localhost:8501](http://localhost:8501) adresinde açılacaktır.


## 📝 Kullanım

### 🖥️ Terminal Versiyonu Kullanımı

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

### 🌐 Web Versiyonu Kullanımı

- Açma: http://localhost:8501
- Model Seçimi: Sidebar'dan istediğiniz modeli seçin
- Ayarlar: Üretkenlik seviyesini ayarlayın
- Soru Sorma: Alt kısımdaki chat input'a sorunuzu yazın
- Sohbet Yönetimi: Gerekirse sohbet geçmişini temizleyin

## 🔧 Yapılandırma

#### Model Parametreleri

`turizm_rehberi.py` dosyasında model ayarlarını değiştirebilirsiniz:

```python
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.8,    # Üretkenlik seviyesi (0.0-1.0)
    num_predict=256     # Maksimum yanıt uzunluğu
)
```

#### Sistem Mesajını Özelleştirme

```python
SystemMessage(content = "Sen bir akıllı turizm rehberisin..."
    # Buraya özel talimatlar ekleyebilirsiniz
)
```

## Tamamlanan Geliştirmeler

 - **Terminal Versiyonu**: Basit komut satırı arayüzü
 - **Statik Web Arayüzü**: Streamlit ile modern tasarım
 - **Streaming Web Arayüzü**: Real-time metin akışı 🆕
 - **Model Seçimi**: Farklı LLAMA model versiyonları
 - **Sohbet Hafızası**: Konuşma geçmişi takibi
 - **Hata Yönetimi**: Gelişmiş hata yakalama
 - **Custom Streaming**: Streamlit için özel callback handler 🆕

## 📚 Ek Kaynaklar

- [Ollama Dokümantasyonu](https://ollama.com/docs)
- [LangChain Rehberi](https://python.langchain.com/docs/get_started/introduction)
- [LLAMA Model Detayları](https://ollama.com/library/llama3.2)


## 📄 Lisans

Bu proje açık kaynak kodlu olarak geliştirilmiştir.




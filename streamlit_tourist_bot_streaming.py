import streamlit as st #streamlit ile web arayuzu olusturma kutuphanesi
from langchain_ollama import ChatOllama # ollama llm arayuzu
from langchain.schema import SystemMessage, HumanMessage # chat mesaj siniflari
from langchain.memory import ConversationBufferMemory # konusma gecmisi icin basit bir hafiza
import time

# streaming callbacks
# terminala yazmak
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler # streamlit ile calismak icin ozel handler
from typing import Any

# streamlit icin ozel streaming callback tanimi 
class StreamHandler(BaseCallbackHandler):
  def __init__(self, placeholder):
    self.placeholder = placeholder  # streamlit icindeki mesaj kutumuz
    self.final_text = ""

  def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
    self.final_text += token  # tokenlari birlestir.
    self.placeholder.markdown(self.final_text + " ") # canli olarak yaz


def initialize_llma(model_name, temp, stream_handler, streaming=True):
  try: 
    return ChatOllama(
      model=model_name, 
      temperature=temp,
      streaming=streaming, 
      callbacks=[stream_handler] if stream_handler else []
    )
  except Exception as e:
    st.error(f"Model yuklenirken hata oluştu : {str(e)}")
    st.error("Lütfen Ollama'nın çalıştığından ve modelin yüklü olduğundan emin olun.")
    return None



# Sayfa konfigurasyon ayarlari
st.set_page_config(
  page_title = "Akıllı Turist Rehberi (Canlı)", 
  page_icon="🌍",
  layout="wide"
)

# Baslik ve aciklamalar
st.title("🌍 Akıllı Turist Rehberi (Streaming Modu)")
st.markdown(
  """
  <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h3>🇹🇷 Türkiye Turizm Rehberiniz</h3>
    <p>Türkiye'nin dört bir yanındaki turistik yerler, yöresel lezzetler, tarihi mekanlar ve seyahat önerileri hakkında detaylı bilgi alabilirsiniz.</p>
    <p><strong>Örnek sorular:</strong> İstanbul'da gezilecek yerler nelerdir? Kapadokya'ya nasıl gidilir? Gaziantep'in meşhur yemekleri nelerdir?</p>
  </div>
  """, 
  unsafe_allow_html=True
)

# Sidebar ile model ayarlari
with st.sidebar:
  st.header("⚙️ Ayarlar")

  # Model secimi
  model_options=["llama3.2:3b", "llama3.2:1b", "llama3.1:8b"]
  selected_model = st.selectbox("Model Seçin: ", model_options, index=0)

  # Sicaklik ayari
  temperature = st.slider("Üretkenlik Seviyesi: ", 0.0, 1.0, 0.7, 0.1)

  # Gecmisi temizleme butonu
  if st.button("🗑️ Sohbet Geçmişini Temizle"):
    st.session_state.clear()
    st.rerun()

  st.markdown("---")
  st.markdown("💡 **İpucu:** Daha spesifik sorular sorun!")


# session state baslatma (streamlit de kullanici gecmisini tutmak icin)
if "memory" not in st.session_state:
  st.session_state.memory = ConversationBufferMemory(return_messages=True) 

if "messages" not in st.session_state:
  st.session_state.messages = []

# Sistem Mesaji
system_prompt = """Sen Türkiye'nin en deneyimli ve bilgili turizm rehberisin. Görevin:

🎯 AMAÇ: Türkiye'deki turizm deneyimlerini zenginleştirmek

📍 KAPSAM: 
- Şehirler ve bölgeler hakkında detaylı bilgi
- Tarihi yerler ve kültürel değerler
- Yöresel yemekler ve mutfak kültürü
- Ulaşım ve konaklama önerileri
- Aktiviteler ve deneyimler
- Pratik seyahat ipuçları

✨ TARZIN:
- Samimi ve sıcak
- Detaylı ama anlaşılır
- Pratik öneriler içeren
- Kültürel zenginlikleri vurgulayan

🚀 HER CEVABINDA:
- Spesifik öneriler ver
- Fiyat aralıkları belirt (mümkünse)
- Zaman tavsiyeleri ekle
- Alternatif seçenekler sun
- Yerel ipuçları paylaş
"""

# mesaj kutusu: kullanicidan gelen mesaj
user_input = st.chat_input("Bir şehir, mekan, yemek ya da aktivite sorabilirsiniz...")

# sohbet gecminisini arayuzde goster
# tum mesaj gecmisini sirasiyla gezip ekrana yazdiralim. 
for msg in st.session_state.memory.chat_memory.messages:
  if isinstance(msg, HumanMessage):
    with st.chat_message("Kullanici: "):
      st.markdown(msg.content)
  else: #ai ise
    with st.chat_message("Akilli Rehber: "):
      st.markdown(msg.content)

if user_input: 
  # yeni gelen kullanici mesajini ilk olarak memory e ekliyor. 
  st.session_state.memory.chat_memory.add_user_message(user_input)
  with st.chat_message("Kullanici: "):
    st.markdown(user_input)

  with st.chat_message("Akıllı Rehber: "):
    response_placeholder = st.empty() # streamlite gecici mesaj kutusu
    stream_handler = StreamHandler(response_placeholder)
    llm = initialize_llma(selected_model, temperature, stream_handler)

    # tum konusmayi modele verecek sekilde mesajlari olusturalim. sistem mesaji + memory + human message
    messages = [
      SystemMessage(content="Sen akıllı bir turizm ve turist rehberisin. "
        "Kullanıcılara Türkiye'de ki şehirler, tarihi yerler, yöresel yemekler, ulaşım ve tatil önerileri hakkında güzel bilgler ver. "
      )
    ] + st.session_state.memory.load_memory_variables({})["history"] + [HumanMessage(content = user_input)]

    # modelden yanit al
    response = llm(messages)

    # yaniti hafizaya kaydet
    st.session_state.memory.chat_memory.add_ai_message(response.content)
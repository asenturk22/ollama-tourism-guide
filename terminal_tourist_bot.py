"""
problem tanimi : kullanicilar yazili olarak soru soracak, gercek zamanli
 ve dogal sekilde yanitlar alabilecek. 
  - akilli turizm rehberi
  - turkiye ozelinde : tarihi yerler, kulturel etkinlikler, yemekler, ulasim, ....
  - llama 3.2 3b parametreli modeli ile cevaplari streamlit uzerinden gercek zamanli olarak gerceklestirelim. 

model tanitimi : LLAMA (Large Language Model Meta AI)
  - acik kaynakli : akademik ve ticari kullanimlar icin uygundur. 
  - verimli : daha az parametre ile ayni performansi sergiliyor. 
  - moduler : 1b, 3b, 70b, ... gibi parametrelere sahip modelleri var. 
  - lokal de calisabilir.
plan/program : 

install libraries : freeze

import libraries 

ollama indir ve llama kur 
  - https://ollama.com/download
  - https://ollama.com/library/llama3.2:3b
  - ollama run llama3.2:3b
"""


# import libraries
from langchain_ollama import ChatOllama # ollama llm arayuzu
from langchain.schema import SystemMessage, HumanMessage # chat mesaj siniflari
from langchain.memory import ConversationBufferMemory # konusma gecmisi icin basit bir hafiza


# llama model 
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.8,
    num_predict=256
)

# hafiza ekleme, konusma gecmisi takip etme
memory = ConversationBufferMemory(return_messages=True) # Bu sayede mesajlar formatli doner. 

# Hosgeldin mesaji
print("Akıllı Turizm Rehberine Hoş Geldiniz")
print("Size gezilecek yerler, tatil önerileri ve ulaşım bilgileri gibi konularda yardımcı olabilirim.")


# terminal uzerinden llama ile konusma
while True:
  user_input = input("Siz: ")

  if user_input.lower() in ["quit", "exit", "çık"]:
    print("Program sonlandırıldı")
    break

  # Kullancinin mesajlarini hafizaya kaydediyoruz. 
  memory.chat_memory.add_user_message(user_input) 

  # model icin gerekli olan tum mesajlari olustur. 
  messages = [
    SystemMessage(content = "Sen bir akıllı turizm rehberisin."
      "Kullanıcılara Türkiye'de ki şehirler, tarihi yerler, yöresel yemekler, ulaşım ve tatil önerileri hakkında yardımcı ol."
    )
  ] + memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]


  # modelden yanit alma
  response = llm(messages)

  # modelin cevabini hafizaya ekle
  memory.chat_memory.add_ai_message(response.content) 

  print(f"Rehber ai: {response.content}")
import time
from datetime import date
import streamlit as strlit

# Sayfa Yapılandırması (Tarayıcı sekme adı ve simgesi)
strlit.set_page_config(
    page_title="İyi ki Doğdun KALBIMMMMM! 🎉", page_icon="🎂", layout="centered"
)


# Özel CSS ile biraz renk ve tasarım katalım
strlit.markdown(
    """
    <style>
    .main {
        background-color: #fff0f5;
    }
    h1 {
        color: #ff1493;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- ANA BAŞLIK ---
strlit.title("🌟 İyi ki Doğdunnnnn KALBIMMMMMMMMM! 🌟")
strlit.write("---")

# --- KİŞİSEL BİLGİLER / GİRİŞ ---
strlit.subheader(
    "Bugün dünyadaki en harika insanlardan birinin doğum günü! 🎈"
)
strlit.write(
    "Bu site senin için tamamen Python ile özel olarak hazırlandı. Aşağıdaki sürprizleri keşfetmeye başla!"
)

# --- BÖLÜM 1: Geri Sayım / Yaş Hesaplayıcı ---
strlit.markdown("### ⏳ Sizin İçin Küçük Bir Not")
dogum_tarihi = date(
    2000, 5, 15
)  # Buraya arkadaşının doğ101um tarihini (Yıl, Ay, Gün) yazabilirsin!
bugun = date.today(2006.10.10.)
yas = (
    bugun.year
    - dogum_tarihi.year
    - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
)

strlit.info(
    f"Bugün itibarıyla **{yas}** yaşındasın ve dünya seninle birlikte çok daha güzel!"
)

# --- BÖLÜM 2: Anı Galerisi (Fotoğraflar) ---
strlit.markdown("### 📸 Birlikte Harika Anılarımız")
strlit.write("En güzel karelerimizden bazıları:")

# Örnek sütun yerleşimi (Yan yana fotoğraflar göstermek için)
 col2 = strlit.columns(1)

    except:
        strlit.warning(
            "fotograflar/foto1.jpg bulunamadı. Klasörü kontrol et! 😊"
        )

with col2:
    try:
        strlit.image(
            "fotograflar/fotp1.jpeg",
            caption="İyi ki varsın kalbimmmm!",
            use_container_width=True,
        )

# --- BÖLÜM 3: Sürpriz Butonu ve Konfeti Efekti ---
strlit.markdown("---")
strlit.markdown("### 🎁 Sürpriz Hediyen veya Mesajın")

if strlit.button("Sürprizi Açmak İçin Tıkla! 🎊"):
    # Konfeti patlatma efekti
    strlit.balloons()

    strlit.success(
        "İyi ki dogdunnnnnnnn kalbimmmmmm seni cok seviyorum her zaman yanimda oldugun icin tesekkür ederim iyiki girdin hayatima umarim her zaman iyi günde kötü günde de beraber oluruz senii cooooooooooooookk seviyorum bitanemmmm 🎂🍰"
    )

    # İsteğe bağlı müzik ekleme (Eğer klasörde müzik varsa)
    try:
        audio_file = open("fotp1.jpeg", "rb")
        audio_bytes = audio_file.read()
        strlit.audio(audio_bytes, format="audio/mp3", autoplay=True)
    except:
        pass

# --- ALT BİLGİ ---
strlit.markdown("---")
strlit.markdown(
    "<p style='text-align: center; color: gray;'>❤️ Python ile Sevgiyle Hazırlanmıştır ❤️</p>",
    unsafe_allow_html=True,
)
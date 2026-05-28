import streamlit as st

st.set_page_config(page_title="Portafolio - Juanita Nassar Londoño", 
                   page_icon="🌟", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #fffde7; color: #333333; }
section[data-testid="stSidebar"] { display: none; }
h1, h2, h3 { color: #f57f17; }

.app-card {
    background: #fff8e1;
    border: 1px solid #ffe082;
    border-radius: 12px;
    padding: 24px;
    margin: 10px 0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 6px rgba(249,168,37,0.1);
}
.app-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(249,168,37,0.25);
}
.app-card h3 {
    color: #e65100 !important;
    margin-bottom: 8px;
    font-size: 1.1rem;
}
.app-card p {
    color: #555 !important;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 16px;
}
.app-link {
    display: inline-block;
    background-color: #f9a825;
    color: white !important;
    padding: 8px 18px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.88rem;
    transition: background-color 0.2s ease;
}
.app-link:hover {
    background-color: #f57f17;
    color: white !important;
}
.tag {
    display: inline-block;
    background: #fff3cd;
    border: 1px solid #ffe082;
    border-radius: 20px;
    padding: 3px 10px;
    font-size: 0.75rem;
    color: #e65100;
    font-weight: 500;
    margin-bottom: 10px;
    margin-right: 4px;
}
.header-card {
    background: linear-gradient(135deg, #fff8e1 0%, #fff3cd 100%);
    border: 1px solid #ffe082;
    border-left: 6px solid #f9a825;
    border-radius: 12px;
    padding: 40px;
    margin-bottom: 30px;
    box-shadow: 0 2px 8px rgba(249,168,37,0.15);
}
.contact-card {
    background: #fff8e1;
    border: 1px solid #ffe082;
    border-radius: 12px;
    padding: 32px 40px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(249,168,37,0.1);
}
.contact-card h3 {
    color: #f57f17 !important;
    margin-bottom: 16px;
}
.contact-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #fff3cd;
    border: 1px solid #ffe082;
    border-radius: 30px;
    padding: 10px 24px;
    margin: 6px;
    font-size: 0.95rem;
    color: #333;
    text-decoration: none;
    transition: background 0.2s ease;
}
.contact-item:hover {
    background: #ffe082;
    color: #333;
}
hr { border-color: #ffe082 !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────
st.markdown("""
<div class="header-card">
    <h1 style="margin:0; font-size:2.2rem;">🌟 Portafolio de Apps de Juanita Nassar</h1>
    <p style="margin:12px 0 4px 0; color:#888; font-size:1rem;">
        Colección de aplicaciones interactivas desarrolladas con Streamlit,
        Python y herramientas de inteligencia artificial.
    </p>
    <p style="margin:0; color:#f9a825; font-size:0.9rem; font-weight:500;">
        🎓 Interfaces Multimodales · Universidad EAFIT
    </p>
</div>
""", unsafe_allow_html=True)

# ── Apps ───────────────────────────────────────────────────────────
apps = [
    {
        "emoji": "🖥️",
        "nombre": "Primera App",
        "desc": "Introducción a Streamlit: columnas, checkboxes, radio buttons y selectbox interactivos.",
        "tags": ["Streamlit", "Interfaz"],
        "link": "https://intro2-2reritgmdnxmmx2hbeymx4.streamlit.app/"
    },
    {
        "emoji": "🎤",
        "nombre": "Traductor de Voz",
        "desc": "Traduce voz a texto en tiempo real y genera audio en múltiples idiomas usando gTTS y Google Translate.",
        "tags": ["Voz", "Traducción", "Audio"],
        "link": "https://traductor-8ux5cbmku7hev4pmjstw9h.streamlit.app/"
    },
    {
        "emoji": "🔊",
        "nombre": "Texto a Audio",
        "desc": "Convierte cualquier texto escrito en audio descargable con selección de idioma y velocidad.",
        "tags": ["gTTS", "Audio", "NLP"],
        "link": "https://project2-lnceopubbb2w37xeax7qdc.streamlit.app/"
    },
    {
        "emoji": "😊",
        "nombre": "Análisis de Sentimiento",
        "desc": "Detecta si un texto es positivo, negativo o neutral usando TextBlob y Google Translate.",
        "tags": ["TextBlob", "Sentimiento", "NLP"],
        "link": "https://sentimentasentimientoab1.streamlit.app/"
    },
    {
        "emoji": "📝",
        "nombre": "Analizador de Texto",
        "desc": "Análisis completo de frecuencia de palabras, sentimiento por frases y subjetividad.",
        "tags": ["TextBlob", "Frecuencia", "NLP"],
        "link": "https://kkaxwqdkgyxunab4ruhnhl.streamlit.app/"
    },
    {
        "emoji": "☁️",
        "nombre": "WordCloud Studio",
        "desc": "Genera nubes de palabras personalizadas desde cualquier texto con múltiples paletas y formas.",
        "tags": ["WordCloud", "Visualización"],
        "link": "https://wordcloudstudio-i9apvsks8xtkcvwgbqqzga.streamlit.app/"
    },
    {
        "emoji": "🔍",
        "nombre": "TF-IDF en Inglés",
        "desc": "Busca el documento más relevante para una pregunta usando TF-IDF y similitud coseno.",
        "tags": ["TF-IDF", "Sklearn", "NLP"],
        "link": "https://5fh6uxnxd4c2t5bpfx6da5.streamlit.app/"
    },
    {
        "emoji": "🔎",
        "nombre": "TF-IDF en Español",
        "desc": "Versión en español del motor TF-IDF con stemming y visualización de similitudes.",
        "tags": ["TF-IDF", "Español", "NLP"],
        "link": "https://tdfesp-vxb6zgdbrskgp3rlbgmf9b.streamlit.app/"
    },
    {
        "emoji": "📷",
        "nombre": "OCR App",
        "desc": "Extrae texto de imágenes usando reconocimiento óptico de caracteres con filtros visuales.",
        "tags": ["OCR", "OpenCV", "Pytesseract"],
        "link": "https://9arxcch7q8mjuqcoawmkqe.streamlit.app/"
    },
    {
        "emoji": "📷🔊",
        "nombre": "OCR + Audio",
        "desc": "Extrae texto de imágenes con OCR y lo traduce y convierte a audio en múltiples idiomas.",
        "tags": ["OCR", "Audio", "Traducción"],
        "link": "https://ocr-audio-stwb49vyjn5jzwlhtnppkn.streamlit.app/"
    },
    {
        "emoji": "🖼️",
        "nombre": "Análisis de Imagen",
        "desc": "Interpreta imágenes y obtén descripciones inteligentes en segundos.",
        "tags": ["Visión", "IA", "Imágenes"],
        "link": "https://visionapp-bqjnbpags6hkl7xncro5ky.streamlit.app/"
    },
    {
        "emoji": "💬",
        "nombre": "Chat PDF",
        "desc": "Chatbot para la interacción con documentos en PDF.",
        "tags": ["PDF", "Chatbot", "IA"],
        "link": "https://chatpdf2-cqfnxl9ki4fho5agwrzabv.streamlit.app/"
    },
    {
        "emoji": "🎨",
        "nombre": "Tablero de Dibujo",
        "desc": "Lienzo interactivo para dibujar libremente con distintos colores y tamaños de pincel.",
        "tags": ["Canvas", "Dibujo", "Interactivo"],
        "link": "https://tableropd-rudf8swfhdxnwzcsmj5iwb.streamlit.app/"
    },
    {
        "emoji": "✏️",
        "nombre": "Tablero Inteligente",
        "desc": "Dibuja y deja que la IA identifique qué figura o elemento has trazado en tiempo real.",
        "tags": ["Visión", "IA", "Dibujo"],
        "link": "https://drawrecog-8jiunjphggpxnbkgdfgh3s.streamlit.app/"
    },
    {
        "emoji": "🖊️",
        "nombre": "Reconocimiento de Escritura",
        "desc": "Reconoce texto manuscrito a partir de trazos realizados directamente en la interfaz.",
        "tags": ["Handwriting", "OCR", "IA"],
        "link": "https://cdjkjo77zgswcb9uqkwzar.streamlit.app/"
    },
    {
        "emoji": "🧠",
        "nombre": "Insight Sketch",
        "desc": "Dibuja cualquier cosa y la IA interpreta tu trazo para contarte datos curiosos y enseñarte sobre lo que has dibujado.",
        "tags": ["Visión", "IA", "Dibujo"],
        "link": "https://insights-3uwdgx5puvdevrsh9fcf9f.streamlit.app/"
    },
    {
        "emoji": "📥",
        "nombre": "Receptor MQTT",
        "desc": "Recibe y muestra en tiempo real los mensajes publicados en un topic MQTT desde cualquier dispositivo.",
        "tags": ["MQTT", "IoT", "Tiempo real"],
        "link": "https://recepmqtt-meoq7wkb5gq5tg3vjwtdmf.streamlit.app/"
    },
    {
        "emoji": "📤",
        "nombre": "Emisor MQTT",
        "desc": "Publica mensajes a un broker MQTT para controlar dispositivos y sistemas conectados.",
        "tags": ["MQTT", "IoT", "Publicación"],
        "link": "https://sendcmqtt-aqkmbjy25yalpw3o5krxba.streamlit.app/"
    },
    {
        "emoji": "🎙️",
        "nombre": "Control por Voz MQTT",
        "desc": "Reconoce comandos de voz y los publica automáticamente en un broker MQTT para control de dispositivos.",
        "tags": ["Voz", "MQTT", "IoT"],
        "link": "https://voicecontrol-mmbjkp3utx67fcxkgyut3r.streamlit.app/"
    },
]

# ── Grid de cards ──────────────────────────────────────────────────
st.markdown(f"### 📱 {len(apps)} aplicaciones disponibles")
st.markdown("---")

cols = st.columns(3)
for i, app in enumerate(apps):
    with cols[i % 3]:
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in app["tags"]])
        st.markdown(f"""
        <div class="app-card">
            <h3>{app['emoji']} {app['nombre']}</h3>
            {tags_html}
            <p>{app['desc']}</p>
            <a href="{app['link']}" target="_blank" class="app-link">
                🚀 Abrir app
            </a>
        </div>
        """, unsafe_allow_html=True)

# ── Contacto ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="contact-card">
    <h3>📬 Contacto</h3>
    <p style="color:#888; margin-bottom:16px;">
        ¿Tienes preguntas o comentarios sobre alguna de las aplicaciones?
    </p>
    <a href="mailto:mjruab@eafit.edu.co" class="contact-item">
        ✉️ mjruab@eafit.edu.co
    </a>
    <br><br>
    <p style="color:#bbb; font-size:0.82rem; margin:0;">
        🎓 Universidad EAFIT · Interfaces Multimodales
    </p>
</div>
""", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<p style="text-align:center; color:#bbb; font-size:0.82rem;">
    Desarrollado con ❤️ por María José Rúa · Streamlit · 2026
</p>
""", unsafe_allow_html=True)

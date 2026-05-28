import streamlit as st

st.set_page_config(page_title="Portafolio - Juanita Nassar Londoño", 
                   page_icon="🌟", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@500;600;700;800&display=swap');

:root {
    --electric-blue: #00D9FF;
    --blue-main: #0099FF;
    --blue-deep: #0066FF;
    --navy: #07111F;
    --navy-soft: #0D1B2E;
    --card: rgba(13, 27, 46, 0.82);
    --border: rgba(0, 217, 255, 0.22);
    --text: #EAF7FF;
    --muted: #9DB6C9;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(0,217,255,0.22), transparent 32%),
        radial-gradient(circle at bottom right, rgba(0,102,255,0.18), transparent 28%),
        linear-gradient(135deg, #050B14 0%, #07111F 48%, #0A1930 100%);
    color: var(--text);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1240px;
}

section[data-testid="stSidebar"] {
    display: none;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    color: var(--text);
    letter-spacing: -0.04em;
}

hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(0,217,255,0.5), transparent) !important;
    margin: 2rem 0 !important;
}

.header-card {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(135deg, rgba(0,217,255,0.18), rgba(0,102,255,0.12)),
        rgba(13, 27, 46, 0.84);
    border: 1px solid rgba(0,217,255,0.28);
    border-radius: 28px;
    padding: 52px 48px;
    margin-bottom: 34px;
    box-shadow:
        0 24px 70px rgba(0, 0, 0, 0.38),
        inset 0 1px 0 rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
}

.header-card::before {
    content: "";
    position: absolute;
    inset: -2px;
    background:
        radial-gradient(circle at 90% 12%, rgba(0,217,255,0.34), transparent 28%),
        radial-gradient(circle at 10% 90%, rgba(0,153,255,0.24), transparent 30%);
    pointer-events: none;
}

.header-card > * {
    position: relative;
    z-index: 1;
}

.header-card h1 {
    margin: 0;
    font-size: clamp(2rem, 5vw, 4rem);
    line-height: 1;
    font-weight: 900;
    background: linear-gradient(90deg, #FFFFFF, #00D9FF 55%, #0099FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.header-card p {
    max-width: 760px;
}

.hero-subtitle {
    margin: 20px 0 8px 0;
    color: #C8EFFF;
    font-size: 1.08rem;
    line-height: 1.7;
}

.hero-label {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 14px;
    color: #07111F;
    background: linear-gradient(135deg, #00D9FF, #0099FF);
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 0.86rem;
    font-weight: 800;
    box-shadow: 0 12px 32px rgba(0,153,255,0.28);
}

.section-title {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-top: 8px;
    margin-bottom: 6px;
}

.section-title h3 {
    margin: 0;
    font-size: 1.45rem;
    font-weight: 800;
    color: #FFFFFF;
}

.section-pill {
    color: var(--electric-blue);
    border: 1px solid rgba(0,217,255,0.28);
    background: rgba(0,217,255,0.08);
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 700;
}

.app-card {
    min-height: 260px;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.055), rgba(255,255,255,0.025)),
        rgba(13, 27, 46, 0.86);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 26px;
    margin: 12px 0;
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease,
        background 0.25s ease;
    box-shadow:
        0 16px 42px rgba(0, 0, 0, 0.24),
        inset 0 1px 0 rgba(255,255,255,0.06);
    backdrop-filter: blur(12px);
}

.app-card:hover {
    transform: translateY(-7px);
    border-color: rgba(0,217,255,0.72);
    background:
        linear-gradient(180deg, rgba(0,217,255,0.10), rgba(255,255,255,0.025)),
        rgba(13, 27, 46, 0.94);
    box-shadow:
        0 24px 62px rgba(0, 153, 255, 0.20),
        0 0 0 1px rgba(0,217,255,0.16);
}

.app-card h3 {
    color: #FFFFFF !important;
    margin-bottom: 12px;
    font-size: 1.15rem;
    font-weight: 800;
    line-height: 1.25;
}

.app-card p {
    color: var(--muted) !important;
    font-size: 0.92rem;
    line-height: 1.65;
    margin-bottom: 20px;
}

.tag {
    display: inline-block;
    background: rgba(0,217,255,0.10);
    border: 1px solid rgba(0,217,255,0.22);
    border-radius: 999px;
    padding: 5px 11px;
    font-size: 0.72rem;
    color: #7CEBFF;
    font-weight: 700;
    margin-bottom: 12px;
    margin-right: 5px;
}

.app-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #00D9FF, #0099FF);
    color: #03101C !important;
    padding: 10px 18px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 900;
    font-size: 0.88rem;
    transition:
        transform 0.22s ease,
        box-shadow 0.22s ease,
        filter 0.22s ease;
    box-shadow: 0 12px 26px rgba(0,153,255,0.28);
}

.app-link:hover {
    transform: translateY(-2px);
    filter: brightness(1.08);
    color: #03101C !important;
    box-shadow: 0 16px 34px rgba(0,217,255,0.34);
}

.contact-card {
    background:
        linear-gradient(135deg, rgba(0,217,255,0.13), rgba(0,102,255,0.08)),
        rgba(13, 27, 46, 0.84);
    border: 1px solid rgba(0,217,255,0.25);
    border-radius: 28px;
    padding: 38px 42px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0 20px 54px rgba(0, 0, 0, 0.28);
}

.contact-card h3 {
    color: #FFFFFF !important;
    margin-bottom: 12px;
    font-size: 1.55rem;
    font-weight: 800;
}

.contact-card p {
    color: var(--muted);
}

.contact-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(0,217,255,0.10);
    border: 1px solid rgba(0,217,255,0.28);
    border-radius: 999px;
    padding: 12px 24px;
    margin: 6px;
    font-size: 0.95rem;
    color: #DFFAFF !important;
    text-decoration: none;
    transition:
        background 0.22s ease,
        transform 0.22s ease,
        border-color 0.22s ease;
}

.contact-item:hover {
    background: rgba(0,217,255,0.18);
    border-color: rgba(0,217,255,0.60);
    transform: translateY(-2px);
    color: #FFFFFF !important;
}

.footer-text {
    text-align: center;
    color: rgba(234,247,255,0.52);
    font-size: 0.82rem;
    margin: 0;
}

@media (max-width: 900px) {
    .header-card {
        padding: 34px 26px;
        border-radius: 22px;
    }

    .app-card {
        min-height: auto;
        padding: 22px;
    }

    .section-title {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────
st.markdown("""
<div class="header-card">
    <h1>🌟 Portafolio de Apps de Juanita Nassar</h1>
    <p class="hero-subtitle">
        Colección de aplicaciones interactivas desarrolladas con Streamlit,
        Python y herramientas de inteligencia artificial.
    </p>
    <p class="hero-label">
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
st.markdown(f"""
<div class="section-title">
    <h3>📱 {len(apps)} aplicaciones disponibles</h3>
    <span class="section-pill">Streamlit · IA · IoT · NLP</span>
</div>
""", unsafe_allow_html=True)

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
    <p style="margin-bottom:16px;">
        ¿Tienes preguntas o comentarios sobre alguna de las aplicaciones?
    </p>
    <a href="mailto:jnassarl@eafit.edu.co" class="contact-item">
        ✉️ mjruab@eafit.edu.co
    </a>
    <br><br>
    <p style="color:rgba(234,247,255,0.48); font-size:0.82rem; margin:0;">
        🎓 Universidad EAFIT · Interfaces Multimodales
    </p>
</div>
""", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<p class="footer-text">
    Desarrollado con ❤️ por Juanita Nassar · Streamlit · 2026
</p>
""", unsafe_allow_html=True)

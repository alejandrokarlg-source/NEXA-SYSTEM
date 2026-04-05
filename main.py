import streamlit as st
from groq import Groq

# 1. Configuration de l'interface Premium
st.set_page_config(page_title="NEXA PREMIUM", page_icon="🌐", layout="centered")

# Style pour un look sombre et pro
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 NEXA PREMIUM")
st.caption("Intelligence Artificielle Connectée | Propriété du PDG Alejandro")
st.write("---")

# 2. TA CLÉ API GROQ (Le moteur de réponse)
client = Groq(api_key="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")

# 3. Gestion de la mémoire de l'IA (Historique)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des anciens messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Zone de saisie (Comme Google)
if prompt := st.chat_input("Posez votre question à NEXA..."):
    # On mémorise ton message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Réponse intelligente via les serveurs Groq
    with st.chat_message("assistant"):
        try:
            # On envoie la question au modèle Llama 3
            completion = client.chat.completions.create(
               model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system", 
                        "content": "Tu es NEXA PREMIUM, une IA surpuissante créée par le PDG Alejandro, un jeune entrepreneur de 15 ans en Haïti. Tu es experte en Mathématiques, Business, et Technologie. Tu réponds de manière intelligente, rapide et polie en Français ou en Créole."
                    },
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ],
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Erreur de connexion aux serveurs : {e}")

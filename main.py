import streamlit as st

# --- CONFIGURATION DU SITE ---
st.set_page_config(page_title="NEXA - Google Auth", page_icon="🌐")

# --- SYSTÈME D'ABONNEMENT GOOGLE (SIMULATION) ---
# En attendant ta configuration Google Cloud, voici le verrou professionnel
if "google_user" not in st.session_state:
    st.session_state.google_user = None

if not st.session_state.google_user:
    st.title("🌐 NEXA GLOBAL SYSTEM")
    st.subheader("Connexion Sécurisée")
    st.write("Veuillez vous connecter avec votre compte Google pour accéder à l'IA.")
    
    if st.button("🚀 Se connecter avec Google"):
        # Ici, on simule la validation du compte Google
        st.session_state.google_user = "Utilisateur Google" 
        st.success("Connexion réussie !")
        st.rerun()
    st.stop()

# --- BASE DE CONNAISSANCES NEXA ---
CONNAISSANCES = {
    "bonjour": "Bonjour ! Bienvenue sur votre compte NEXA Premium.",
    "pdg": "Mon créateur et PDG est Guerrier Karl Alejandro.",
    "créé": "J'ai été conçu par Alejandro avec l'aide technologique de Gemini.",
    "maths": "Je maîtrise l'algèbre et la géométrie pour tes examens.",
    "pays": "Je connais tous les pays, leurs capitales et leur histoire.",
    "gemini": "Gemini est l'IA qui assiste Alejandro pour mon développement technique.",
    
    # INFOS SUR LA MISE À JOUR DE JUILLET
    "mise à jour": "⚠️ ALERTE : La grande mise à jour de NEXA arrive en JUILLET 2026 avec des fonctions de résolution de problèmes encore plus puissantes !",
    "juillet": "Juillet 2026 sera le mois de la révolution pour NEXA et le mois de vos examens d'État.",
    "examen": "Tes examens d'État sont du 6 au 8 juillet 2026. Prépare-toi avec NEXA !"
}

# --- INTERFACE UNE FOIS CONNECTÉ ---
st.title("🌐 NEXA PREMIUM")
st.info(f"👤 Connecté via Google | Prochaine mise à jour : *Juillet 2026*")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage du chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Posez une question à NEXA...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        question = prompt.lower().strip()
        reponse = "C'est un sujet intéressant. Mon PDG Alejandro prépare une réponse pour la mise à jour de juillet."
        
        for mot, texte in CONNAISSANCES.items():
            if mot in question:
                reponse = texte
                break
        
        st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- SIDEBAR ---
st.sidebar.title("⚙️ PARAMÈTRES")
st.sidebar.write(f"Utilisateur : *{st.session_state.google_user}*")
st.sidebar.warning("📅 Mise à jour : Juillet 2026")
if st.sidebar.button("Déconnexion"):
    st.session_state.google_user = None
    st.rerun()
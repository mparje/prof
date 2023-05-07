import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para evaluar la proficiencia en español
def evaluar_proficiencia(texto):
    prompt = (
        f"Evaluar la proficiencia en español del siguiente texto: \"{texto}\". "
        "Identificar errores y estimar el porcentaje de proficiencia. Tomar en cuenta erores de puntuación y vicios del lenguaje."
    )
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        temperature=0.5,
    )
    return completions.choices[0].text.strip()

def main():
    st.title("Evaluación de proficiencia en español con GPT-3")
    st.write("Introduce un texto en español y obtén una evaluación de tu proficiencia en español con GPT-3 DaVinci.")

    user_text = st.text_area("Escribe tu texto aquí:", height=200)

    if st.button("Evaluar"):
        if not user_text:
            st.warning("Por favor, ingrese un texto.")
        else:
            with st.spinner("Procesando la evaluación..."):
                resultado = evaluar_proficiencia(user_text)
                st.write(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

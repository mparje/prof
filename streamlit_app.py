import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para evaluar la proficiencia en español
def evaluar_proficiencia(texto):
    prompt = (
        f"Evaluar la calidad del siguiente texto: \"{texto}\". "
        "Para ello, 1. Reescribir el texto, mejorándolo. 2. Escribir un informe detallado de los cambios que se hicieron y por qué. 3. Asignar una puntuacion de 0 a 100."
        "4. Sugerir recursos en línea en español que ayuden a superar las deficiencias encontradas."
    )
    
    
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ])
    response = completion.choices[0].message.content
    return response

    
    
def main():
    st.title("Evaluación de competencia en español")
    
    # Agregar descripción e información de clases personalizadas en la columna izquierda
    st.sidebar.header("Acerca de esta aplicación")
    st.sidebar.markdown("""
    Esta aplicación utiliza la potencia de GPT-3 de OpenAI para evaluar la competencia del usuario en español. 
    Introduce un texto en español y obtén una evaluación detallada de tu dominio del idioma, junto con sugerencias 
    para recursos en línea que pueden ayudarte a mejorar.
    """)
    st.sidebar.markdown("""
    Si estás interesado en clases de español personalizadas, visita [Asesoría Lingüística Online](https://asesorialinguisica.online).
    """)

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

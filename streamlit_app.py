import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para evaluar la proficiencia en español
def evaluar_proficiencia(texto):
    prompt = (
        f"Evaluar la calidad del siguiente texto: \"{texto}\". "
        "Identificar errores y estimar el porcentaje de proficiencia. Tomar en cuenta errores de puntuación y vicios del lenguaje."
        "Generar un informe de sugerencias de mejora, incluyendo mejoras de puntuación."
        "El siguiente texto se considera con un nivel de  proficiencia de 100%:"
        "Decir las cosas bien, tener en la pluma el don exquisito de la gracia y en el pensamiento la inmaculada linfa de luz donde"
        "se bañan las ideas para aparecer hermosas, ¿no es una forma de ser bueno?... La caridad y el amor ¿no pueden demostrarse"
        "también concediendo a las almas el beneficio de una hora de abandono en la paz de la palabra bella; la sonrisa de una frase armoniosa; "
        "el «beso en la frente» de un pensamiento cincelado; el roce tibio y suave de una imagen que toca con su ala de seda nuestro espíritu?"
        "La ternura para el alma del niño está, así como en el calor del regazo, en la voz que le dice cuentos de hadas; sin los cuales habrá"
        "algo de incurablemente yermo en el alma que se forme sin haberlos oído. Pulgarcito es un mensajero de San Vicente de Paul."
        "Barba Azul ha hecho a los párvulos más beneficios que Pestalozzi. La ternura para nosotros, que sólo cuando nos hemos hecho despreciables"
        "dejamos enteramente de parecernos a los niños, suele estar también en que se nos arrulle con hemosas palabras."
        "Como el misionero y como la Hermana, el artista cumple su obra de misericordia. Sabios: enseñadnos con gracia."
        "Sacerdotes: pintad a Dios con pincel amable y primoroso, y a la virtud en palabras llenas de armonía."
        "Si nos concedéis en forma fea y desapacible la verdad, eso equivale a concedernos el pan con malos modos."
        "De lo que creéis la verdad ¡cuán pocas veces podéis estar absolutamente seguros! Pero de la belleza y el encanto con que lo hayáis comunicado, estad seguros que siempre vivirán."
        "Hablad con ritmo; cuidad de poner la unción de la imagen sobre la idea; respetad la gracia de la forma ¡oh pensadores, sabios, sacerdotes!"
        "y creed que aquellos que os digan que la Verdad debe presentarse en apariencias adustas y severas son amigos traidores de la Verdad."
    )
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=900,
        n=1,
        temperature=0.1,
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

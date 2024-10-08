import streamlit as st



st.title("Currículum Vitae")
st.markdown("---")

st.header("Información Personal")
st.write("""
- **Nombre:** **Santiago Peregrina Flores**
- **Edad:** 22 años
- **Correo Electrónico:** 0242856@up.edu.mx
- **Teléfono:** 3312706143  
- **Ciudad y Estado:** Guadalajara, Jalisco
""")

st.markdown("---")

st.header("Resumen")
st.write("""
Estudiante de 7mo semestre en la Universidad Panamericana de Guadalajara, cursando la licenciatura de Administración y Finanzas
Además llevo trabando más de año y medio en una empresa de Desarrollo Inmobiliario, donde he adquirido bastante experiencia y conocimientos.
Manejo las herramientas de Office, principalmente excel. También un poco sobre programación
""")

st.markdown("---")

st.header("Experiencia Laboral")

st.subheader("Becario de Finanzas")
st.write("""
- **Empresa:** Grupo MAG 
- **Duración:** abril de 2023 - Actualidad
- **Responsabilidades:**  
1. Elaboración de modelos financieros sobre proyectos inmobiliarios
2. Análisis de costos, gastos, ingresos y futuros proyectos
3. Elaboración de proyecciones financieras       
""")

st.subheader("Venta de Joyería")
st.write("""
- **Empresa:** Personal 
- **Duración:** 2020 - Actualidad 
- **Responsabilidades:**  
1. Venta de joyería de oro y diamantes en tiempo libre
""")



st.header("Educación")

st.subheader("Licenciatura en Administración y Finanzas")
st.write("""
- **Institución:** Universidad Panamericana de Guadalajara
- **Duración:** 2021 - Actualidad (termino en 2025)  

""")
st.progress(78)

st.subheader("Preparatoria")
st.write("""
- **Institución:** Liceo del Valle A.C.
- **Duración:** 2019 - 2021

""")
st.progress(100)
st.markdown("---")

st.header("Habilidades")
st.write("""
- **Programas y Aplicaciones:** Microsoft Office, Google Drive, VBA, Python (aprendiendo actualmente)
- **Aptitudes:** Liderazgo, buen manejo del estrés, trabajo bajo presión, honestidad ante todo
""")

st.markdown("---")

st.header("Contacto")
st.write("Para cualquier duda, aclaración o contacto, no dude en llamarme a mi telefono personal o correo electrónico mencionado en la parte superior de la página.")




import streamlit as st

st.set_page_config(page_title='Mateus Schualtz', layout="wide")

st.header('Prazer, sou Mateus Schipanski Schualtz!')

st.write("\n\n")

col1, col2 = st.columns([2, 1],gap="large")

with col1:
    st.markdown('## Quem Sou eu?')
    st.markdown('''<p style='text-align: justify;'>      
             Formado em Economia pela UniSantaCruz, foi na universidade que tive meu primeiro contato com estatística e métodos preditivos
             nas matérias de Estatística e Econometria, essa experiência despertou meu interesse pela Ciência de Dados, e desde então, decidi direcionar minha carreira para essa área.
             Busquei conhecer melhor sobre as principais ferramentas da Ciência de Dados, e optei por fazer um curso de extensão onde 
             pude conhecer desde ferramentas básicas como Pandas, bibliotecas de DataViz, SQL, até mesmo conteúdos mais avançados como Machine Learning e Deploy de modelos.
             <p style='text-align: justify;'> 
             Após me formar passei a cursar um MBA em Data Science e Analytics pela USP/ESALQ, para que eu possa me aprofundar mais nas tendências da Ciência de Dados.
             Devido à minha formação inicial em Economia, tenho uma afinidade especial pelas áreas de Crédito e Pricing, onde consigo aplicar meus conhecimentos em Macroeconomia e Microeconomia, o que é um diferencial no momento da análise. 
             Buscando um desenvolvimento contínuo, planejo ingressar no Mestrado Profissional em Economia da UFPR em um futuro próximo. Acredito que essa combinação 
             entre uma sólida base teórica e a prática do mercado de trabalho me permitirá desenvolver soluções inovadoras e impactantes para as empresas.
             <p style='text-align: justify;'> 
             Além do meu trabalho, sou casado e dedico meu tempo livre à minha família. Tenho dois hobbies que são minha paixão: música e gastronomia.
             Apesar de ter uma formação em gastronomia pela PUCPR, optei por não seguir profissionalmente nessa área, mas continuo a explorar minha criatividade na cozinha como um hobby.
             ''',unsafe_allow_html=True)
    
st.write("\n\n")

with col2:
    st.image('./Img/foto_cracha.jpg',  width=425)

st.sidebar.markdown('HOME')

st.success('Fico feliz em ter tido a oportunidade de me apresentar! Não se esqueça de explorar o menu lateral para descobrir mais sobre meus projetos ou para entrar em contato comigo.')
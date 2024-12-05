<template>
    <div>
      <section class="img"></section>
      <article class="fade-in">
        <section>
          <h1>Quem Somos?</h1>
          <p>
            A N9 Agência é uma empresa especializada em soluções criativas e inovadoras para empresas que buscam fortalecer sua presença no mercado.
          </p>
          <p>
            Com um olhar atento às tendências de design e marketing, nós oferecemos uma gama de serviços que inclui criação de material gráfico, desenvolvimento de identidade visual, gestão de mídias sociais e estratégias de marketing digital.
          </p>
          <p>
            Nosso objetivo é proporcionar uma comunicação visual impactante e eficaz, alinhada com os valores e o posicionamento de cada cliente através de projetos personalizados e uma abordagem estratégica. Buscamos conectar marcas e públicos de forma autêntica, promovendo resultados concretos e sustentáveis.
          </p>
          <p>
            Apaixonados pelo que fazemos, estamos comprometidos em transformar ideias em experiências visuais que cativam e engajam.
          </p>
        </section>
      </article>
    </div>
  </template>
  
  <script>
  export default {
    mounted() { 
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("visible");
            }
          });
        },
        {
          threshold: 0.1,
        }
      );
      document.querySelectorAll(".fade-in").forEach((el) => observer.observe(el));
    },
  };
  </script>
  
  <style scoped>
  h1, p {
    font-family: 'Roboto';
  }
  h1 {
    font-size: 3rem;
    color: var(--dark);
    font-family: 'Bebas Neue';
    letter-spacing: 12px;
    padding-top: 30px;
  }
  p {
    padding: 5px 0;
    font-size: 1.3rem;
    color: var(--dark);
  }
  .img {
    display: flex;
    width:50%;
    z-index: 9;
    height: auto;
    background: url('../imgs/SVG/about.svg') no-repeat center;
    background-size: contain;
    background-position: bottom;
  }
  article section {
    width: 100%;
    padding:0 20px;
  }
  div {
    display: flex;
    flex-direction: row-reverse;
    gap: 50px;
    width: 60vw;
    padding: 50px 20px;
    border-radius: 10px;
  }
  article {
    display: flex;
    flex-direction: column;
    text-align: start;
    padding: 20px;
    margin: 0 auto;
    width: 45vw;
    margin: 0 20px 0 0;
    max-width: var(--maxw);
    opacity: 0; 
    transform: translateY(50px); 
    transition: all 0.8s ease-in-out;
  }
  article.visible {
    opacity: 1;
    transform: translateY(0); 
  }
  @media screen and (max-width: 768px) {
    div {
      margin-top: -40px;
      flex-direction: column-reverse;
      width: 100vw;
      justify-content: center;
      text-align: center;
    }
    .img{
      width: calc(100vw /1.4);
      height:calc(100vh /2);
      margin: 0 auto;
    }
    article {
      text-align: center;
      width: 100%;
      padding: 10px 0;
      margin-top: 40px;
    }
    h1 {
      padding: 0;
      margin:4vh 0 5vh 0;
      font-size: 2rem;
    }
    p{
      text-align: left;
    }
  }
  </style>
  
<template>
  <div>
    <header>
      <h1>Projetos de Sucesso</h1>
      <span>Clientes que confiaram nos nossos Serviços</span>
    </header>
    <article class="portfolioCards">
      <Portfolio 
        v-for="(item, index) in portfolios" 
        :key="index" 
        :title="item.title" 
        :background="item.img"
        :desc="item.desc" 
        :features="item.specs" 
        :date="formatDate(item.created_at)" 
        class="portfolioCard" 
      />
    </article>
  </div>
</template>

<script>
import Portfolio from '@/components/portfolio.vue';
import apiService, { url_api } from '@/services/apiService';

export default {
  components: {
    Portfolio,
  },
  methods:{
    formatDate(isoDate) {
      const date = new Date(isoDate);
      const options = { day: 'numeric', month: 'long', year: 'numeric' };
      return date.toLocaleDateString('pt-BR', options);
    },
  },
  data() {
    return {
      portfolios: [
        {
          title: "N9 Agência Digital",
          desc: "Desenvolvimento de layout website, programação vue.js com Django e todo material digital",
          features: "VueJS, Angular, Django, SQLite, Python, Illustrator, Figma, MySQL",
          date: "01 de novembro de 2024",
        },
        {
          title: "Startup X",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        },
        {
          title: "Startup X",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        },
        {
          title: "Startup X",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        },
        {
          title: "BAZARZINHO",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        },
        {
          title: "Startup X",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        }, {
          title: "Startup X",
          desc: "Plataforma de e-commerce com integração de pagamentos e layout responsivo",
          features: "React, Node.js, MongoDB, AWS, CSS, UX/UI Design",
          date: "15 de outubro de 2024",
        },
      
      ],
    };
  },
  
  async created() {
    try {
        const response = await apiService.getPortfolio(); 
        this.portfolios = response.data;
        this.portfolios.forEach((client, index) => {
            console.log(`Cliente ${index + 1}:`, client);
            client.img = `${url_api}/media/${client.img}`;
        });
    } catch (error) {
        console.error('Erro ao buscar informações:', error);
    }
    },
  mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    });
    const cards = document.querySelectorAll(".portfolioCard");
    cards.forEach((card) => observer.observe(card));
  },
};
</script>

<style scoped>
h1 {
  display: flex;
  font-family: 'Bebas Neue';
  font-size: 3rem;
  letter-spacing: 3px;
  color: var(--rxSecondary);
  text-transform: uppercase;
}
header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
  padding: 80px;
}
span {
  font-family: 'Roboto';
  color: var(--darkgray);
  font-weight: bold;
}
.portfolioCards {
  display: flex;
  max-width: 70vw;
  justify-content: center;
  flex-wrap: wrap;
  height: auto;
  gap: 50px;
  flex-direction: row;
}
.portfolioCard {
  opacity: 0;
  transform: translateX(-50px);
  transition: opacity 0.6s ease, transform 1s ease;
}
.portfolioCard.visible {
  opacity: 1; 
  transform: translateX(0); 
}
@media screen and (max-width: 768px) {
    header{
    width: 80vw;
    padding:30px 0 50px 0;
    text-align: center;
    }
    h1{
      font-size: 2rem;
    }
    .portfolioCards{
      display: flex;
      width: 90vw;
      margin: 0 auto;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    }
}
</style>

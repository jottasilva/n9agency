<template>
   <section id="about-container">
        <section class="about">
            <section class="about-title">
                <h1>alguns serviços</h1>
                <p>conheça um pouco mais do que nós fazemos</p>
            </section>
            <section class="about-cards">
                <Card title="IDENTIDADE VISUAL" subtitle="Sua identidade visual, desenhada para marcar e conquistar." desc="A identidade visual é a “cara” da sua marca e um dos pilares para conquistar espaço e credibilidade no mercado, lembre-se quem não é visto não é lembrado!"  iconclass="identy" />
                <Card title="SOCIAL MEDIA" subtitle="Conectamos sua marca ao mundo, transformando seguidores em clientes fiéis." desc="O gerenciamento de redes sociais vai além de postar conteúdo: é uma estratégia essencial para conectar marcas ao público, impulsionar vendas e construir autoridade no mercado. "  iconclass="socialmedia" />
                <Card title="INOVAÇÃO" subtitle="Utilizar fotos reais dos produtos do cliente em campanhas de marketing é uma estratégia poderosa, que gera mais confiança e aproxima o público" desc=" no ambiente digital, onde tudo é muito visual, a autenticidade de imagens reais pode ser o diferencial decisivo."  iconclass="inovation" />
            </section>
        </section>
   </section>
   <div id="bt-more">
    <section class="bt-more">
        <span><a href="#">ver mais</a></span>
    </section>
</div>
</template>
<script>
    import Card from '../components/card.vue';
    export default {
        name:'AboutComponent',
        components:{
            Card
        }
    }
</script>
<style scoped>
    #about-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100vw;
        padding:50px 0;
        background:url('../imgs/SVG/bg-about.svg') no-repeat white;
        background-position: 10%;
        background-size: cover;
        clip-path: polygon(0 5%, 100% 0, 100% 100%, 100% 90%, 0 100%);
        z-index: 1;
    }
    .about{
        display: flex;
        flex-direction: column;
        gap: 50px;
        align-items: center;
        max-width: var(--maxw);
        width: 100%;
        height: 600px;
    }
    .about-title{
        margin-top: 30px;
        display: flex;
        flex-direction: column;
        text-align: center;
    }
    .about-cards{
        display: flex;
        width: 100%;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .about-title h1{
        font-size: 4rem;
        color: var(--darkgray);
        font-family: "Roboto";
    }
    .about-title p{
        font-size: 1.2rem;
        color:var(--darkgray);
    }
    #bt-more{
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%;
        max-width: var(--maxw);
    }
    .bt-more{
        display: flex;
        margin-top: -90px;
        justify-content: flex-end;
        align-items: end;
        height: 80px;
        z-index: 0;
        border-radius: 10px;
        background-color: var(--orange);
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }
    .bt-more:hover{
        margin-top: -80px;
    }
    .bt-more span a{
        display: flex;
        text-decoration: none;
        align-items: center;
        justify-content: end;
        padding: 14px;
        color: white;
        letter-spacing: 1px;
    }
    @media screen and (max-width: 768px){
        #about-container{
            height: 1480px;
        }
        .bt-more{
            margin-top: -250px;
            margin-right: 10px;
        }
        .bt-more:hover{
            margin-top: -240px; 
        }
        .about-cards{
            flex-direction: column;
            gap: 80px;
        }
        .about-title h1{
        font-size: 2rem;
        }
        .about-title p{
        font-size: 1rem;
        }
    }
</style>
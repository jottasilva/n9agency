<template>
    <article>
        <section class="fade-in">
            <h2>Social Media</h2>
            <ul>
                <li><b>Gestão de Redes Sociais:</b> Criação e manutenção de perfis em plataformas como Instagram, Facebook, LinkedIn, TikTok, entre outras.</li>
                <li><b>Criação de Conteúdo Visual e Textual:</b> Postagens criativas com design atrativo e copywriting envolvente.</li>
                <li><b>Planejamento e Calendário de Conteúdo:</b> Desenvolvimento de cronogramas estratégicos para manter sua marca ativa e engajada.</li>
                <li><b>Análise de Métricas:</b> Acompanhamento de resultados e relatórios para entender o desempenho e ajustar a estratégia.</li>
                <li><b>Campanhas de Publicidade Paga:</b> Gerenciamento de anúncios pagos para maximizar o alcance e conversões.</li>
            </ul>
        </section>
        <section class="fade-in">
            <h2>Designer Gráfico</h2>
            <ul>
                <li><b>Criação de Logotipos:</b> Design de logotipos exclusivos que representam a essência e os valores da sua marca.</li>
                <li><b>Material Gráfico para Impressão:</b> Flyers, cartazes, banners, cartões de visita e outros materiais impressos de alta qualidade.</li>
                <li><b>Design de Embalagens e Rótulos:</b> Criação de embalagens que atraem a atenção do consumidor e reforçam sua identidade de marca.</li>
                <li><b>Design para Web e Mídias Digitais:</b> Criação de peças visuais como banners, posts, anúncios e gráficos para sites e redes sociais.</li>
                <li><b>Edição de Imagens e Vídeos:</b> Processamento de imagens e vídeos para garantir uma apresentação profissional.</li>
            </ul>
        </section>
        <section class="fade-in">
            <h2>Identidade Visual</h2>
            <ul>
                <li><b>Criação de Identidade Visual Completa:</b> Desenvolvimento de todos os elementos visuais que compõem a identidade da marca, como logotipo, paleta de cores, tipografia e ícones.</li>
                <li><b>Manual de Marca:</b> Elaboração de um guia detalhado para o uso consistente de todos os elementos da identidade visual, tanto online quanto offline.</li>
                <li><b>Aplicações da Marca:</b> Criação de layouts e designs que aplicam sua identidade visual em diferentes plataformas e materiais, garantindo coesão e reconhecimento.</li>
                <li><b>Rebranding:</b> Atualização da identidade visual para marcas que buscam modernização ou reposicionamento no mercado.</li>
            </ul>
        </section>
        <section class="fade-in">
            <h2>Marketing</h2>
            <ul>
                <li><b>Estratégia de Marketing Digital:</b> Desenvolvimento de planos estratégicos para alcançar seus objetivos, seja aumento de vendas, engajamento ou construção de autoridade.</li>
                <li><b>SEO e Otimização de Sites:</b> Técnicas de otimização para melhorar o posicionamento do seu site nos motores de busca e atrair mais visitantes qualificados.</li>
                <li><b>Campanhas de Publicidade Online:</b> Gestão de anúncios no Google Ads, Facebook Ads, Instagram Ads, LinkedIn Ads, e outras plataformas para gerar tráfego e vendas.</li>
                <li><b>Consultoria e Análise de Mercado:</b> Diagnóstico detalhado sobre sua presença online, concorrência e recomendações para melhorar os resultados.</li>
            </ul>
        </section>
    </article>
</template>

<script>
export default {
    mounted() { 
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.classList.add("visible");
                        }, index * 300); 
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
section {
    background: white;
    padding: 30px;
    margin: 35px 0;
    opacity: 0; 
    transform: translateY(50px); 
    transition: all 0.8s ease-in-out; 
}
section.visible {
    opacity: 1;
    transform: translateY(0); 
}

article {
    width: 60vw;

}
h2 {
    color: var(--rxPrimary);
    padding: 10px 10px;
    text-transform: uppercase;
    letter-spacing: 5px;
    font-size:3rem;
}
ul li {
    color: var(--darkgray);
    padding: 5px 10px;
    font-family: 'Roboto';
    list-style: none;
    text-wrap: wrap;
}
h1 {
    font-size: 3rem;
    margin-bottom: 50px;
    color: var(--rxPrimary);
    font-family: 'Bebas Neue';
    letter-spacing: 3px;
    text-transform: uppercase;
}
@media screen and (max-width: 768px) {
    article{
        width: 90vw;
    }
    h2{
        font-size: 1.5rem;
        width: 100%;
        letter-spacing: 1px;
    }
}
</style>

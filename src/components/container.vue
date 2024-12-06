<template>
    <article id="container">
            <section class="phrase">
                <section class="text">
                    <h2>{{ phrase }}</h2>
                    <span>{{ middle_phrase }}</span>
                    <h1>{{ sub_phrase }}</h1>
                    <section class="subphrase"><p>{{desc_phrase}}</p></section>
                </section>  
            </section>
            <div class="image" :style="backgroundStyle" />      
    </article>
</template>
<script>
    import apiService, { url_api } from '@/services/apiService';
    export default{
        name:'my-Phrase',
        data(){
        return{
         info: [],
         phrase: 'CONECTANDO', // Inicialize com uma string padrão
         sub_phrase: 'NEGÓCIOS', // Inicialize com uma string padrão
         middle_phrase: 'IDÉIAS, TRANSFORMANDO', // Inicialize com uma string padrão
         img:  url_api+'/media/images/slide.svg',
         desc_phrase: 'levamos sua marca além dos limites com estratégias criativas e soluções digitais inovadoras.',
            }
        },
        computed: {
            backgroundStyle() {
            return {
                background: `url(${this.img}) no-repeat center`,
                backgroundSize: '100%',
            };
            },
            
        },
        async created() {
            const response = await apiService.getArchives(this.email); 
console.log('Dados recebidos da API:', response.data);
this.archives = response.data;
            try {
                const response = await apiService.getInfo();
                this.info = response.data;
                if (this.info.length > 0) {
                    this.phrase = this.info[0].phrase;
                    this.sub_phrase = this.info[0].sub_phrase;
                    this.middle_phrase = this.info[0].middle_phrase;
                    this.img = url_api + '/media/' + this.info[0].img;
                    this.desc_phrase = this.info[0].desc_phrase;
                }
            } catch (error) {
                console.error('Erro ao buscar Informações:', error);
            }
        },
      
    }
</script>
<style scoped>
    /* .phrase */
#container {
    display: flex;
    margin: 0 auto;
    max-width: var(--maxw);
    flex-grow: 1;
    padding-bottom: 30px;
    height: auto;
    min-height: 50vh;
    opacity: 0;
    animation: fadeIn 1s ease-out forwards;
}

.phrase {
    display: flex;
    align-items: center;
    opacity: 0;
    animation: fadeInUp 1s ease-out forwards 0.5s;
}

.phrase h2, .phrase h1 {
    letter-spacing: 4px;
    font-family: "Roboto", serif;
    font-weight: 800;
    color: var(--darkgray);
    transform: translateY(20px);
    animation: fadeInUp 1s ease-out forwards 1s;
}

.phrase h1 {
    font-size: 5.2rem;
    line-height: 80px;
}

.phrase h2 {
    font-size: 3.8rem;
    line-height: 60px;
}

.phrase p {
    font-size: 1.7rem;
    line-height: 27px;
    color: var(--rxPrimary);
    font-family: "Roboto", serif;
    font-weight: 500;
    padding-left: 5px;
    opacity: 0;
    animation: fadeInUp 1.5s ease-out forwards 1.5s;
}

.phrase span {
    background-color: var(--rxSecondary);
    color: white;
    font-size: .9rem;
    font-family: "Roboto", serif;
    font-weight: 500;
    margin-left: 225px;
    letter-spacing: 1px;
    padding: 5px 5px;
    border-radius: 4px;
    text-align: center;
    transform: translateY(20px);
    opacity: 0;
    animation: fadeInUp 1s ease-out forwards 2s;
}
.image {
    display: flex;
    width: 100vw;
    background-size: 100%;
    opacity: 0;
    animation: fadeIn 1.5s ease-out forwards 1.5s; 
}

@media screen and (max-width: 768px) {
    #container {
        flex-direction: column-reverse;
        width: 100vw;
        height: 80vh;
    }
    .phrase {
        width: 100%;
        text-align: center;
    }
    .subphrase {
        margin: 0 auto;
    }
    .phrase h1 {
        font-size: 3.5rem;
        text-align: center;
        width: 80vw;
        margin: 0 auto;
    }
    .phrase h2 {
        font-size: 2.4rem;
        width: 80vw;
        margin: 0 auto;
    }
    .phrase p {
        font-size: 1.4rem;
        flex-wrap: wrap;
        width: 80vw;
        padding: 10px 40px;
    }
    .phrase span {
        font-size: .9rem;
        width: 60vw;
        margin: 0 auto;
    }
    .text {
        width: 100%;
        flex-direction: column;
    }
    .image {
        display: flex;
        width: 80vw;
        align-self: center;
        height: 100vh;
    }
}
@keyframes fadeIn {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
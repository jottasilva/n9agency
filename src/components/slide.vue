<template>
    <article class="slide-box">
        <div class="arrow-left swiper-button-prev" @click="goToPrevSlide" :class="{'fade-effect': true}"></div>
        <section class="slide" :class="{'fade-effect': true}">
            <swiper-container
                ref="swiper"
                slides-per-view="3"
                space-between="20"
                loop="true"
                autoplay-delay="6000"
                autoplay-disable-on-interaction="false"
                pagination
                :breakpoints="{
                    320: { slidesPerView: 1, spaceBetween: 10 },       
                    480: { slidesPerView: 1, spaceBetween: 15 },        
                    768: { slidesPerView: 2, spaceBetween: 20 },       
                    1080: { slidesPerView: 1, spaceBetween: 20 },      
                    1324: { slidesPerView: 3, spaceBetween: 30 }}"
            >
                <swiper-slide v-for="(client, index) in clients" :key="index" :class="{'fade-slide': true}">
                    <Clients :img="client.img" :name="client.title" :desc="client.desc"/>
                </swiper-slide>
            </swiper-container>
        </section>
        <div class="arrow-right swiper-button-next" @click="goToNextSlide" :class="{'fade-effect': true}"></div>
    </article>
</template>

<script>
import { register } from 'swiper/element/bundle';      
register();
import Clients from '../components/clients.vue';
import apiService, { url_api } from '@/services/apiService';
export default {
    components: {
        Clients
    },
    name: "Slide",
    data() {
        return {
            swiperInstance: null,
            clients: []
            
        };
    },
    async created() {
    try {
        const response = await apiService.getPortfolio(); 
        this.clients = response.data;
        this.clients.forEach((client, index) => {
            console.log(`Cliente ${index + 1}:`, client);
            client.img = `${url_api}/media/${client.img}`;
        });
    } catch (error) {
        console.error('Erro ao buscar informações:', error);
    }
    },
    mounted() {
        this.swiperInstance = this.$refs.swiper.swiper;
    },
    methods: {
        goToNextSlide() {
            this.swiperInstance.slideNext();
        },
        goToPrevSlide() {
            this.swiperInstance.slidePrev();
        }
    }
};
</script>

<style scoped>
    swiper-container {
        width: 100%;
        height: 300px;
    }
    swiper-slide {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        transition: transform 0.4s ease-in-out, opacity 0.5s ease;
        opacity: 0;
        transform: translateY(20px);
    }

    swiper-slide.fade-slide {
        opacity: 1 !important;
        transform: translateY(0);
    }

    .slide-box {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100vw;
        height: 40vh;
        max-width: 1080px;
        padding: 20px 0;
        opacity: 0;
        transform: translateY(30px);
        animation: fadeIn 0.5s ease forwards;
    }

    .arrow-left, .arrow-right {
        width: 40px;
        height: 50px;
        cursor: pointer;
        background: url('../imgs/icons/seta.svg') no-repeat center;
        transition: all 0.3s ease-in-out;
        opacity: 0;
        animation: fadeIn 0.5s ease forwards;
        animation-delay: 0.5s;
    }
    .arrow-right {
    transform: rotate(180deg); 
    }

    .arrow-left:hover, .arrow-right:hover {
        scale: 1.2;
    }

    .fade-effect {
        opacity: 1 !important;
        transform: translateX(0);
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .slide {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 30px;
        width: 85%;
        transition: transform 0.5s ease-in-out;
    }

    .slide:hover {
        transform: scale(1.05);
    }

    @media screen and (max-width: 768px) {
        .slide {
            flex-direction: column;
        }
        .slide-box {
            width: 80vw;
        }
    }
</style>

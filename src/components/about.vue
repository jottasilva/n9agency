<template>
    <section id="about-container">
         <section class="about">
             <section class="about-title">
                 <h1>alguns serviços</h1>
                 <p>conheça um pouco mais do que nós fazemos</p>
             </section>
             <section class="about-cards">
                 <Card :title=title_ident :subtitle=msg_ident :desc=desc_ident iconclass="identy" />
                 <Card :title=title_media :subtitle=msg_media :desc=desc_media iconclass="socialmedia" />
                 <Card :title=title_invt :subtitle=msg_invt :desc=desc_invt iconclass="inovation" />
             </section>
         </section>
    </section>
    <div id="bt-more">
     <section class="bt-more">
         <span><RouterLink class="router" to="/portfolio">ver mais</RouterLink></span>
     </section>
 </div>
 </template>
 <script>
     import apiService from '@/services/apiService';
import Card from '../components/card.vue';
     export default {
        data(){
            return{
                title_ident:String,
                msg_ident:String,
                desc_ident:String,
                //
                title_media:String,
                msg_media:String,
                desc_media:String,
                //
                title_invt:String,
                msg_invt:String,
                desc_invt:String,
            }
        },
        async created() {
            try {
            const response = await apiService.getIdea();
            this.data = response.data;
            this.data.map(()=>{
                this.title_ident = this.data[0].title;
                this.msg_ident   = this.data[0].msg;
                this.desc_ident  = this.data[0].desc;

                this.title_media = this.data[1].title;
                this.msg_media   = this.data[1].msg
                this.desc_media  = this.data[1].desc;

                this.title_invt  = this.data[2].title;
                this.msg_invt    = this.data[2].msg;
                this.desc_invt   = this.data[2].desc;
            });

            } catch (error) {
            console.error('Erro ao buscar Informações:', error);
            }
        },
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
         opacity: 0;
         animation: fadeIn .5s ease-out forwards; 
     }
     .about{
         display: flex;
         flex-direction: column;
         gap: 50px;
         align-items: center;
         max-width: var(--maxw);
         width: 100%;
         height: calc(100vh / 1.5);
         opacity: 0;
         animation: slideInUp 1.5s ease-out forwards 0.5s;
     }
     .about-title{
         margin-bottom:30px;
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
         opacity: 0;
         animation: fadeIn 1.5s ease-out forwards 1s; 
     }
     .about-title h1{
         font-size: 4rem;
         color: var(--darkgray);
         font-family: "Roboto";
         transform: translateY(-20px); 
         animation: fadeInUp 1s ease-out forwards .5s; 
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
         clip-path: polygon(4% 0, 100% 0%, 94% 100%, 0% 100%);
         background-color: var(--orange);
         cursor: pointer;
         transition: all 0.3s ease-in-out;
         transform: translateY(40px);
         opacity: 0;
         animation: fadeInUp 1s ease-out forwards 2s; 
     }
     .bt-more:hover{
         margin-top: -80px;
     }
     .router{
         display: flex;
         text-decoration: none;
         align-items: center;
         justify-content: end;
         padding: 14px;
         color: white;
         font-weight: bold;
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
         .bt-more span{
             transform: rotate(-8deg);
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
     /* Keyframe Animations */
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
     @keyframes slideInUp {
         0% {
             opacity: 0;
             transform: translateY(0);
         }
         100% {
             opacity: 1;
             transform: translateY(50px);
         }
     }
 </style>
 
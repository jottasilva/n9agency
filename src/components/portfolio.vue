<template>

    <article>
       <section>
           <h2>{{ title }}</h2>
           <img :src="this.background" :alt="this.title">
           <p>{{ desc }}</p>
           <span>{{ features }}</span>
           <div><span>{{ date }}</span></div>
       </section>
    </article>
   </template>
   <script>
       export default{
        name:"Portfolio",
           props:{
               title:String,
               desc:String,
               date:String,
               background:String,
               features:String
           },
    }

   </script>
   <style scoped>
     section{
       display: flex;
       min-width: 300px;
       width:20vw;
       justify-content: center;
       flex-direction: column;
       padding: 30px;
       margin-bottom: 30px;
       background-color: white;
       transition: all .3s ease-in-out;
     }
     section:hover{
        scale: 1.1;
     }
     section p{
       padding:20px 0 10px 0;
       font-weight: bold;
       letter-spacing: 1px;
       color: var(--darkgray);
     }
     section h2{
       font-size: 1.2rem;
       color: var(--rxPrimary);
       padding: 0 0 20px 0;
     }
     section img{
       max-width: 30vw;
       max-height: 30vh;
     }
     section span:first-of-type {
     font-size: 0.8rem;
     color: rgb(144, 144, 144);
     margin: 0 0 10px 0;
     }
     div{
        width: 100%;
        text-align: end;
     }
     section span:nth-last-child(1){
        font-weight: bold;
        font-size: 0.7rem;
     }
     @media screen and (max-width: 768px) { 
      article{
        width: 100%;
        display: flex;
        justify-content: center;
      }
      section{
      width: 90%;
     }
    p, span{
      width: 100%;
      text-align: center;
     }
     section img{
       max-width: 100%;
       max-height: 100%;
     }
     }
   </style>
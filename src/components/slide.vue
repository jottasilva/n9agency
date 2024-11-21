<template>
    <article class="slide-box">
        <div class="arrow-left"/>
        <section class="slide">
            <section class="card-slide"/>
            <section class="card-slide"/>
            <section class="card-slide"/>
            <section class="card-slide"/>
            <section class="card-slide"/>
        </section>
        <div class="arrow-right"/>
    </article>
</template>
<script>    
    export default{
        name:"Slide"
    }
</script>
<style scoped>
    .slide-box{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100vw;
        height: 100vh;
        max-width: 1080px;
        height: 300px;
        padding: 20px 0;
    }
    .card-slide{
        width: 140px;
        height: 110px;
        background:url('../imgs/SVG/logo.slide.svg') no-repeat center;
        background-size: 70%;
        border-radius: 10px;
        transition: all .3s linear;
        cursor: pointer;
    }
    .card-slide:hover{
        scale: 1.2;
    }
    .arrow-left ,
     .arrow-right{
        width: 40px;
        height: 50px;
        cursor: pointer;
        background: url('../imgs/icons/seta.svg') no-repeat center;
        transition: all 0.3s linear;
    }
    .arrow-right{
        transform: rotate(180deg);
    }
    .arrow-left:hover, 
    .arrow-right:hover{
        scale: 1.2;
    }
    .slide{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 30px;
        width: 80%;
    }
</style>
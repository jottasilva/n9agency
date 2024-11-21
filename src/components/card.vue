<template>
    <div id="card">
        <section :class="['icon', iconclass]"></section>
        <section class="card-box">
            <h1>{{title}}</h1>
            <p>{{subtitle}}</p>
            <p>{{desc}}</p>
        </section>
    </div>
</template>
<script>
    export default{
        name:'CardAbout',
        props:{
            iconclass:String,
            title:String,
            subtitle:String,
            desc:String
        }
    }
</script>
<style scoped>
#card{
    display: flex;
    justify-content: center;
    flex-direction: column;
    max-width: 360px;
    max-height: 320px;
    width: 100%;
    height: 100%;
    transform: skew(-3deg);
}
.icon{
    width: 86px;
    height: 86px;
    z-index: 1;
}
.identy{
    background:url('../imgs/icons/visualidentify.png') no-repeat center;
    background-size: contain;
}
.socialmedia{
    background:url('../imgs/icons/socialmedia.png') no-repeat center;
    background-size: contain;
}
.inovation{
    background:url('../imgs/icons/ideology.png') no-repeat center;
    background-size: contain;
}
.card-box{
    max-width: 270px;
    max-height: 290px;
    height: 100%;
    width: 100%;
    z-index: 0;
    margin:0 auto;
    border-radius: 5px;
    background-color: white;
    -webkit-box-shadow: 10px 9px 5px -5px rgba(182, 182, 182, 0.1);
    -moz-box-shadow: 10px 9px 5px -5px rgba(182, 182, 182, 0.1);
    box-shadow: 10px 9px 5px -5px rgba(182, 182, 182, 0.1);
    margin-top: -30px;
    transition: all ease-in-out 0.4s;
    padding:40px 20px 20px 20px;
    border:1px #e9e9e9 solid;
}
.card-box:hover{
    scale: 1.1;
}
.card-box h1{
    font-size: 1.5rem;
    letter-spacing: 2px;
    color: var(--darkgray);
    font-family: "Roboto",sans-serif;
    margin-bottom: 10px;
    text-align: center;
}
.card-box p:nth-of-type(1) {
    color:var(--rxSecondary);  
}
.card-box p{
    font-size: 1rem;
    font-family: "Roboto",sans-serif;
    font-weight: 500px;
    margin-bottom: 10px;
    color:#444;
    text-align: center;
} 
</style>
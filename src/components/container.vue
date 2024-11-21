<template>
    <article id="container">
            <section class="phrase">
                <section class="text">
                        <h2>CONECTANDO</h2>
                        <span>IDÉIAS, TRANSFORMANDO</span>
                        <h1>NEGÓCIOS</h1>
                        <section class="subphrase"><p>levamos sua marca além dos limites com estratégias criativas e soluções digitais inovadoras.</p></section>
                </section>  
            </section>
            <div class="image" />      
    </article>
</template>
<script>
    export default{
        name:'my-Phrase',
        props:{
           msg:String
        }
    }
</script>
<style scoped>
    /* .phrase  */
    #container{
        display: flex;
        margin: 0 auto;
        max-width: var(--maxw);
        max-height: 60vh;
        flex-grow: 1;
        padding-bottom: 30px;
        height: 100vh;
    }
   .phrase{
        display: flex;
        align-items: center;
    }
    .phrase h2, .phrase h1{
        letter-spacing: 4px;
        font-family: "Roboto", serif;
        font-weight: 800;
        color: var(--darkgray);
    }
    .phrase h1{
        font-size: 5.2rem;
        line-height:80px;
    }
    .phrase h2{
        font-size: 3.8rem;
        line-height:60px;
    }
    .phrase p{
        font-size: 1.7rem;
        line-height: 27px;
        color: var(--rxPrimary);
        font-family: "Roboto", serif;
        font-weight: 500;
        padding-left: 5px;
    }
    .phrase span{
        background-color: var(--rxSecondary);
        color: white;
        font-size:.9rem;
        font-family: "Roboto", serif;
        font-weight: 500;
        margin-left: 225px;
        letter-spacing: 1px;
        padding:5px 5px;
        border-radius: 4px;
        text-align: center;
    }
    .text{
        display: flex;
        align-items: flex-start;
        flex-direction: column;
    }
   
    /* .image  */
    .image{
        display: flex;
        width: 100%;
        background: url('../imgs/SVG/slide.svg') no-repeat center;
        background-size:contain;
    }
    @media screen and (max-width: 768px){
        #container{
            flex-direction: column-reverse;
            width: 100vw;
            margin-left: 0;
        }
        .phrase{
            width:100%;
            text-align: center;
        }
        .subphrase{
            margin: 0 auto;
        }
        .phrase h1{
        font-size: 4rem;
        width:80vw;
        margin: 0 auto;
        }
        .phrase h2{
            font-size: 3rem;
            width:80vw;
            margin: 0 auto;
        }
        .phrase p{
            font-size: 1.4rem;
            flex-wrap: wrap;
            width:80vw;
            padding:10px 40px;
        }
        .phrase span{
            font-size:.9rem;
            width:60vw;
            margin: 0 auto;
        }
        .text{
            width: 100%;
            flex-direction: column;
        }
        .image{
            height: 80%;
        }
    }
</style>
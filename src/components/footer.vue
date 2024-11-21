<template>
    <article class="footer">
        <div class="footer-container">
            <section class="links">
                <h1>Links Úteis</h1>
                <ul>
                    <li><a href="#">Política de Privacidade</a></li>
                    <li><a href="#">Termos de uso</a></li>
                    <li><a href="#">Suporte</a></li>
                </ul>
            </section>
            <section class="info">
                <div class="info-logo"></div>
                <section class="link-infos">
                    <ul>
                        <li><a href="#">Jacarezinho, Paraná</a></li>
                        <li><a href="#">contato@n9agency.site</a></li>
                    </ul>
                </section>
            </section>
            <section class="social-icons">
                <h1>Nossas redes</h1>
                <section class="icons">
                    <div class="insta" />
                    <div class="wpp" />
                    <div class="in" />
                    <div class="fc" />
                </section>
            </section>
            
        </div>
        <section class="copyright">
            <span>® todos os direitos reservados.</span>
        </section>
    </article>
</template>
<script>
export default{
    name:"Footer"
}
</script>
<style scoped>
    .footer{
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 100vh;
        padding-top: 30px;
        background-color: white;
        border-top:22px var(--rxSecondary) solid;
        clip-path: polygon(0 20%, 100% 1%, 100% 100%, 0% 100%);
        max-height:250px;
    }
    .footer-container{
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        transform: rotate(-1.3deg);
        width: 100%;
        max-width: var(--maxw);
    }
    .links, .info,.social-icons{
        display: flex;
        flex-direction: column;
        padding: 20px;
    }
    .social-icons{
        text-align: center;
    }
    .info{
        display: flex;
        justify-content: center;
        flex-direction: row;
        align-items: center;
        height: 100px;
    }
    .info-logo{
        width: 100px;
        height: 100px;
        background:url('../imgs/SVG/logo.svg') no-repeat center;
        margin: 20px;
        transition: all 0.3s linear;
    }
    .info-logo:hover{
        background:url('../imgs/SVG/logo.hover.svg') no-repeat center;
    }
    .links h1, .social-icons h1{
        color:var(--dark);
        font-family: "Roboto",sans-serif;
        font-size: 1.6rem;
        letter-spacing: 1px;
        margin: 4px 0;
    }
    .links h1{
        color:var(--dark)
    }
    .links ul li, .link-infos ul li{
        display: flex;
        list-style: none;
        letter-spacing: 1px;
        font-size: 1.1rem;
    }
    .links ul li a, .link-infos ul li a{
        outline: none;
        margin:1px 0;
        text-decoration: none;
        color: #696969;
        transition: all .4s linear;
    }
    .links ul li a:hover, .link-infos ul li a:hover{
      color: var(--orange);
    }
    .icons{
      display: flex;
      flex-direction: row;
      gap: 14px;
      margin-top: 10px;
    }
   .insta, .in, .fc, .wpp{
        width: 45px;
        background-color: red;
        height: 45px;
        background: url('../imgs/icons/sociais.svg') no-repeat;
        background-size:cover;
    }
    .insta{
        background-position: 0;
    }
    .wpp{
        background-position: -65px;
    }
    .in{
        background-position:-133px;
    }
    .fc{
        background-position:-200px;
    }
    .copyright{
        transform: rotate(-1.3deg);
        color:var(--dark);
        padding: 30px;
        font-family: "Roboto";
        letter-spacing: 1px;
        padding:15px 0;
    }
    @media screen and (max-width: 768px){
        .footer{
            height: 800px;
            max-height: 700px;
        }
        .footer-container{
            align-items: center;
            gap: 50px;
            flex-direction: column;
        }
    }
</style>
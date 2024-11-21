<template>
  <div id="navbar">
    <nav class="nav">
        <section class="logo"></section>
        <div class="menu">
            <ul>
              <li>SOBRE NÓS</li>
              <li>O QUE FAZEMOS?</li>
              <li>PORTFÓLIO</li>
              <li>CONTATOS</li>
              <li class="login-btn">CLIENTE</li>
            </ul>
            <section class="hamburguer" />
        </div>

    </nav>
  </div>
</template>
<script>
export default {
  name: 'N9-Agency',
  props: {
    msg: String
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 #navbar {
  display: flex;
  justify-content: center;
  padding-top:60px;
  align-items: center;
  width: 100vw;
}
#navbar nav .logo{
  width: 212px;
  height: 175px;
  background:url('../imgs/logo.png') no-repeat center;
  background-size: contain;
}
#navbar nav .menu{
  display: flex;
  padding-top: 50px;
}
#navbar nav .menu ul{
  display: flex;
  align-items: center;
  list-style: none;
  gap: 20px;
  color:var(--darkgray);
}
#navbar nav .menu ul li{
  font-family: "Roboto", serif;
  font-weight: 500;
  cursor: pointer;
  font-style: normal;
  letter-spacing: .5px;
  font-size: 1rem;
  transition:all 0.3s linear;
}
#navbar ul li:hover{
  color: var(--orange);
}
#navbar nav .login-btn{
  background-color: var(--dark);
  border-radius: 4px;
  padding: 5px 10px;
  color: white;
  transform: skew(-10deg);
}
#navbar nav .login-btn:hover{
  background-color: var(--orange);
  color: white;
}
.nav{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-height: 200px;
  height: 100vh;
  width: 100vw;
  max-width:var(--maxw);
}
.hamburguer{
  width: 46px;
  height: 46px;
  background:url('../imgs/icons/menu-hamburguer.svg') no-repeat center;
  display: none;
  transition: all 0.3s linear;
}
.hamburguer:hover{
  scale: 1.1;
}
@media screen and (max-width: 768px){
  #navbar{
    width: 70vw;
    height: 300px;
    margin-top: 0;
    align-items: center;
    justify-content: space-between;
  }
  .hamburguer{
    display: flex;
  }
 
  .menu ul{ 
    display: none !important;
    flex-direction: column;
    margin: 0 auto;
    justify-content: center;
  }
  .menu ul li{
    margin: 0 auto;
    justify-content: center;
  }
}
</style>

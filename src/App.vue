<template>
  <div id="main">
    <NavBar msg="N9 Agência Digital"/>
    <Phrase msg="teste" />
    <About />
    <Slide />
    <Footer />
  </div>
</template>
<script>
import Phrase from './components/container.vue';
import NavBar from './components/navbar.vue';
import About from './components/about.vue';
import Slide from './components/slide.vue';
import Footer from './components/footer.vue';
export default {
name: 'App',
components: {
  NavBar,
  Phrase,
  About,
  Slide,
  Footer
}
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');
*{
font-family: Avenir, Arial, Helvetica, sans-serif;
margin: 0;
box-sizing: border-box;
padding: 0;
}
:root {
--rxPrimary: #5D0B8D;
--rxSecondary: #6F0BD7;
--orange : #EA5724;
--darkgray : #333333;
--dark : #1C1C1C;
--maxw: 1080px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html, body {
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  background: url("../src/imgs/SVG/bg.svg") no-repeat;
  background-size:cover;
  background-position:center;
}
#main{
display: flex;
flex-direction: column;
align-items: center;
}
#app {
border-top: 4px var(--rxPrimary) solid;
}

@media screen and (max-width: 768px){

}
</style>

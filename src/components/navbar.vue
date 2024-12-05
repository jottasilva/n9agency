<template>
  <div id="navbar">
    <nav class="nav">
        <section class="logo"></section>
        <div class="menu">
            <ul v-bind:class="{ show: menuOpen }">
              <RouterLink @click="hiddenMenu" class="router" active-class="active" to="/"><li>HOME</li></RouterLink>
              <RouterLink @click="hiddenMenu" class="router" active-class="active" to="/about"><li>SOBRE NÓS</li></RouterLink>
              <RouterLink @click="hiddenMenu" class="router" active-class="active" to="/services"><li>O QUE FAZEMOS?</li></RouterLink>
              <RouterLink @click="hiddenMenu" class="router" active-class="active" to="/portfolio"><li>PORTFÓLIO</li></RouterLink>
              <RouterLink @click="hiddenMenu" class="router" active-class="active-cl" to="/clients"><li class="login-btn">CLIENTE</li></RouterLink>
            </ul>
            <section @click="toggleMenu" class="hamburguer"></section>
        </div>
    </nav>
  </div>
  
</template>

<script>

export default {
  name: 'N9-Agency',
  data() {
    return {
      menuOpen: false,

    }
  },
 
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen; 
    },
    hiddenMenu(){
      this.menuOpen = false;
    }
  }
}

</script>

<style scoped>
 #navbar {
  display: flex;
  justify-content: center;
  padding-top: 60px;
  align-items: center;
  width: 100vw;
}
.router {
  text-decoration: none;
  color: var(--dark);
}
#navbar nav .logo {
  width: 212px;
  height: 175px;
  background: url('../imgs/logo.png') no-repeat center;
  background-size: contain;
}
#navbar nav .menu {
  display: flex;
  padding-top: 50px;
}
#navbar nav .menu ul {
  display: flex;
  align-items: center;
  list-style: none;
  gap: 30px;
  color: var(--darkgray);
}

#navbar nav .menu ul li {
  font-family: "Bebas Neue", serif;
  font-weight: 500;
  cursor: pointer;
  font-style: normal;
  letter-spacing: 0.5px;
  font-size: 1.6rem;
  transition: all 0.3s linear;
}

#navbar ul li:hover {
  color: var(--orange);
}
.router.active li {
  color: var(--orange);
  font-weight: bold;
}
.router.active-cl li {
  background-color: var(--orange);
}
#navbar nav .login-btn {
  background-color: var(--dark);
  border-radius: 4px;
  padding: 5px 20px;
  color: white;
  transform: skew(-10deg);
}
#navbar nav .login-btn:hover {
  background-color: var(--orange);
  color: white;
}
.nav {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-height: 200px;
  height: 100vh;
  width: 100vw;
  max-width: var(--maxw);
}
.hamburguer {
  width: 46px;
  height: 46px;
  background: url('../imgs/icons/menu-hamburguer.svg') no-repeat center;
  display: none;
  transition: all 0.3s linear;
}
.hamburguer:hover {
  scale: 1.1;
}
@media screen and (max-width: 768px) {
  #navbar nav .logo {
    width: 170px;
  }
  #navbar {
    width: 70vw;

    align-items: center;
    justify-content: space-between;
  }
  .hamburguer {
    display: flex;
    z-index: 10;
  }
  .menu ul {
    z-index: 9;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    justify-content: center;
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    position: absolute;
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    width: 100vw;
    height: 100vh;
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s, opacity 0.3s ease-in-out;
  }
  .menu ul.show {
    visibility: visible;
    opacity: 1;
  }
  .menu ul li {
    margin: 10px 0;
  }
}
</style>

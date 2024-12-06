<template>
    <header>
      <h2>Encontre seus arquivos</h2>
      <section>
        <input type="text" placeholder="Insira seu E-mail" v-model="email">
        <button @click="listArchives"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#fff" d="M10 18a7.95 7.95 0 0 0 4.897-1.688l4.396 4.396l1.414-1.414l-4.396-4.396A7.95 7.95 0 0 0 18 10c0-4.411-3.589-8-8-8s-8 3.589-8 8s3.589 8 8 8m0-14c3.309 0 6 2.691 6 6s-2.691 6-6 6s-6-2.691-6-6s2.691-6 6-6"/><path fill="#fff" d="M11.412 8.586c.379.38.588.882.588 1.414h2a3.98 3.98 0 0 0-1.174-2.828c-1.514-1.512-4.139-1.512-5.652 0l1.412 1.416c.76-.758 2.07-.756 2.826-.002"/></svg></button>
      </section>
    </header>
    <div>
      <nav>
        <span><b>Nome</b></span>
        <span><b>Arquivo</b></span>
        <span><b>Descrição</b></span>
        <span><b>Data / Hora</b></span>
      </nav>
      <div class="msg" v-if="archives.length === 0">
      <p> Digite seu e-mail para acessar seus arquivos.</p>
    </div>
      <article v-for="(item, index) in archives" :key="index" @click="redirect(item.archive)">
        <span>{{ item.title }}</span>
        <span>{{ item.specifications }}</span>
        <span>{{ item.description }}</span>
        <span style="white-space: pre;"> {{ formatDate(item.created_at) }}</span>
      </article>
    </div>
  </template>
  
  <script>
  import apiService, { url_api } from '@/services/apiService';
  export default {
    
    data() {
      return {
        email: '', 
        archives: [] 
      };
    },
    methods: {
        formatDate(isoDate) {
        const date = new Date(isoDate);
        const optionsDate = { day: 'numeric', month: 'long', year: 'numeric' };
        const optionsTime = { hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: false };
        const formattedDate = date.toLocaleDateString('pt-BR', optionsDate);
        const formattedTime = date.toLocaleTimeString('pt-BR', optionsTime);
        return `${formattedDate}\n${formattedTime}`;
         },
         
      async listArchives() {
        console.log("Buscando arquivos para o e-mail: " + this.email); 
        try {
          const response = await apiService.getArchives(this.email); 
          this.archives = response.data;  
          this.archives.forEach((client, index) => {
            console.log(`Cliente ${index + 1}:`, client);
            client.img = `${url_api}/media/${client.img}`;  
          });
        } catch (error) {
          console.error('Erro ao buscar informações:', error);
        }
      },
      redirect(link) {
    window.open(link, '_blank'); 
    }
    }
  };

  </script>
  
<style scoped>
    
    .bt{
        width: 32px;
        height: 32px;
    }
    .msg{
        width: 100%;
        padding: 20px;
        color: var(--orange);
        font-size: 1.4rem;
        letter-spacing: 1px;
        text-align: center;
    }
    header{
        display: flex;
        flex-direction: column;
        gap: 20px;
        justify-content: space-between;
        width:60vw;
        margin-top: 80px;
        padding: 20px;
        background: white;
        border-radius: 5px;
    }
    header input {
        width: 100%; 
        padding: 10px;
        box-sizing: border-box;
        outline: none;
        border: 1px #ddd solid;
        border-radius: 5px;
        font-size: 1.4rem;
        color: #817f7f;
    }
   
    header section{
        display: flex;
        gap: 30px;
    }
    header button{
        border:1px var(--rxPrimary) solid;
        border-radius: 5px;
        color: white;
        padding: 0 20px;
        cursor: pointer;
        background-color: var(--rxSecondary);
        transition: all .5s linear;
    }
    header button:hover{
        background-color: var(--rxPrimary);
    }
    div{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        width: 60vw;
        background:white;
        padding: 30px;
        border-radius: 8px;
        margin: 20px 0;
    }
    nav{
        display: flex;
        justify-content: space-between;
    }
    nav span{
        padding: 20px;
    }
    nav span {
        width: calc(100vw/4);
        background: rgb(243, 243, 243);
        text-align: start;
    }
    article{
        display: flex;
        height: 10vh;
        justify-content: space-between;
        color: #817f7f;  
        border-top: 1px #ddd solid;
    }
    article span{
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        font-size: .8rem;
        transition: all .2s linear
    }
 
    article span{
        width: calc(100vw/3);

    }
    article span:nth-child(1){
        font-weight: bold;
    }
    article span:nth-child(1):hover{
        color: var(--rxSecondary);
        cursor: pointer;
    }
    article span:nth-child(3){
        color: var(--rxPrimary);
    }
    article span:nth-child(4){
        font-size: .7rem;
    }
    @media screen and (max-width: 768px) {
        div, header{
            width: 90vw;
            padding: 0;
            background: none;
        }
        header{
            padding: 20px;
        }
        nav{
           display: none;
        }
        section{
            flex-direction: column;
            padding: 10px 0;
        }
        section button{
            padding: 10px 0;
        }
        article{
            flex-direction: column;
            width:90vw;
            align-items: center;
            height: auto;
            min-height:35vh;
            margin: 20px 0;
            background: white;
            border-top: 3px var(--orange) solid;
        }
        article span{
            min-width: 85vw;
            border: 0;
            gap: 0;
            justify-content: center;
        }
        article span:nth-child(1){
            font-weight: bold;
            font-size: 1rem;
        }
        article span:nth-child(4){
            font-size: 1rem;
            font-weight: bold;
        }
  
    }
</style>
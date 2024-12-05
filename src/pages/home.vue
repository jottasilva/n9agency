<script>
  import About from '../components/about.vue';
  import Slide from '../components/slide.vue';
  import Phrase from '../components/container.vue';
export default {

  components:{
    Slide,
    About,
    Phrase
  },
}
</script>
<template>
      <Phrase msg="teste" />
      <About />
      <Slide />
</template>
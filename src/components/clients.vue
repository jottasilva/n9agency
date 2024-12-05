<template>
  <div :style="containerStyle"
  @mouseenter="onMouseEnter"
    @mouseleave="onMouseLeave">
    <h2>{{ name }}</h2>
    <p>{{ desc }}</p>
  </div>
</template>

<script>
export default {
  name: 'Clients',
  props: {
    name: String,
    desc: String,
    img: String,
  },
  data() {
    return {
      isHovered: false,
    };
  },

  computed: {
    containerStyle() {
      return {
        position: 'relative',
        width: '90%',
        height: '90%',
        overflow: 'hidden',
        background: 'white',
        borderRadius: '8px',
        backgroundImage: `url(${this.img})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        transition: 'all 0.3s ease',
        transform: this.isHovered ? 'scale(1.05)' : 'scale(1)', 
        boxShadow: this.isHovered ? '0 4px 4px rgba(0, 0, 0, 0.2)' : 'none',
      };
    },
  },
  methods: {
    onMouseEnter() {
      this.isHovered = true;
    },
    onMouseLeave() {
      this.isHovered = false;
    },
  },

};
</script>

<style scoped>
div {
  display: flex;
  position: relative;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px 0;
  cursor: pointer;
  align-items: center;
  overflow: hidden;
  background: white;
  border-radius: 8px;
  -webkit-box-shadow: 6px 6px 10px 0px rgba(0, 0, 0, 0.22);
  -moz-box-shadow: 6px 6px 10px 0px rgba(0, 0, 0, 0.22);
  box-shadow: 6px 6px 10px 0px rgba(0, 0, 0, 0.22);
  transition: all .5s linear;
}

div h2 {
  font-size: 1.2rem;
  line-height: 30px;
  display: flex;
  width: 100%;
  max-width: 80%;
  max-height: 30%;
  align-items: center;
  justify-content: center;
  letter-spacing: 1px;
  display: -webkit-box;
  -webkit-line-clamp: 3; 
  -webkit-box-orient: vertical;
  line-clamp: 3;
  overflow: hidden;
  color: white;
  text-align: center;
  font-family: "Roboto";
  padding: 5px 10px;
  background-color: var(--rxPrimary);
  border-radius: 6px;
}

div p {
  background-color: white;
  color: var(--dark);
  font-size: .8rem;
  max-height: 50%;
  max-width: 80%;
  font-weight: bold;
  margin: 10px;
  padding: 8px;
  border-radius: 5px;
}
</style>
